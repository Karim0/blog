from .models import Flower, FlowerPhoto
from rest_framework import routers, serializers, viewsets, status
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from django.http import JsonResponse
from PIL import Image


class FlowerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Flower
        fields = ['name', 'desc']


class FlowerPhotoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FlowerPhoto
        fields = ['flower', 'img']


class FlowerViewSet(viewsets.ModelViewSet):
    queryset = Flower.objects.all()
    serializer_class = FlowerSerializer


class FlowerPhotoViewSet(viewsets.ModelViewSet):
    queryset = Flower.objects.all()
    serializer_class = FlowerSerializer


class ImageUploadParser(FileUploadParser):
    media_type = 'image/*'


class ModelPredict(APIView):
    parser_class = (ImageUploadParser,)

    def put(self, request, format=None):
        '''
        From the presented photo, we predict what kind of flower it is.
        '''
        if 'file' not in request.data:
            raise ParseError("Empty content")
        f = request.data['file']

        return JsonResponse({'flower_id': -1})


router = routers.DefaultRouter()
router.register(r'flower', FlowerViewSet)
router.register(r'flower_photo', FlowerViewSet)
