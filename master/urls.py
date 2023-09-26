from django.conf.urls import url
from django.urls import include, path
from master.views import *


urlpatterns = [
    path('v1/fetch-masslm',
         MASSlmApiView.as_view(), name='fetch-masslm')
]