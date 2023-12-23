import re


class TxtProcessor:
    """
    Класс для обработки TXT
    """

    PHONE_NUMBER_REGEXP: str = r'\b\+?[7,8](\s*\d{3}\s*\d{3}\s*\d{2}\s*\d{2})\b'
    INN_REGEXP: str = r'ИНН'

    def __init__(self, document_name: str, file_path: str):
        self.document_name: str = document_name
        self.output_document_name: str = f'{self.document_name}_anonymized'

        self.NUMBER_PATTERN = re.compile(self.PHONE_NUMBER_REGEXP)
        self.INN_PATTERN = re.compile(self.INN_REGEXP)

        self.document = open(self.document_name, 'r')

        self.document_content = self.document.read()

        self.document.close()

    def _print_content(self) -> None:
        """
        Вывод содержимого документа в консоль
        :return:
        """
        for line in self.document_content.split('\n'):
            print(line)

    def anonymize_doc(self):

        for i in range(1, len(self.document_content) - 1):
            if self.document_content[i].isdigit() and \
                    self.document_content[i + 1] != '.' and \
                    self.document_content[i - 1] != '.':
                self.document_content = self.document_content.replace(self.document_content[i], "#")

    def save_document(self):
        output_file = open(f'{self.output_document_name}.txt', 'w')
        output_file.write(self.document_content)
        output_file.close()


def main():
    doc = TxtProcessor(
        document_name="document.txt",
        file_path=""
    )

    doc._print_content()

    doc.anonymize_doc()

    doc.save_document()


if __name__ == "__main__":
    main()
