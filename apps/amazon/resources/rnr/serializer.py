import re
import time

import requests
import logging

from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import serializers

from amazon.utils import Region, Endpoint, Headers, Payloads, RnrEnums, RnrEventTypes
from core.utils import BaseSerializer
from amazon.models import Rnr, Marketplace
from config import Connectors

logger = logging.getLogger(__name__)

MAX_RETRIES = 5
RETRY_DELAY = 2


class RnrListSerializer(BaseSerializer):
    class Meta:
        model = Rnr
        fields = [
            "id",
            "marketplace",
            "asin",
            "child_one_star_reviews_count",
            "child_one_star_rating_count",
            "child_two_star_reviews_count",
            "child_two_star_rating_count",
            "child_three_star_reviews_count",
            "child_three_star_rating_count",
            "child_four_star_reviews_count",
            "child_four_star_rating_count",
            "child_five_star_reviews_count",
            "child_five_star_rating_count",
            "child_total_rating",
            "child_total_reviews",
            "created_on",
            "updated_on",
        ]


class RnrSerializer(BaseSerializer):
    marketplace = serializers.ChoiceField(
        choices=Connectors.get_choices(), required=True
    )
    region = serializers.ChoiceField(choices=Region.get_choices(), required=True)
    asin = serializers.CharField(required=True)

    class Meta:
        model = Rnr
        fields = [
            "id",
            "marketplace",
            "asin",
            "child_one_star_reviews_count",
            "child_one_star_rating_count",
            "child_two_star_reviews_count",
            "child_two_star_rating_count",
            "child_three_star_reviews_count",
            "child_three_star_rating_count",
            "child_four_star_reviews_count",
            "child_four_star_rating_count",
            "child_five_star_reviews_count",
            "child_five_star_rating_count",
            "child_total_rating",
            "child_total_reviews",
            "parent_one_star_reviews_count",
            "parent_one_star_rating_count",
            "parent_two_star_reviews_count",
            "parent_two_star_rating_count",
            "parent_three_star_reviews_count",
            "parent_three_star_rating_count",
            "parent_four_star_reviews_count",
            "parent_four_star_rating_count",
            "parent_five_star_reviews_count",
            "parent_five_star_rating_count",
            "parent_total_rating",
            "parent_total_reviews",
            "child_verified_total_rating",
            "child_verified_total_reviews",
            "child_verified_one_star_reviews_count",
            "child_verified_one_star_rating_count",
            "child_verified_two_star_reviews_count",
            "child_verified_two_star_rating_count",
            "child_verified_three_star_reviews_count",
            "child_verified_three_star_rating_count",
            "child_verified_four_star_reviews_count",
            "child_verified_four_star_rating_count",
            "child_verified_five_star_reviews_count",
            "child_verified_five_star_rating_count",
            "parent_verified_total_rating",
            "parent_verified_total_reviews",
            "parent_verified_one_star_reviews_count",
            "parent_verified_one_star_rating_count",
            "parent_verified_two_star_reviews_count",
            "parent_verified_two_star_rating_count",
            "parent_verified_three_star_reviews_count",
            "parent_verified_three_star_rating_count",
            "parent_verified_four_star_reviews_count",
            "parent_verified_four_star_rating_count",
            "parent_verified_five_star_reviews_count",
            "parent_verified_five_star_rating_count",
            "region",
        ]
        extra_kwargs = {
            field: {"read_only": True} for field in [
                "id",
                "child_one_star_reviews_count",
                "child_one_star_rating_count",
                "child_two_star_reviews_count",
                "child_two_star_rating_count",
                "child_three_star_reviews_count",
                "child_three_star_rating_count",
                "child_four_star_reviews_count",
                "child_four_star_rating_count",
                "child_five_star_reviews_count",
                "child_five_star_rating_count",
                "child_total_rating",
                "child_total_reviews",
                "parent_one_star_reviews_count",
                "parent_one_star_rating_count",
                "parent_two_star_reviews_count",
                "parent_two_star_rating_count",
                "parent_three_star_reviews_count",
                "parent_three_star_rating_count",
                "parent_four_star_reviews_count",
                "parent_four_star_rating_count",
                "parent_five_star_reviews_count",
                "parent_five_star_rating_count",
                "parent_total_rating",
                "parent_total_reviews",
                "child_verified_total_rating",
                "child_verified_total_reviews",
                "child_verified_one_star_reviews_count",
                "child_verified_one_star_rating_count",
                "child_verified_two_star_reviews_count",
                "child_verified_two_star_rating_count",
                "child_verified_three_star_reviews_count",
                "child_verified_three_star_rating_count",
                "child_verified_four_star_reviews_count",
                "child_verified_four_star_rating_count",
                "child_verified_five_star_reviews_count",
                "child_verified_five_star_rating_count",
                "parent_verified_total_rating",
                "parent_verified_total_reviews",
                "parent_verified_one_star_reviews_count",
                "parent_verified_one_star_rating_count",
                "parent_verified_two_star_reviews_count",
                "parent_verified_two_star_rating_count",
                "parent_verified_three_star_reviews_count",
                "parent_verified_three_star_rating_count",
                "parent_verified_four_star_reviews_count",
                "parent_verified_four_star_rating_count",
                "parent_verified_five_star_reviews_count",
                "parent_verified_five_star_rating_count",
            ]
        }

    def create(self, validated_data):
        region = validated_data.pop("region")
        asin = validated_data["asin"]
        url = f"https://www.amazon.{Endpoint.get_endpoint(region)}/hz/reviews-render/ajax/reviews/get/"
        marketplace = get_object_or_404(
            Marketplace,
            name=validated_data["marketplace"],
            region=region,
            updated_on__date=timezone.now().date(),
        )
        for event in RnrEventTypes.get_list():
            for star in [
                "total",
                "five_star",
                "four_star",
                "three_star",
                "two_star",
                "one_star",
            ]:
                for attempt in range(MAX_RETRIES):
                    try:
                        response = requests.post(
                            url,
                            data=Payloads.fetch_rnr(asin, star, event),
                            headers=Headers.rnr_headers(region, marketplace.config),
                        ).text
                        if len(response) > 0:
                            break
                    except Exception:
                        time.sleep(RETRY_DELAY)
                else:
                    logger.error(f"All retry attempts failed for {star}.")
                    continue
                self.transform(response, validated_data, star, region, event)
        validated_data["marketplace"] = marketplace
        self.perform_create(validated_data=validated_data, model=Rnr)
        validated_data["region"] = region
        return validated_data

    def transform(self, response, validated_data, star, region, event_type):
        response = response.replace(",", "")
        rating_and_reviews_text = re.search(RnrEnums.get_regex(region=region), response)
        event_type = event_type.lower()
        try:
            rating_count = int(rating_and_reviews_text.group(1).replace(",", "").replace(' ', '').replace('.', ''))
            reviews_count = int(rating_and_reviews_text.group(2).replace(",", "").replace(' ', '').replace('.', ''))
            if star == "total":
                validated_data[f"{event_type}_total_rating"] = rating_count
                validated_data[f"{event_type}_total_reviews"] = reviews_count
            else:
                validated_data[f"{event_type}_{star}_rating_count"] = rating_count
                validated_data[f"{event_type}_{star}_reviews_count"] = reviews_count
        except:
            logger.error(f"Amazon RNR API error: {response}")
        return validated_data
