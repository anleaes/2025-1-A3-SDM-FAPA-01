from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'visitors'

router = routers.DefaultRouter()
router.register('', views.VisitorViewSet, basename='visitantes')

urlpatterns = [
    path('', include(router.urls) )
]