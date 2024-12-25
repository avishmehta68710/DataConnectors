from decimal import Decimal

import requests

from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import serializers
from sp_api.base.marketplaces import Marketplaces as SpMarketplaces

from amazon.models import Promotions, Marketplace
from amazon.utils import Region, RegionMap, Parameters
from core.utils import BaseSerializer
from config import Connectors


class PromotionsListSerializer(BaseSerializer):
    """Promotions serializer"""

    class Meta:
        model = Promotions
        fields = [
            "id",
            "marketplace",
            "asin",
            "brand",
            "deal_badge",
            "deal_text",
            "discount_percentage",
            "listing_image",
            "price",
            "prime_benefit_type",
            "prime_price",
            "promotion_type",
            "parent_rating",
            "parent_total_reviews",
            "title",
            "updated_on",
            "created_on",
        ]


class PromotionsSerializer(BaseSerializer):
    """Promotions serializer"""

    marketplace = serializers.ChoiceField(
        choices=Connectors.get_choices(), required=True
    )
    region = serializers.ChoiceField(choices=Region.get_choices(), required=True)
    asin = serializers.CharField(required=True)

    class Meta:
        model = Promotions
        fields = [
            "id",
            "marketplace",
            "asin",
            "brand",
            "deal_badge",
            "deal_text",
            "discount_percentage",
            "listing_image",
            "price",
            "prime_benefit_type",
            "prime_price",
            "promotion_type",
            "parent_rating",
            "parent_total_reviews",
            "title",
            "region",
        ]
        extra_kwargs = {
            "brand": {"read_only": True},
            "deal_badge": {"read_only": True},
            "deal_text": {"read_only": True},
            "discount_percentage": {"read_only": True},
            "listing_image": {"read_only": True},
            "price": {"read_only": True},
            "prime_benefit_type": {"read_only": True},
            "prime_price": {"read_only": True},
            "promotion_type": {"read_only": True},
            "parent_rating": {"read_only": True},
            "parent_total_reviews": {"read_only": True},
            "title": {"read_only": True},
        }

    def create(self, validated_data):
        region = validated_data.pop("region")
        url = f"https://{RegionMap.promotions_domain(SpMarketplaces[region].region)}/ajax/carousel/products"
        response = requests.get(
            url,
            params=Parameters.fetch_promotions(
                asin=validated_data["asin"], region=region
            ),
        ).json()
        validated_data.update(**self.transform(response[0]))
        validated_data["marketplace"] = get_object_or_404(
            Marketplace,
            name=validated_data["marketplace"],
            region=region,
            updated_on__date=timezone.now().date(),
        )
        self.perform_create(validated_data=validated_data, model=Promotions)
        validated_data["region"] = region
        return validated_data

    def transform(self, response):
        deal_badge, deal_text, prime_benefit_type = None, None, None
        if response.get("dealBadge") is not None:
            deal_badge = response["dealBadge"]["messageText"]
            deal_text = response["dealBadge"]["labelText"]
        if response.get("primeBenefitSaving") is not None:
            prime_benefit_type = response["primeBenefitSaving"].get("benefitType")
        return {
            "brand": response.get("brand"),
            "deal_badge": deal_badge,
            "deal_text": deal_text,
            "discount_percentage": response.get(
                "formattedSellerDiscountPercentage", "0"
            ),
            "listing_image": response.get("formattedImageUrl"),
            "price": response.get("formattedPriceV2"),
            "prime_benefit_type": prime_benefit_type,
            "prime_price": response.get("formattedPrimePrice"),
            "promotion_type": response.get("promotionType"),
            "parent_rating": Decimal(response.get("ratingValue", 0)),
            "parent_total_reviews": int(response.get("totalReviewCount", 0)),
            "title": response.get("title"),
        }

