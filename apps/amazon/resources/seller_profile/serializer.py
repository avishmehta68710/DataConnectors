import requests

from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import serializers

from amazon.models import SellerProfile, Marketplace
from amazon.utils import Region, Endpoint, Parameters, Headers
from core.utils import BaseSerializer
from config import Connectors


class SellerProfileListSerializer(BaseSerializer):
    class Meta:
        model = SellerProfile
        fields = [
            "id",
            "marketplace",
            "asin",
            "sold_by",
            "condition",
            "ships_from",
            "shipping_price",
            "shipping_currency",
            "created_on",
            "updated_on",
        ]


class SellerProfileSerializer(BaseSerializer):
    """Seller Profile serializer"""

    marketplace = serializers.ChoiceField(
        choices=Connectors.get_choices(), required=True
    )
    region = serializers.ChoiceField(choices=Region.get_choices(), required=True)
    asin = serializers.CharField(required=True)

    class Meta:
        model = SellerProfile
        fields = [
            "id",
            "marketplace",
            "asin",
            "sold_by",
            "condition",
            "ships_from",
            "shipping_price",
            "shipping_currency",
            "region",
        ]
        extra_kwargs = {
            "sold_by": {"read_only": True},
            "condition": {"read_only": True},
            "ships_from": {"read_only": True},
            "shipping_price": {"read_only": True},
            "shipping_currency": {"read_only": True},
        }

    def create(self, validated_data):
        region = validated_data.pop("region")
        asin = validated_data["asin"]
        url = f"https://sellercentral.amazon.{Endpoint.get_endpoint(region)}/rcpublic/getadditionalpronductinfo"
        response = requests.get(
            url,
            params=Parameters.fetch_sp(asin, region),
            headers=Headers.seller_central_headers(region, ),
        ).json()
        if response is None:
            return {}
        validated_data.update(**self.transform(response))
        validated_data["marketplace"] = get_object_or_404(
            Marketplace,
            name=validated_data["marketplace"],
            region=region,
            updated_on__date=timezone.now().date(),
        )
        self.perform_create(validated_data=validated_data, model=SellerProfile)
        validated_data["region"] = region
        return validated_data

    def transform(self, response):
        return {
            "sold_by": response.get("data", {}).get("soldBy"),
            "condition": response.get("data", {}).get("condition"),
            "ships_from": response.get("data", {}).get("shipsFrom"),
            "shipping_price": response.get("data", {})
            .get("shipping", {})
            .get("amount"),
            "shipping_currency": response.get("data", {})
            .get("shipping", {})
            .get("currency"),
        }

