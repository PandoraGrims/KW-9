from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from webapp.forms import AlbumForm, AddPhotosToAlbumForm
from webapp.models import Album, Photo, AlbumPhoto


class AlbumCreateView(LoginRequiredMixin, CreateView):
    form_class = AlbumForm
    template_name = "albums/album_create.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AlbumDetailView(DetailView):
    queryset = Album.objects.all()
    template_name = "albums/album_view.html"


class AlbumDeleteView(PermissionRequiredMixin, DeleteView):
    model = Album
    template_name = "albums/album_delete.html"

    def has_permission(self):
        return self.request.user == self.get_object().author

    def get_success_url(self):
        return reverse("accounts:profile", kwargs={"pk": self.request.user.pk})


class AlbumUpdateView(PermissionRequiredMixin, UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = "albums/album_update.html"

    def has_permission(self):
        return self.request.user == self.get_object().author


class AddPhotosToAlbumView(View):
    def get(self, request, album_id):
        album = get_object_or_404(Album, pk=album_id)
        form = AddPhotosToAlbumForm()
        return render(request, 'partial/add_photos_to_album.html', {'album': album, 'form': form})

    def post(self, request, album_id):
        album = get_object_or_404(Album, pk=album_id)
        photo_pks = request.POST.getlist('selected_photos')
        photos = Photo.objects.filter(pk__in=photo_pks)
        for photo in photos:
            AlbumPhoto.objects.create(album=album, photo=photo)
        return redirect('webapp:album_view', pk=album_id)

