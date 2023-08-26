from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from webapp.models import Post, Like


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def validate_title(self, value):
        if len(value) < 5:
            raise ValidationError("Длина меньше 5 символов не разрешена")
        return value


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
