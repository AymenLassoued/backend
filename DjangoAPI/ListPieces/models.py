from django.db import models

# Create your models here.
class LIST_PIECES(models.Model):
    RefOF = models.IntegerField(primary_key=True)
    NumOF = models.IntegerField()
    Qte = models.IntegerField()
    Designation = models.CharField(max_length=100)
    Matiere = models.CharField(max_length=100)
    Dimension = models.IntegerField()
    Qualification = models.CharField(max_length=100)
    Temps_Pre = models.IntegerField()
    Temps_Rea = models.IntegerField()
    TotalCNC_Pre = models.IntegerField()
    TotalCNC_Rea = models.IntegerField()
    TotalCONV_Pre = models.IntegerField()
    TotalCONV_Rea = models.IntegerField()
    Conformite_C = models.IntegerField()
    Conformite_NC = models.IntegerField()