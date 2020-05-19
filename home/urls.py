from django.conf.urls import url, include
from .views import about, index, contact

urlpatterns = [

  url(r'^about/$', about, name='about'),
  url(r'^$', index, name='index'),
  url(r'^contact/$', contact, name='contact'),

]