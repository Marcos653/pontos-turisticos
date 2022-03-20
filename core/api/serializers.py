from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from core.models import PontoTuristico
from atracoes.api.serializers import AtracaoSerializer
from enderecos.api.serializers import EnderecoSerializer

class PontoTuristicoSerializer(ModelSerializer):
    atracao = AtracaoSerializer(many=True)
    endereco = EnderecoSerializer()
    descricao_completa = serializers.SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao', 'aprovado', 'foto',
         'atracao', 'comentario', 'avaliacao', 'endereco',
         'descricao_completa' )


    def get_descricao_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao) 