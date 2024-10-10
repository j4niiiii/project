from django.contrib import admin
from .models import Rol, Usuario, Metas, Categoria, Producto, VentasUnitarias, MetasCumplidas

# Register your models here.

admin.site.register(Rol)
admin.site.register(Usuario)
admin.site.register(Metas)
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(VentasUnitarias)
admin.site.register(MetasCumplidas)



