import re
from docx import Document

from document_processor.processors.doc_processor import DocProcessor
from document_processor.processors.docx_processor import DocxProcessor
from document_processor.processors.jpg_processor import JPGProcessor
from document_processor.processors.pdf_processor import PDFProcessor
from document_processor.processors.png_processor import PNGProcessor
from document_processor.processors.txt_processor import TxtProcessor
from document_processor.processors.xml_processor import XMLProcessor


class DocumentProcessorSelector:
    SUPPORTED_EXTENSION: list[str] = [".doc", "docx", ".txt", "png", "jpg", "pdf", "xml"]

    def _is_supported_extension(self, filename: str) -> bool:
        if filename[-3:] in self.SUPPORTED_EXTENSION:
            return True
        if filename[-4:] in self.SUPPORTED_EXTENSION:
            return True
        return False

    @classmethod
    def _get_file_extension(cls, file_name: str) -> str:
        separator_pos: int | None = None
        for i in range(len(file_name) - 1, 0, -1):
            if file_name[i] == '.':
                separator_pos = i
                break

        if separator_pos is None:
            raise Exception("Filename not contain extension")

        file_extension: str = file_name[separator_pos:]

        return file_extension

    @classmethod
    def get_processor(cls, filename: str, file_path: str):
        """
        Получение класса для обработки файла по его расширению
        :param filename:
        :param file_path:
        :return:
        """

        if not cls._is_supported_extension(filename):
            raise Exception("Unsupported filetype")

        match cls._get_file_extension(filename):
            case ".txt":
                return TxtProcessor
            case ".docx":
                return DocxProcessor
            case ".doc":
                return DocProcessor
            case ".png":
                return PNGProcessor
            case ".jpg":
                return JPGProcessor
            case ".pdf":
                return PDFProcessor
            case ".xml":
                return XMLProcessor
            case _:
                raise Exception("Unsupported filetype")


def main() -> None:
    doc = DocxProcessor(
        document_name="document.docx"
    )

    doc.stupid_phone_numbers_hiding()

    doc.stupid_inn_hiding()

    doc.save_document()


if __name__ == "__main__":
    # main()

    DocumentProcessorSelector._get_file_type("filename.txt")

'''
ОГРН 1026103165241,
ИНН 6163027810, КПП 616301001
'''
