from django.urls import path

from webapp.views.album import AlbumCreateView, AlbumDetailView, AlbumUpdateView, AlbumDeleteView
from webapp.views.photos import PhotoListView, PhotoCreateView, PhotoDetailView, PhotoUpdateView, PhotoDeleteView, \
    view_photo_by_token

app_name = "webapp"

urlpatterns = [
    path('', PhotoListView.as_view(), name="photo_list"),
    path('photos/add/', PhotoCreateView.as_view(), name="photo_add"),
    path('post/<int:pk>/', PhotoDetailView.as_view(), name="photo_view"),
    path('post/<int:pk>/update/', PhotoUpdateView.as_view(), name="photo_update"),
    path('post/<int:pk>/delete/', PhotoDeleteView.as_view(), name="photo_delete"),

    path('album/add/', AlbumCreateView.as_view(), name="album_add"),
    path('album/<int:pk>/', AlbumDetailView.as_view(), name="album_view"),
    path('album/<int:pk>/update/', AlbumUpdateView.as_view(), name="album_update"),
    path('album/<int:pk>/delete/', AlbumDeleteView.as_view(), name="album_delete"),

    path('view_photo_by_token/<uuid:token>/', view_photo_by_token, name='view_photo_by_token'),
]
