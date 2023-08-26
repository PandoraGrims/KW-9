from rest_framework import status
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from api_v1.serializers import PhotoSerializer, AlbumSerializer, FavoriteSerializer
from webapp.models import Photo, Album
from rest_framework.decorators import action


class AddToFavoriteViewPhoto(APIView):
    def post(self, request):
        serializer = FavoriteSerializer(data=request.data)
        if serializer.is_valid():
            photo_id = serializer.validated_data['id']
            photo = Photo.objects.get(pk=photo_id)
            request.user.favorite_photos.add(photo)
            return Response({"success": True})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddToFavoriteViewAlbum(APIView):
    def post(self, request):
        serializer = FavoriteSerializer(data=request.data)
        if serializer.is_valid():
            album_id = serializer.validated_data['id']
            album = Album.objects.get(pk=album_id)
            request.user.favorite_albums.add(album)
            return Response({"success": True})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RemoveFavoriteViewPhoto(APIView):
    def post(self, request):
        serializer = FavoriteSerializer(data=request.data)
        if serializer.is_valid():
            photo_id = serializer.validated_data['id']
            photo = Photo.objects.get(pk=photo_id)
            request.user.favorite_photos.remove(photo)
            return Response({"success": True})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RemoveFavoriteViewAlbum(APIView):
    def post(self, request):
        serializer = FavoriteSerializer(data=request.data)
        if serializer.is_valid():
            album_id = serializer.validated_data['id']
            album = Album.objects.get(pk=album_id)
            request.user.favorite_albums.remove(album)
            return Response({"success": True})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ApiViewSet(ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        return Response(PhotoSerializer(self.get_object()).data)

    def get_serializer_class(self):
        if self.action in ("retrieve", "list"):
            return PhotoSerializer
        return PhotoSerializer

    def get_permissions(self):
        super().get_permissions()
        if self.request.method in SAFE_METHODS:
            return []
        return [IsAuthenticated()]


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        user.auth_token.delete()
        return Response({'status': 'ok'})
