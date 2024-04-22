from datetime import datetime

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Asset, Supplier
from .serializers import AssetSerializer, SupplierSerializer


class AssetModelViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all().order_by("name")
    serializer_class = AssetSerializer


class SupplierModelViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.order_by("name")
    serializer_class = SupplierSerializer


@api_view(["GET"])
def assets_expired(request):
    assets = Asset.objects.filter(expiration_date__lte=datetime.today())
    serializer = AssetSerializer(assets, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def assets_unused(request):
    assets = Asset.objects.filter(location=None, responsible=None)
    serializer = AssetSerializer(assets, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def assets_used(request):
    assets = Asset.objects.filter(expiration_date__gte=datetime.today()).exclude(
        location=None, responsible=None
    )
    serializer = AssetSerializer(assets, many=True)
    return Response(serializer.data)
