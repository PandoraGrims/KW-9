from django import forms

from webapp.models import Photo, Album


class SearchForm(forms.Form):
    search = forms.CharField(max_length=30, required=False, label="Найти")


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ["content", "image"]


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ["title", "author"]
