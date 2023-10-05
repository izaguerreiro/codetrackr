import pytest

from http import HTTPStatus
from django.urls import reverse

from asset.models import Supplier


@pytest.mark.django_db
class TestSupplierViewSet:
    @pytest.fixture
    def supplier_data(self):
        return {
            "name": "Fake",
            "contact_name": "Fake Name",
            "email": "fake@mail.com",
        }

    def test_adding_an_supplier_with_success(self, client, supplier_data):
        response = client.post(reverse("supplier-list"), data=supplier_data)
        assert response.status_code == HTTPStatus.CREATED
        assert response.json()["name"] == supplier_data["name"]
        assert response.json()["contact_name"] == supplier_data["contact_name"]

    def test_list_suppliers_with_success(self, client, supplier):
        response = client.get(reverse("supplier-list"))
        assert response.status_code == HTTPStatus.OK
        assert str(response.json()["results"][0]["id"]) == str(supplier.id)

    def test_delete_suppliers_with_success(self, client, supplier):
        assert Supplier.objects.count() == 1
        response = client.delete(reverse("supplier-detail", kwargs={"pk": supplier.id}))
        assert response.status_code == HTTPStatus.NO_CONTENT
        assert Supplier.objects.count() == 0

    def test_edit_suppliers_with_success(self, client, supplier):
        assert supplier.name == "Fake"
        response = client.patch(
            reverse("supplier-detail", kwargs={"pk": supplier.id}),
            data={"name": "Changed Fake Name"},
        )
        assert response.status_code == HTTPStatus.OK
        assert response.json()["name"] == "Changed Fake Name"

    def test_get_supplier_when_supplier_doesnot_exists(self, client):
        response = client.delete(reverse("supplier-detail", kwargs={"pk": "123"}))
        assert response.status_code == HTTPStatus.NOT_FOUND
