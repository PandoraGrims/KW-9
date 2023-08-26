import uuid

from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Album(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="albums", verbose_name="Автор")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pk} {self.author}"

    def get_absolute_url(self):
        return reverse("webapp:album_view", kwargs={"pk": self.pk})

    class Meta:
        db_table = "albums"
        verbose_name = "Альбом"
        verbose_name_plural = "Альбомы"


class Photo(models.Model):
    image = models.ImageField(upload_to="photos", verbose_name='Картинка')
    content = models.CharField(max_length=255)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="photos", verbose_name="Автор")
    album = models.ForeignKey(Album, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_private = models.BooleanField(default=False)
    token = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        return f"{self.pk} {self.author}"

    def get_absolute_url(self):
        return reverse("webapp:photo_view", kwargs={"pk": self.pk})

    class Meta:
        db_table = "photos"
        verbose_name = "Картинка"
        verbose_name_plural = "Картинки"


class AlbumPhoto(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.album} {self.photo}"

