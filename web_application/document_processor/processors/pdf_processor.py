# import pytesseract
# from anonympy.pdf import pdfAnonymizer
#
# from docDefender_backend import settings
from docDefender_backend import settings
from docx import Document


class PDFProcessor:
    """
    Обработка pdf
    """

    def __init__(self, document_name: str):
        self.document_name: str = document_name
        self.output_document_name: str = f'{self.document_name}'

        self.document = Document(settings.MEDIA_ROOT + self.document_name)

    # def anonymize_doc(self):
    #     anonym = pdfAnonymizer(path_to_pdf=f'{settings.MEDIA_ROOT}{self.document_name}')
    #
    #     anonym.anonymize(
    #         output_path=f'{settings.MEDIA_ROOT}anon_{self.document_name}.pdf',
    #         remove_metadata=True,
    #         fill='green',
    #         outline='green'
    #     )

    def save_document(self) -> None:
        pass

