import logging
import requests

from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import serializers

from amazon.models import Bsr, Marketplace
from amazon.utils import Region, Endpoint, Headers, Parameters
from core.utils import BaseSerializer
from config import Connectors

logger = logging.getLogger(__name__)


class BsrListSerializer(BaseSerializer):
    """Bsr serializer"""

    class Meta:
        model = Bsr
        fields = [
            "id",
            "marketplace",
            "asin",
            "amazon_category",
            "rank",
            "thumbnail_image",
            "rank_category",
            "offers_count",
            "updated_on",
            "created_on",
        ]


class BsrSerializer(BaseSerializer):
    """Bsr serializer"""

    marketplace = serializers.ChoiceField(
        choices=Connectors.get_choices(), required=True
    )
    region = serializers.ChoiceField(choices=Region.get_choices(), required=True)
    asin = serializers.CharField(required=True)

    class Meta:
        model = Bsr
        fields = [
            "id",
            "marketplace",
            "asin",
            "amazon_category",
            "rank",
            "region",
            "thumbnail_image",
            "rank_category",
            "offers_count",
        ]
        extra_kwargs = {
            "amazon_category": {"read_only": True},
            "rank": {"read_only": True},
            "thumbnail_image": {"read_only": True},
            "rank_category": {"read_only": True},
            "offers_count": {"read_only": True},
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
        bsr_url = f"https://sellercentral.amazon.{Endpoint.get_endpoint(region)}/rcpublic/productmatch"
        response = requests.get(
            bsr_url,
            params=Parameters.fetch_bsr(asin, region),
            headers=Headers.bsr_headers(region, marketplace.config),
        ).json()
        if self.validate_catalogue(asin, response) is None:
            return {}
        validated_data.update(**self.transform(self.validate_catalogue(asin, response)))
        validated_data["marketplace"] = marketplace
        self.perform_create(validated_data=validated_data, model=Bsr)
        validated_data["region"] = region
        return validated_data

    def transform(self, response):
        return {
            "amazon_category": response.get("gl"),
            "offers_count": response.get("offerCount"),
            "rank": response.get("salesRank"),
            "rank_category": response.get("salesRankContextName"),
            "thumbnail_image": response.get("thumbStringUrl"),
        }

    @staticmethod
    def validate_catalogue(asin, response):
        print(f"BSR Catalogue data : {response}")
        for i in range(len(response["data"]["otherProducts"]["products"])):
            if response["data"]["otherProducts"]["products"][i]["asin"] == asin:
                return response["data"]["otherProducts"]["products"][i]
        return None
