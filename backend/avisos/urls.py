from rest_framework.routers import DefaultRouter
from .views import AreaViewSet, PrioridadViewSet, EstadoViewSet

router = DefaultRouter()
router.register(r'areas', AreaViewSet, basename='areas')
router.register(r'prioridad', PrioridadViewSet, basename='prioridad')
router.register(r'estado', PrioridadViewSet, basename='estado')
urlpatterns = router.urls