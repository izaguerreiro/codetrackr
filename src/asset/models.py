import uuid

from django.db import models
from simple_history.models import HistoricalRecords

from .enums import AssetStatus, LicenceType, SupplierStatus


class BaseModel(models.Model):
    id = models.UUIDField(unique=True, default=uuid.uuid4, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)


class Supplier(BaseModel):
    name = models.CharField(max_length=255)
    contact_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=20, null=True)
    status = models.CharField(
        max_length=SupplierStatus.get_database_max_length(),
        choices=SupplierStatus.get_database_choices(),
        default=SupplierStatus.REVIEW,
    )
    history = HistoricalRecords()


class Asset(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    version = models.CharField(max_length=150)
    license_type = models.CharField(
        max_length=LicenceType.get_database_max_length(),
        choices=LicenceType.get_database_choices(),
        default=LicenceType.COMERCIAL,
    )
    supplier_id = models.ForeignKey(
        Supplier, on_delete=models.CASCADE, related_name="suppliers"
    )
    acquisition_date = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateTimeField()
    serial_number = models.CharField(max_length=255)
    location = models.CharField(max_length=100, null=True, blank=True)
    responsible = models.CharField(max_length=100, null=True, blank=True)
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(
        max_length=AssetStatus.get_database_max_length(),
        choices=AssetStatus.get_database_choices(),
        default=AssetStatus.ACTIVE,
    )
    history = HistoricalRecords()
