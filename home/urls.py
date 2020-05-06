from .views import about
from django.urls import path, re_path

urlpatterns = [
  path('about/', about, name='about'),
]