
from django.http import FileResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.files.storage import default_storage

from docDefender_backend import settings
from docDefender_backend.settings import MEDIA_ROOT


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

        print(request.FILES.keys())

        print(file_obj)
        # print(file_obj.read_lines())

        file = request.FILES['file']
        file_name = default_storage.save(file.name, file)

        file = default_storage.open(file_name)
        file_url = default_storage.url(file_name)

        # file_location = default_storage.location(file_name)
        #
        # print(file_url)
        #
        # print(file_location)

        print(settings.MEDIA_ROOT + file_name)



        response = FileResponse(open(settings.MEDIA_ROOT + file_name, 'rb'))

        return response


'''
#  Saving POST'ed file to storage
file = request.FILES['myfile']
file_name = default_storage.save(file.name, file)

#  Reading file from storage
file = default_storage.open(file_name)
file_url = default_storage.url(file_name)
'''