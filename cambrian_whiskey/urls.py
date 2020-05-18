"""cambrian_whiskey URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from accounts import urls as urls_accounts
# BELOW: FROM HOME ETC THIS HAS GIVEN BE ABSOLUTE GRIEF FOR 6 HRS. I COULD NOT OPEN MY APP BECAUSE OF SOMETHING TO DO WITH IN NAV.HTML AND THE URL LOGOUT 
# from home import urls as urls_accounts
from products import urls as urls_products
from cart import urls as urls_cart
from search import urls as urls_search
from checkout import urls as urls_checkout
from home import urls as urls_home
from products.views import all_products_view
from django.views import static
from .settings import MEDIA_ROOT

# If there is no name after the slash in the url we will just display the all_products

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # Homepage
    url(r'^$', all_products_view, name='index'),
    url(r'^home/', include(urls_home)),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^products/', include(urls_products)),
    url(r'^cart/', include(urls_cart)),
    url(r'^checkout/', include(urls_checkout)),
    url(r'^search/', include(urls_search)),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT}),

]
