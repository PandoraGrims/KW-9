from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from api_v1.views import ApiViewSet, LikeViewSet, LogoutView

app_name = "api_v1"

router = DefaultRouter()
router.register("posts", ApiViewSet)
router.register('likes', LikeViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('login/', obtain_auth_token, name='api_token_auth'),
    path('logout/', LogoutView.as_view(), name='api_token_delete'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
