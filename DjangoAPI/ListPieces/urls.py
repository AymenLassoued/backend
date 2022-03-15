from django.urls import re_path as url
from ListPieces import views



urlpatterns=[
    url(r'^List_OF_Pieces$',views.ListPiecesApi),
    url(r'^List_OF_Pieces/([0-9]+)$',views.ListPiecesApi),

  
]