from django.contrib import admin
from .models import Categoria, Proveedor, Bodega, Departamento, Empleado, Producto, Entrada, Salida

admin.site.register(Categoria)
admin.site.register(Proveedor)
admin.site.register(Bodega)
admin.site.register(Departamento)
admin.site.register(Empleado)
admin.site.register(Producto)
admin.site.register(Entrada)
admin.site.register(Salida)
