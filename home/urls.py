from django.conf.urls import url, include
from .views import about, index

urlpatterns = [
  url(r'^about/$', about, name='about'),
  url(r'^$', index, name='index'),
]