from django.http import FileResponse, JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.files.storage import default_storage

from docDefender_backend import settings
from docDefender_backend.settings import MEDIA_ROOT
from .processors.docx_processor import DocxProcessor
from .processors.txt_processor import TxtProcessor
from .models import FileModel


# Create your views here.

class UploadFilesView(APIView):
    """

    """

    def handle_uploaded_file(file, filename: str):
        with open(f'some/file/{filename}', "wb+") as destination:
            for chunk in file.chunks():
                destination.write(chunk)

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        # usernames = [user.username for user in User.objects.all()]
        return Response("Список файлов")

    def post(self, request, format=None):
        file_obj = request.FILES['file']

        file = request.FILES['file']
        file_name = default_storage.save(file.name, file)
        file = default_storage.open(file_name)
        file_url = default_storage.url(file_name)

        new_file: FileModel = FileModel(
            file_path=f'{settings.MEDIA_ROOT}anon_{file_name}',
            file_name=file_name
        )
        new_file.save()

        doc = TxtProcessor(
            document_name=file_name
        )

        doc.anonymize_doc()

        doc.save_document()

        # doc = DocxProcessor(
        #     document_name=f'{file_name}'
        # )
        #
        # doc.anonymize_doc()
        #
        # doc.save_document()



        # response = FileResponse(open(f'{settings.MEDIA_ROOT}anon_{file_name}', 'rb'))

        # return Response(new_file.id)
        return JsonResponse({'id': new_file.id})

    def get(self, request, format=None):

        id: int = int(request.query_params.get('id'))

        file_path: str = FileModel.objects.get(id=id).file_path

        response = FileResponse(open(file_path, 'rb'))

        return response
