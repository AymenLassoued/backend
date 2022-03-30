from re import U
from rest_framework import serializers
from ListPieces.models import LIST_PIECES

class LISTSerializer(serializers.ModelSerializer):
    class Meta:
        model = LIST_PIECES
        fields = ('NumOF', 'Qte', 'Désignation', 'Matiére', 'Dimension', 'Qual',
        'Prévu_h', 'Réalisé_h', 'Conformité_C', 'Conformité_NC')