from rest_framework.routers import DefaultRouter
from .views import AreaViewSet

router = DefaultRouter()
router.register(r'avisos', AreaViewSet, basename='avisos')
urlpatterns = router.urls