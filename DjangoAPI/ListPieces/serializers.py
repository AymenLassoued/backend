from re import U
from rest_framework import serializers
from ListPieces.models import LIST_PIECES

class LISTSerializer(serializers.ModelSerializer):
    class Meta:
        model = LIST_PIECES
        fields = ('RefOF','NumOF', 'Qte', 'Designation', 'Matiere', 'Dimension', 'Qualification',
        'Temps_Pre', 'Temps_Rea', 'TotalCNC_Pre', 'TotalCNC_Rea', 'TotalCONV_Pre', 'TotalCONV_Rea'
        , 'Conformite_C', 'Conformite_NC')