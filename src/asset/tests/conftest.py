import pytest
from datetime import datetime, timedelta
from decimal import Decimal
from rest_framework.test import APIClient

from asset.models import Asset, Supplier


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def supplier():
    return Supplier.objects.create(
        name="Fake",
        contact_name="Fake Name",
        email="fake@mail.com",
    )


@pytest.fixture
def asset(supplier):
    return Asset.objects.create(
        name="Fake",
        description="Fake description",
        version="1.0",
        supplier_id=supplier,
        expiration_date=datetime.now() + timedelta(days=1),
        serial_number="1738423fjkdfjsf",
        location="RH",
        responsible="Fake Responsible",
        cost=Decimal(10.00),
    )


@pytest.fixture
def asset_unused(supplier):
    return Asset.objects.create(
        name="Fake Unused",
        description="Fake description",
        version="1.0",
        supplier_id=supplier,
        expiration_date=datetime.now() + timedelta(days=1),
        serial_number="1738423fjkdfjsf",
        cost=Decimal(10.00),
    )


@pytest.fixture
def asset_expired(supplier):
    return Asset.objects.create(
        name="Fake Expired",
        description="Fake description",
        version="1.0",
        supplier_id=supplier,
        expiration_date=datetime.now() - timedelta(days=1),
        serial_number="1738423fjkdfjsf",
        location="RH",
        responsible="Fake Responsible",
        cost=Decimal(10.00),
    )
