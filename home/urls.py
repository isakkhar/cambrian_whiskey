from .views import about, index
from django.urls import url

urlpatterns = [
  url(r'^about/$', about, name='about'),
  url(r'^$', index, name='index')
]