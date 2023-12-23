from document_processor.processors.doc_processor import DocProcessor
from document_processor.processors.docx_processor import DocxProcessor
from document_processor.processors.jpg_processor import JPGProcessor
from document_processor.processors.pdf_processor import PDFProcessor
from document_processor.processors.png_processor import PNGProcessor
from document_processor.processors.txt_processor import TxtProcessor
from document_processor.processors.xml_processor import XMLProcessor
from docx import Document


class DocumentProcessorSelector:
    SUPPORTED_EXTENSION: list[str] = [".doc", "docx", ".txt", "png", "jpg", "pdf", "xml"]

    def _is_supported_extension(self, file_name: str) -> bool:
        if file_name[-3:] in self.SUPPORTED_EXTENSION:
            return True
        if file_name[-4:] in self.SUPPORTED_EXTENSION:
            return True
        return False

    def _get_file_extension(self, file_name: str) -> str:
        separator_pos: int | None = None
        for i in range(len(file_name) - 1, 0, -1):
            if file_name[i] == '.':
                separator_pos = i
                break

        if separator_pos is None:
            raise Exception("Filename not contain extension")

        file_extension: str = file_name[separator_pos:]

        return file_extension

    def get_processor(
            self, filename: str
    ) -> TxtProcessor | DocxProcessor | DocProcessor | PNGProcessor | JPGProcessor | PDFProcessor | XMLProcessor:
        """
        Получение класса для обработки файла по его расширению
        :param filename:
        :return:
        """

        if not self._is_supported_extension(file_name=filename):
            raise Exception("Unsupported filetype")

        match self._get_file_extension(filename):
            case ".txt":
                return TxtProcessor(
                    document_name=filename
                )
            case ".docx":
                return DocxProcessor(
                    document_name=filename,
                )
            case ".doc":
                return DocProcessor()
            case ".png":
                return PNGProcessor()
            case ".jpg":
                return JPGProcessor()
            case ".pdf":
                return PDFProcessor()
            case ".xml":
                return XMLProcessor()
            case _:
                raise Exception("Unsupported filetype")

    # def __init__(self, file_name, str, file_path: str):
    #     self.get_processor(
    #         filename=file_name,
    #         file_path=file_path
    #     )


def main() -> None:

    doc: DocxProcessor = DocumentProcessorSelector().get_processor(
        filename="document.docx",
    )

    doc.stupid_phone_numbers_hiding()

    doc.stupid_inn_hiding()

    doc.save_document()


if __name__ == "__main__":
    main()
