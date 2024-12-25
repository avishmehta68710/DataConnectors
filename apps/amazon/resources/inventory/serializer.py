import logging
import re
import requests

from django.utils import timezone
from rest_framework import serializers
from rest_framework.generics import get_object_or_404
from sp_api.base.marketplaces import Marketplaces as SpMarketplaces

from amazon.models import Inventory, Marketplace
from amazon.utils import Region
from core.utils import BaseSerializer
from amazon.utils import Endpoint, Headers, Payloads
from config import Connectors

logger = logging.getLogger(__name__)


class InventoryListSerializer(BaseSerializer):
    class Meta:
        model = Inventory
        fields = [
            "id",
            "marketplace",
            "asin",
            "quantity",
            "is_qty_limit_set",
            "merchant_id",
            "url",
            "title",
            "updated_on",
            "created_on",
        ]


class InventorySerializer(BaseSerializer):
    marketplace = serializers.ChoiceField(
        choices=Connectors.get_choices(), required=True
    )
    region = serializers.ChoiceField(choices=Region.get_choices(), required=True)
    asin = serializers.CharField(required=True)

    class Meta:
        model = Inventory
        fields = [
            "id",
            "marketplace",
            "asin",
            "quantity",
            "is_qty_limit_set",
            "merchant_id",
            "url",
            "title",
            "region",
        ]
        extra_kwargs = {
            "quantity": {"read_only": True},
            "is_qty_limit_set": {"read_only": True},
            "merchant_id": {"read_only": True},
            "url": {"read_only": True},
            "title": {"read_only": True},
        }

    def create(self, validated_data):
        region = validated_data.pop("region")
        marketplace = get_object_or_404(
            Marketplace,
            name=validated_data["marketplace"],
            region=region,
            updated_on__date=timezone.now().date(),
        )

        url = f"https://data.amazon.{Endpoint.get_endpoint(region)}/api/marketplaces/{SpMarketplaces[region].marketplace_id}/cart/carts/retail/items?ref=aod_dpdsk_new_0&sr=&qid="
        response = requests.post(
            url,
            headers=Headers.inv_headers(region=region, config=marketplace.config),
            data=Payloads.fetch_inv(asin=validated_data["asin"]),
        )
        if response.status_code >= 500:
            logger.error(f"Amazon Inventory API error: {response.text}")
            return {}
        response = response.json()

        validated_data.update(**self.transform(response))
        validated_data["marketplace"] = marketplace
        self.perform_create(validated_data=validated_data, model=Inventory)
        validated_data["region"] = region
        return validated_data

    def transform(self, data):
        inv_data = data.get("entity", {}).get("items", [])[0]["responseMessage"]["detailed"]["fragments"]
        print(data)
        return {
            "quantity": data.get("entity", {}).get("items", [])[0].get("quantity"),
            "title": inv_data[1]["link"]["content"]["text"],
            "url": inv_data[1]["link"]["url"],
            "is_qty_limit_set": (
                True if "has a limit of" in inv_data[2]["text"] else False
            ),
            "merchant_id": re.search(r"smid=([^&]+)", inv_data[1]["link"]["url"]).group(
                1
            ),
        }
