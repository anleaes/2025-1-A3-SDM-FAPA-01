from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'museums'

router = routers.DefaultRouter()
router.register('', views.MuseumViewSet, basename='museus')

urlpatterns = [
    path('', include(router.urls) )
]