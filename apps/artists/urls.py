from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'artists'

router = routers.DefaultRouter()
router.register('', views.ArtistViewSet, basename='artistas')

urlpatterns = [
    path('', include(router.urls) )
]