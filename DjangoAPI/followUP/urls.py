from django.urls import re_path as url
from followUP import views



urlpatterns=[
    url(r'^PO_followUP$',views.fabOrderApi),
    url(r'^api/tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),
    url(r'^api/tutorials$', views.tutorial_list),
    url(r'^PO_followUP/([0-9]+)$',views.fabOrderApi),
    url(r'update/([0-9]+)$', views.update_items),
]
