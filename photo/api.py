from .models import Photo
from rest_framework import serializers, viewsets, status, mixins
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'


class PhotoBodySerializer(serializers.Serializer):
    author = serializers.IntegerField()
    text = serializers.CharField()
    image = serializers.URLField()


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    @swagger_auto_schema(request_body=PhotoBodySerializer)
    def add(self, request):
        photo = Photo.objects.filter(**request.data)
        if photo.exists():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

        photo_serializer =PhotoSerializer(data=request.data, partial=True)
        if not photo_serializer.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

        photo = photo_serializer.save()

        return Response(PhotoSerializer(photo).data, status=status.HTTP_201_CREATED)