from rest_framework.routers import DefaultRouter
from apps.products.api.views.general_views import *
from apps.products.api.views.product_viewsets import ProducViewSet

router = DefaultRouter()

router.register(r'products', ProducViewSet, basename='products')
router.register(r'measure-unit', MeasureUnitViewSet, basename='measure_unit')
router.register(r'category-product', CategoryProductViewSet, basename='category_product')
router.register(r'indicator', IndicatorViewSet, basename='indicator')

urlpatterns = router.urls