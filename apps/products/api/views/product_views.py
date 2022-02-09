from itertools import product
from apps.base.api import GeneralListAPIView
from apps.products.api.serializers.product_serializers import ProductSerializer


class ProductListAPIView(GeneralListAPIView):
    serializer_class = ProductSerializer