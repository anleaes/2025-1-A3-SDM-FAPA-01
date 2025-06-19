from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'pieces'

router = routers.DefaultRouter()
router.register('', views.PieceViewSet, basename='obras')

urlpatterns = [
    path('', include(router.urls) )
]