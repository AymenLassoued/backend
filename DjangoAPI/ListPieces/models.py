from django.db import models

# Create your models here.
class LIST_PIECES(models.Model):
    NumOF = models.IntegerField(primary_key=True)
    Qte = models.CharField(max_length=100)
    Désignation = models.CharField(max_length=100)
    Matiére = models.CharField(max_length=100)
    Dimension = models.CharField(max_length=100)
    Qual = models.CharField(max_length=100)
    Prévu_h = models.CharField(max_length=100)
    Réalisé_h = models.CharField(max_length=100)
    Conformité_C = models.CharField(max_length=100)
    Conformité_NC = models.CharField(max_length=100)
    # TotalCNC_Rea = models.CharField(max_length=100)
    # TotalCONV_Pre = models.IntegerField()
    # TotalCONV_Rea = models.IntegerField()
    # Conformite_C = models.IntegerField()
    # Conformite_NC = models.IntegerField()