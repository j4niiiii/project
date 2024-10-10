from django.urls import path, include
from rest_framework import routers
from . import views, analytics_views

# Definir las rutas de la API
router = routers.DefaultRouter()
router.register(r'roles', views.RolViewSet)
router.register(r'usuarios', views.UsuarioViewSet)
router.register(r'metas', views.MetasViewSet)
router.register(r'categorias', views.CategoriaViewSet)
router.register(r'productos', views.ProductoViewSet)
router.register(r'ventas-unitarias', views.VentasUnitariasViewSet)
router.register(r'metas-cumplidas', views.MetasCumplidasViewSet)

# Definir las rutas de la API para KPIs y autenticación
urlpatterns = [
    path('', include(router.urls)),
    path('ventas-totales/', analytics_views.ventas_totales_view, name='ventas_totales'),
    path('autenticar/', views.autenticar, name='autenticar'),  # Asegúrate de que esta línea esté presente
]
