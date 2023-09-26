from django.conf.urls import url
from django.urls import include, path
from crm.views import *


urlpatterns = [
    path('v1/fetch-crm-led',
         CrmApiView.as_view(), name='fetch-crm-led'),
    path('v1/fetch-forecast-amount',
         CrmOppApiView.as_view(), name='fetch-forecast-amount'),
]