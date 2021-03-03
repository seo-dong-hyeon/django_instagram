from django.urls import path
from django.conf.urls import url, include
from .views import PhotoList, PhotoDelete, PhotoDetail, PhotoUpdate, PhotoCreate, PhotoLike, PhotoFavorite
from django.conf.urls.static import static
from django.conf import settings

import photo.api
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

app_name = "photo"

router = routers.DefaultRouter()
router.register('photos', photo.api.PhotoViewSet)

urlpatterns = [
    path("create/", PhotoCreate.as_view(), name='create'),
    path("delete/<int:pk>/", PhotoDelete.as_view(), name='delete'),
    path("update/<int:pk>/", PhotoUpdate.as_view(), name='update'),
    path("detail/<int:pk>/", PhotoDetail.as_view(), name='detail'),
    path("", PhotoList.as_view(), name='index'),
    path("like/<int:photo_id>/", PhotoLike.as_view(), name='like'),
    path("favorite/<int:photo_id>/", PhotoFavorite.as_view(), name='favorite'),
    url(r'^api/v1/', include((router.urls, 'photo'), namespace='api')),
    url(r'^api/doc', get_swagger_view(title='Rest API Document')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)