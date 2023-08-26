from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from webapp.models import Photo, Album


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'

    def validate_title(self, value):
        if len(value) < 5:
            raise ValidationError("Длина меньше 5 символов не разрешена")
        return value


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'
