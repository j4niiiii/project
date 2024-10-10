from rest_framework import  serializers
from .models import Rol, Usuario, Metas, Categoria, Producto, VentasUnitarias, MetasCumplidas

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class MetasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metas
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class VentasUnitariasSerializer(serializers.ModelSerializer):
    class Meta:
        model = VentasUnitarias
        fields = '__all__'

class MetasCumplidasSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetasCumplidas
        fields = '__all__'