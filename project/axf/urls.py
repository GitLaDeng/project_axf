from django.conf.urls import url

from .views import *


urlpatterns = [
    url(r'^home/$',home_views,name='home'),
    url(r'^market/$',market_views,name='home'),
    url(r'^cart/$',cart_views,name='home'),
    url(r'^mine/$',mine_views,name='home'),

]
