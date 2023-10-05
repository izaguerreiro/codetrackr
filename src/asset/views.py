from rest_framework import viewsets

from .models import Asset, Supplier
from .serializers import AssetSerializer, SupplierSerializer


class AssetModelViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer


class SupplierModelViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
