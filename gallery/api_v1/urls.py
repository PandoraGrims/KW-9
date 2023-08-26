from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from api_v1.views import ApiViewSet, LogoutView, AddToFavoriteViewPhoto, AddToFavoriteViewAlbum, \
    RemoveFavoriteViewPhoto, RemoveFavoriteViewAlbum

app_name = "api_v1"

router = DefaultRouter()
router.register("photos", ApiViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path('login/', obtain_auth_token, name='api_token_auth'),
    path('logout/', LogoutView.as_view(), name='api_token_delete'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/favorites_photo/add/', AddToFavoriteViewPhoto.as_view(), name='add_to_favorite_photo'),
    path('api/favorites_album/add/', AddToFavoriteViewAlbum.as_view(), name='add_to_favorite_album'),
    path('api/favorites_photo/remove/', RemoveFavoriteViewPhoto.as_view(), name='remove_from_favorite_photo'),
    path('api/favorites_album/remove/', RemoveFavoriteViewAlbum.as_view(), name='remove_from_favorite_album'),
]
