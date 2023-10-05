import pytest

from django.urls import reverse

from asset.models import Asset


@pytest.mark.django_db
def test_get_assets_used_with_success(client, asset, asset_unused, asset_expired):
    assert Asset.objects.count() == 3
    response = client.get(reverse("assets-used"))
    assert len(response.json()) == 1


@pytest.mark.django_db
def test_get_assets_unused_with_success(client, asset, asset_unused, asset_expired):
    assert Asset.objects.count() == 3
    response = client.get(reverse("assets-unused"))
    assert len(response.json()) == 1


@pytest.mark.django_db
def test_get_assets_expired_with_success(client, asset, asset_unused, asset_expired):
    assert Asset.objects.count() == 3
    response = client.get(reverse("assets-expired"))
    assert len(response.json()) == 1
