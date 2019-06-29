from django.conf.urls import url

from .views import (searchposts)

urlpatterns = [
     url(r'^$', searchposts, name='searchposts'),

]
