from django.urls import re_path as url
from followUP import views



urlpatterns=[
    url(r'^PO_followUP$',views.fabOrderApi),
    url(r'^PO_followUP/([0-9]+)$',views.fabOrderApi),

  
]