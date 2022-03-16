from django.urls import path
from django.urls import URLPattern
from .views import artikelIndexView


urlpatterns = [
    path('', artikelIndexView, name = 'index')
]