from django.urls import path

from webapp.views.photos import PhotoListView, PhotoCreateView, PhotoDetailView, PhotoUpdateView, PhotoDeleteView

app_name = "webapp"

urlpatterns = [
    path('', PhotoListView.as_view(), name="photo_list"),
    path('photos/add/', PhotoCreateView.as_view(), name="photo_add"),
    path('post/<int:pk>/', PhotoDetailView.as_view(), name="photo_view"),
    path('post/<int:pk>/update/', PhotoUpdateView.as_view(), name="photo_update"),
    path('post/<int:pk>/delete/', PhotoDeleteView.as_view(), name="photo_delete"),
]
