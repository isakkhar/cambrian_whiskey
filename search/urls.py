from django.conf.urls import url
from .views import whiskey_search

# a app like this one, search, and others in the repository i.e cart, accounts... when filling in urls.py in there local app you then will have to add it to the main urls of the repository. In this case 'cambrian_whiskey'
urlpatterns = [

  url(r'^$', whiskey_search, name='search')

]
