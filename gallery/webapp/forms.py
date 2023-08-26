from django import forms

from webapp.models import Photo, Album


class SearchForm(forms.Form):
    search = forms.CharField(max_length=30, required=False, label="Найти")


class AlbumForm(forms.ModelForm):
    title = forms.CharField(max_length=50, required=True, label="Название")
    description = forms.CharField(max_length=2000, required=True, label="Описание")

    class Meta:
        model = Album
        fields = ["title", "description", 'is_private']


class PhotoForm(forms.ModelForm):

    class Meta:
        model = Photo
        fields = ["content", "image", "album", "is_private"]
