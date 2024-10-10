from django.db import models

# Modelo de la tabla 'rol'
class Rol(models.Model):
    id_rol = models.IntegerField(primary_key=True)
    puestos = models.CharField(max_length=255)
    roles = models.CharField(max_length=255)
    permisos = models.CharField(max_length=255)

    class Meta:
        db_table = 'rol'
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'


# Modelo de la tabla 'usuarios'
class Usuario(models.Model):
    id_usuario = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    clave = models.CharField(max_length=50)  # Campo 'clave' agregado según la estructura SQL
    id_rol = models.ForeignKey(Rol, on_delete=models.CASCADE, db_column='id_rol')
    email = models.EmailField(max_length=255)
    sucursal = models.CharField(max_length=255)
    antiguedad = models.DateField()
    password = models.CharField(max_length=255)

    class Meta:
        db_table = 'usuarios'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'


# Modelo de la tabla 'categorias'
class Categoria(models.Model):
    id_categoria = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    stock = models.IntegerField()

    class Meta:
        db_table = 'categorias'
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'


# Modelo de la tabla 'productos'
class Producto(models.Model):
    id_producto = models.CharField(primary_key=True, max_length=50)
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, db_column='id_categoria')
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    precio = models.DecimalField(max_digits=10, decimal_places=2)  # Cambiado a 'precio' según el archivo SQL
    stock = models.IntegerField()

    class Meta:
        db_table = 'productos'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'


# Modelo de la tabla 'ventas_unitarias'
class VentasUnitarias(models.Model):
    id_unitaria = models.IntegerField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='id_usuario')
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE, db_column='id_producto')
    fecha = models.DateField()
    hora = models.TimeField()
    unidades_vendidas = models.IntegerField()
    total_venta = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'ventas_unitarias'
        verbose_name = 'Venta Unitaria'
        verbose_name_plural = 'Ventas Unitarias'


# Modelo de la tabla 'metas'
class Metas(models.Model):
    id_meta = models.IntegerField(primary_key=True)
    meta_ventas = models.IntegerField()
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()

    class Meta:
        db_table = 'metas'
        verbose_name = 'Meta'
        verbose_name_plural = 'Metas'


# Modelo de la tabla 'metas_cumplidas'
class MetasCumplidas(models.Model):
    id_total = models.AutoField(primary_key=True)
    id_meta = models.ForeignKey(Metas, on_delete=models.CASCADE, db_column='id_meta')
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='id_usuario')
    monto_meta = models.DecimalField(max_digits=10, decimal_places=2)
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    meta_cumplida = models.BooleanField()

    class Meta:
        db_table = 'metas_cumplidas'
        verbose_name = 'Meta Cumplida'
        verbose_name_plural = 'Metas Cumplidas'
