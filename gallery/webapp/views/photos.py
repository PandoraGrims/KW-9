from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import PhotoForm
from webapp.models import Photo


class PhotoListView(ListView):
    model = Photo
    template_name = "photos/photo_list.html"
    context_object_name = "photos"
    paginate_by = 3
    ordering = ("-created_at",)

    def get_queryset(self):
        photos = super().get_queryset()
        if self.request.user.is_authenticated:
            photos = photos.filter(author=self.request.user)
        return photos


class PhotoCreateView(LoginRequiredMixin, CreateView):
    form_class = PhotoForm
    template_name = "photos/photo_create.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PhotoUpdateView(PermissionRequiredMixin, UpdateView):
    model = Photo
    form_class = PhotoForm
    template_name = "photos/photo_update.html"

    def has_permission(self):
        return self.request.user == self.get_object().author


class PhotoDeleteView(PermissionRequiredMixin, DeleteView):
    model = Photo
    template_name = "photos/photo_delete.html"

    def has_permission(self):
        return self.request.user == self.get_object().author

    def get_success_url(self):
        return reverse("accounts:profile", kwargs={"pk": self.request.user.pk})


class PhotoDetailView(DetailView):
    queryset = Photo.objects.all()
    template_name = "photos/photo_view.html"

#
# class LikePostView(LoginRequiredMixin, View):
#     def get(self, request, *args, pk, **kwargs):
#         post = get_object_or_404(Post, pk=pk)
#         if request.user in post.like_users.all():
#             post.like_users.remove(request.user)
#         else:
#             post.like_users.add(request.user)
#         return HttpResponseRedirect(self.request.GET.get("next"))
#
#
# class FollowersView(LoginRequiredMixin, View):
#     def get(self, request, *args, pk, **kwargs):
#         user = get_object_or_404(get_user_model(), pk=pk)
#         if user == request.user:
#             return HttpResponseBadRequest()
#         if request.user in user.followers.all():
#             user.followers.remove(request.user)
#         else:
#             user.followers.add(request.user)
#         return redirect("accounts:profile", pk=pk)
