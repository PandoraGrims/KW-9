from django import forms

from webapp.models import Photo, Album


class SearchForm(forms.Form):
    search = forms.CharField(max_length=30, required=False, label="Найти")


class PhotoForm(forms.ModelForm):
    album = forms.ModelChoiceField(queryset=Album.objects.all(), empty_label="(Nothing)")

    class Meta:
        model = Photo
        fields = ["content", "image"]


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ["title", "description"]


class AddPhotosToAlbumForm(forms.Form):
    selected_photos = forms.ModelMultipleChoiceField(queryset=Photo.objects.all(), widget=forms.CheckboxSelectMultiple)
