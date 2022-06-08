from rest_framework.routers import DefaultRouter
from apps.products.api.views.product_viewsets import ProducViewSet

router = DefaultRouter()

router.register(r'products', ProducViewSet, basename='products')

urlpatterns = router.urls