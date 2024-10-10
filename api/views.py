from rest_framework import viewsets, status
from .models import Rol, Usuario, Metas, Categoria, Producto, VentasUnitarias, MetasCumplidas
from .serializer import (
    RolSerializer,
    UsuarioSerializer,
    MetasSerializer,
    CategoriaSerializer,
    ProductoSerializer,
    VentasUnitariasSerializer,
    MetasCumplidasSerializer
)
# api/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# --- CRUD ViewSets ---
class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class MetasViewSet(viewsets.ModelViewSet):
    queryset = Metas.objects.all()
    serializer_class = MetasSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class VentasUnitariasViewSet(viewsets.ModelViewSet):
    queryset = VentasUnitarias.objects.all()
    serializer_class = VentasUnitariasSerializer

class MetasCumplidasViewSet(viewsets.ModelViewSet):
    queryset = MetasCumplidas.objects.all()
    serializer_class = MetasCumplidasSerializer

@api_view(['POST'])
def autenticar(request):
    """
    Vista API para autenticar un usuario usando el correo y la contraseña sin cifrado.
    """
    email = request.data.get('email')
    password = request.data.get('password')

    if not email or not password:
        return Response({'error': 'Por favor, proporcione correo y contraseña.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = Usuario.objects.get(email=email)
        print(f"Usuario encontrado: {user.nombre} - Password en BD: {user.password}")

        # Comparación directa de contraseñas
        if password == user.password:  # Comparar directamente
            usuario_data = {
                'usuario_id': user.id_usuario,
                'nombre': user.nombre,
                'rol_id': user.id_rol.id_rol,
                'rol_puesto': user.id_rol.puestos,
                'rol_nombre': user.id_rol.roles,
            }
            return Response(usuario_data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Credenciales incorrectas.'}, status=status.HTTP_401_UNAUTHORIZED)
    except Usuario.DoesNotExist:
        return Response({'error': 'Usuario no encontrado.'}, status=status.HTTP_404_NOT_FOUND)
