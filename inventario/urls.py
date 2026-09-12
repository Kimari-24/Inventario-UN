from rest_framework.routers import DefaultRouter
from .views import (
    CategoriaViewSet, ProveedorViewSet, BodegaViewSet, DepartamentoViewSet,
    EmpleadoViewSet, ProductoViewSet, EntradaViewSet, SalidaViewSet
)

router = DefaultRouter()
router.register('categorias', CategoriaViewSet)
router.register('proveedores', ProveedorViewSet)
router.register('bodegas', BodegaViewSet)
router.register('departamentos', DepartamentoViewSet)
router.register('empleados', EmpleadoViewSet)
router.register('productos', ProductoViewSet)
router.register('entradas', EntradaViewSet)
router.register('salidas', SalidaViewSet)

urlpatterns = router.urls
