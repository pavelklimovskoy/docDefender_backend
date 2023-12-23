# import pytesseract
# from anonympy.pdf import pdfAnonymizer
#
# from docDefender_backend import settings


class PDFProcessor:
    """
    Обработка pdf
    """

    def __init__(self):
        pass

    def anonymize_doc(self):
        pass

    def save_document(self):
        pass

    # def pdfanon(self, filename: str) -> None:
    #     anonym = pdfAnonymizer(path_to_pdf=f'{settings.MEDIA_ROOT}{filename}')
    #
    #     anonym.anonymize(
    #         output_path=f'{settings.MEDIA_ROOT}anon_{filename}.pdf',
    #         remove_metadata=True,
    #         fill='green',
    #         outline='green'
    #     )
