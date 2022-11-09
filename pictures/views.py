from rest_framework import viewsets
from pictures.models import CatPicture
from pictures.serializers import CatPictureSerializer

class CatPictureViewSet(viewsets.ModelViewSet):
    queryset = CatPicture.objects.all()
    serializer_class = CatPictureSerializer
