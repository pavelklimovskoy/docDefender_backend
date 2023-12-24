from anonympy.pandas import dfAnonymizer
from anonympy.pandas.utils_pandas import load_dataset

import pandas as pd
import spacy


from docDefender_backend import settings
# class settings:
#     MEDIA_ROOT = '/home/sunshine/docDefender_backend/web_application/media/'


class XMLProcessor:

    def _hide_string(self, data: str) -> str:
        res = ""

        for ch in data:
            if ch.isalpha() and ch != '@':
                res += '#'
            else:
                res += ch

        return res

    def _hide_email_string(self, data: str) -> str:
        res = ""

        for ch in data:
            if ch.isalpha() and ch != '@':
                res += '*'
            else:
                res += ch

        return res

    def _hide_email(self, data: str) -> str:

        if '@' in str(data):
            return self._hide_email_string(data)
        else:
            return data

    def __init__(self, document_name: str):
        self.document_name: str = document_name
        self.output_document_name: str = f'{settings.MEDIA_ROOT}anon_{self.document_name}'

        self.language_model = spacy.load("ru_core_news_sm")
        self.input_file_path = f'{settings.MEDIA_ROOT}{self.document_name}'

        self.data = pd.read_excel(self.input_file_path)

    def anonymize_doc(self) -> None:

        # Определение чувствительных столбцов на основе наличия именованных сущностей
        sensitive_columns = []
        for column_name in self.data.columns:
            for i, cell_value in enumerate(self.data[column_name].astype(str)):

                tokens = self.language_model(cell_value)

                for token in tokens:
                    if token.ent_type_ != "":
                        sensitive_columns.append((column_name, token,))
                        hided_data = self._hide_string(self.data.at[i, column_name])
                        self.data.at[i, column_name] = hided_data
                        break

                data = self.data.at[i, column_name]
                self.data.at[i, column_name] = self._hide_email(data)

    def save_document(self) -> None:
        self.data.to_excel(self.output_document_name, index=False)


def main() -> None:
    doc = XMLProcessor(
        document_name="document.xlsx"
    )

    doc.anonymize_doc()

    doc.save_document()


if __name__ == "__main__":
    main()
