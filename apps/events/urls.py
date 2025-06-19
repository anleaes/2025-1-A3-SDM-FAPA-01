from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'events'

router = routers.DefaultRouter()
router.register('', views.EventViewSet, basename='eventos')

urlpatterns = [
    path('', include(router.urls) )
]