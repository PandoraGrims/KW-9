import uuid

from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Album(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name="Название")
    description = models.TextField(max_length=1000, verbose_name="Описание")
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="albums", verbose_name="Автор")
    created_at = models.DateTimeField(auto_now_add=True)
    is_private = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.pk} {self.title}"

    def get_absolute_url(self):
        return reverse("webapp:album_view", kwargs={"pk": self.pk})

    class Meta:
        db_table = "albums"
        verbose_name = "Альбом"
        verbose_name_plural = "Альбомы"


class Photo(models.Model):
    image = models.ImageField(upload_to="photos", verbose_name='Картинка')
    content = models.CharField(max_length=2000, null=False, blank=False, verbose_name="Подпись")
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="photos", verbose_name="Автор")
    album = models.ForeignKey("webapp.Album", on_delete=models.SET_NULL, verbose_name="Альбом", related_name="photos",
                              null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
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
