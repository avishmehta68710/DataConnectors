import json
import requests

from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import serializers
from sp_api.base.marketplaces import Marketplaces as SpMarketplaces

from amazon.models import Product, Marketplace
from amazon.utils import Region, Endpoint, Headers, Payloads
from core.utils import BaseSerializer
from config import Connectors


class ProductListSerializer(BaseSerializer):
    """Product serializer"""

    class Meta:
        model = Product
        fields = [
            "id",
            "marketplace",
            "asin",
            "max_order_quantity",
            "is_max_order_quantity_set",
            "availability",
            "availability_text",
            "mrp",
            "selling_price",
            "discount_percentage",
            "parent_five_star_rating_percentage",
            "parent_four_star_rating_percentage",
            "parent_three_star_rating_percentage",
            "parent_two_star_rating_percentage",
            "parent_one_star_rating_percentage",
            "deal_type",
            "deal_state",
            "deal_access_behaviour",
            "deal_early_access_duration_in_ms",
            "deal_percentage_claimed",
            "deal_start_time",
            "deal_end_time",
            "deal_id",
            "media_alt_text",
            "features",
            "updated_on",
            "created_on",
        ]


class ProductSerializer(BaseSerializer):
    """Product serializer"""

    marketplace = serializers.ChoiceField(
        choices=Connectors.get_choices(), required=True
    )
    region = serializers.ChoiceField(choices=Region.get_choices(), required=True)
    asin = serializers.CharField(required=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "marketplace",
            "asin",
            "region",
            "max_order_quantity",
            "is_max_order_quantity_set",
            "availability",
            "availability_text",
            "mrp",
            "selling_price",
            "discount_percentage",
            "parent_five_star_rating_percentage",
            "parent_four_star_rating_percentage",
            "parent_three_star_rating_percentage",
            "parent_two_star_rating_percentage",
            "parent_one_star_rating_percentage",
            "deal_type",
            "deal_state",
            "deal_access_behaviour",
            "deal_early_access_duration_in_ms",
            "deal_percentage_claimed",
            "deal_start_time",
            "deal_end_time",
            "deal_id",
            "media_alt_text",
            "features",
        ]
        extra_kwargs = {
            "max_order_quantity": {"read_only": True},
            "is_max_order_quantity_set": {"read_only": True},
            "availability": {"read_only": True},
            "availability_text": {"read_only": True},
            "mrp": {"read_only": True},
            "selling_price": {"read_only": True},
            "discount_percentage": {"read_only": True},
            "parent_five_star_rating_percentage": {"read_only": True},
            "parent_four_star_rating_percentage": {"read_only": True},
            "parent_three_star_rating_percentage": {"read_only": True},
            "parent_two_star_rating_percentage": {"read_only": True},
            "parent_one_star_rating_percentage": {"read_only": True},
            "deal_type": {"read_only": True},
            "deal_state": {"read_only": True},
            "deal_access_behaviour": {"read_only": True},
            "deal_early_access_duration_in_ms": {"read_only": True},
            "deal_percentage_claimed": {"read_only": True},
            "deal_start_time": {"read_only": True},
            "deal_end_time": {"read_only": True},
            "deal_id": {"read_only": True},
            "media_alt_text": {"read_only": True},
            "features": {"read_only": True},
            "deleted_on": {"read_only": True},
        }

    def create(self, validated_data):
        region = validated_data.pop("region")
        asin = validated_data["asin"]
        marketplace = get_object_or_404(
            Marketplace,
            name=validated_data["marketplace"],
            region=region,
            updated_on__date=timezone.now().date(),
        )
        url = f"https://data.amazon.{Endpoint.get_endpoint(region)}/api/marketplaces/{SpMarketplaces[region].marketplace_id}/products/{asin}"
        print(url)
        print(Headers.product_headers(region, marketplace.config))
        response = requests.get(
            url, headers=Headers.product_headers(region, marketplace.config)
        )
        print(response.text)
        response = response.json()
        validated_data.update(**self.transform(response))
        validated_data["marketplace"] = marketplace
        self.perform_create(validated_data=validated_data, model=Product)
        validated_data["region"] = region
        return validated_data

    @staticmethod
    def change_location(region):
        url = f"https://www.amazon.{Endpoint.get_endpoint(region)}/portal-migration/hz/glow/address-change?actionSource=glow"
        response = requests.post(
            url,
            data=json.dumps(Payloads.location_change(region)),
            headers=Headers.secret_headers(),
        )
        return dict(response.cookies)

    @staticmethod
    def current_location(region):
        url = f"https://www.amazon.{Endpoint.get_endpoint(region)}/portal-migration/hz/glow/get-location-label?storeContext=kitchen&pageType=Detail&actionSource=desktop-modal"
        response = requests.get(url, headers=Headers.secret_headers())
        return response.json()

    def transform(self, response):
        product = response["entities"][0]["entity"]
        return {
            "features": product["featureBullets"]
            .get("entity", {})
            .get("featureBullets"),
            "media_alt_text": product["productImages"].get("entity", {}).get("altText"),
            "deal_type": (
                product["buyingOptions"][0]
                .get("dealDetails", {})
                .get("entity", {})
                .get("type")
                if len(product["buyingOptions"]) > 0
                else None
            ),
            "deal_state": (
                product["buyingOptions"][0]
                .get("dealDetails", {})
                .get("entity", {})
                .get("state")
                if len(product["buyingOptions"]) > 0
                else None
            ),
            "deal_access_behaviour": (
                product["buyingOptions"][0]
                .get("dealDetails", {})
                .get("entity", {})
                .get("accessBehavior")
                if len(product["buyingOptions"]) > 0
                else None
            ),
            "deal_early_access_duration_in_ms": (
                product["buyingOptions"][0]
                .get("dealDetails", {})
                .get("entity", {})
                .get("earlyAccessDurationInMilliseconds")
                if len(product["buyingOptions"]) > 0
                else None
            ),
            "deal_percentage_claimed": (
                product["buyingOptions"][0]
                .get("dealDetails", {})
                .get("entity", {})
                .get("percentClaimed")
                if len(product["buyingOptions"]) > 0
                else None
            ),
            "deal_start_time": (
                product["buyingOptions"][0]
                .get("dealDetails", {})
                .get("entity", {})
                .get("startTime")
                if len(product["buyingOptions"]) > 0
                else None
            ),
            "deal_end_time": (
                product["buyingOptions"][0]
                .get("dealDetails", {})
                .get("entity", {})
                .get("endTime")
                if len(product["buyingOptions"]) > 0
                else None
            ),
            "deal_id": (
                product["buyingOptions"][0]
                .get("dealDetails", {})
                .get("entity", {})
                .get("id")
                if len(product["buyingOptions"]) > 0
                else None
            ),
            "mrp": (
                product["buyingOptions"][0]
                .get("price", {})
                .get("entity", {})
                .get("basisPrice", {})
                .get("moneyValueOrRange", {})
                .get("value", {})
                .get("amount")
                if len(product["buyingOptions"]) > 0
                else None
            ),
            "selling_price": (
                product["buyingOptions"][0]
                .get("price", {})
                .get("entity", {})
                .get("priceToPay", {})
                .get("moneyValueOrRange", {})
                .get("value", {})
                .get("amount")
                if len(product["buyingOptions"]) > 0
                else None
            ),
            "discount_percentage": (
                product["buyingOptions"][0]
                .get("price", {})
                .get("savings", {})
                .get("percentage", {})
                .get("value")
                if len(product["buyingOptions"]) > 0
                else None
            ),
            "parent_five_star_rating_percentage": product["customerReviewsSummary"]
            .get("entity", {})
            .get("histogram", {})
            .get("fiveStar", {})
            .get("percentage"),
            "parent_four_star_rating_percentage": product["customerReviewsSummary"]
            .get("entity", {})
            .get("histogram", {})
            .get("fourStar", {})
            .get("percentage"),
            "parent_three_star_rating_percentage": product["customerReviewsSummary"]
            .get("entity", {})
            .get("histogram", {})
            .get("threeStar", {})
            .get("percentage"),
            "parent_two_star_rating_percentage": product["customerReviewsSummary"]
            .get("entity", {})
            .get("histogram", {})
            .get("twoStar", {})
            .get("percentage"),
            "parent_one_star_rating_percentage": product["customerReviewsSummary"]
            .get("entity", {})
            .get("histogram", {})
            .get("oneStar", {})
            .get("percentage"),
            "max_order_quantity": (
                product["buyingOptions"][0]
                .get("quantity", {})
                .get("entity", {})
                .get("maxOrderQuantity")
                if len(product["buyingOptions"]) > 0
                else None
            ),
            "is_max_order_quantity_set": (
                product["buyingOptions"][0]
                .get("quantity", {})
                .get("entity", {})
                .get("isMaxQuantityRestricted")
                if len(product["buyingOptions"]) > 0
                else None
            ),
            "availability": (
                product["buyingOptions"][0]
                .get("availability", {})
                .get("entity", {})
                .get("type")
                if len(product["buyingOptions"]) > 0
                else None
            ),
            "availability_text": (
                product["buyingOptions"][0]
                .get("availability", {})
                .get("entity", {})
                .get("primaryMessage")
                if len(product["buyingOptions"]) > 0
                else None
            ),
        }
