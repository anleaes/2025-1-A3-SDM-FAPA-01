"""
URL configuration for museuapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movimentos/', include('movements.urls', namespace='movements')),
    path('artistas/', include('artists.urls', namespace='artists')), 
    path('enderecos/', include('addresses.urls', namespace='addresses')), 
    path('museus/', include('museums.urls', namespace='museums')),
    path('visitantes/', include('visitors.urls', namespace='visitors')),
    path('obras/', include('pieces.urls', namespace='pieces')),
    path('eventos/', include('events.urls', namespace='events')),
    path('pedidos/', include('orders.urls', namespace='orders')),
    path('itens_pedido/', include('orderitems.urls', namespace='orderitems')),
]
