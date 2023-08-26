from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Album
from webapp.forms import AlbumForm

def album_detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    # ...render the template with the album details

def create_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            album = form.save(commit=False)
            album.author = request.user
            album.save()
            return redirect('album_detail', album_id=album.id)
    else:
        form = AlbumForm()
    # ...render the template with the form

def edit_album(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('album_detail', album_id=album.id)
    else:
        form = AlbumForm(instance=album)
    # ...render the template with the form

def delete_album(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    if request.method == 'POST':
        album.delete()
        return redirect('photo_list')  # Redirect to a suitable page
    # ...render the template for confirmation