import pytest

from datetime import datetime
from http import HTTPStatus
from django.urls import reverse

from asset.models import Asset


@pytest.mark.django_db
class TestAssetViewSet:
    @pytest.fixture
    def asset_data(self, supplier):
        return {
            "name": "Fake",
            "description": "Fake",
            "version": "1.0",
            "supplier_id": supplier.id,
            "acquisition_date": datetime.now(),
            "expiration_date": datetime.now(),
            "serial_number": "12345678900wdfghh",
            "location": "RH",
            "responsible": "Maria",
            "cost": 100.00,
        }

    def test_adding_an_asset_with_success(self, client, asset_data):
        response = client.post(reverse("asset-list"), data=asset_data)
        assert response.status_code == HTTPStatus.CREATED
        assert response.json()["name"] == asset_data["name"]
        assert response.json()["serial_number"] == asset_data["serial_number"]

    def test_list_assets_with_success(self, client, asset):
        response = client.get(reverse("asset-list"))
        assert response.status_code == HTTPStatus.OK
        assert str(response.json()["results"][0]["id"]) == str(asset.id)

    def test_delete_assets_with_success(self, client, asset):
        assert Asset.objects.count() == 1
        response = client.delete(reverse("asset-detail", kwargs={"pk": asset.id}))
        assert response.status_code == HTTPStatus.NO_CONTENT
        assert Asset.objects.count() == 0

    def test_edit_assets_with_success(self, client, asset):
        assert asset.name == "Fake"
        response = client.patch(
            reverse("asset-detail", kwargs={"pk": asset.id}),
            data={"name": "Changed Fake Name"},
        )
        assert response.status_code == HTTPStatus.OK
        assert response.json()["name"] == "Changed Fake Name"

    def test_get_asset_when_asset_doesnot_exists(self, client):
        response = client.delete(reverse("asset-detail", kwargs={"pk": "123"}))
        assert response.status_code == HTTPStatus.NOT_FOUND
