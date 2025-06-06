from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'movements'

router = routers.DefaultRouter()
router.register('', views.MovementViewSet, basename='movements')

urlpatterns = [
    path('', include(router.urls) )
]