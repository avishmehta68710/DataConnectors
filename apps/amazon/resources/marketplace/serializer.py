import re
import requests
import json

from django.utils import timezone
from rest_framework import serializers

from amazon.models.marketplace import Marketplace
from amazon.utils import (
    Region,
    Endpoint,
    Headers,
    Payloads,
    Parameters,
    InvAsin,
    StoreSlots
)
from config import Connectors


class MarketplaceSerializer(serializers.ModelSerializer):
    """Marketplace serializer"""

    name = serializers.ChoiceField(choices=Connectors.get_choices(), required=True)
    region = serializers.ChoiceField(choices=Region.get_choices(), required=True)
    config = serializers.ReadOnlyField()

    class Meta:
        model = Marketplace
        fields = ["name", "region", "config", "created_on", "updated_on"]

    @staticmethod
    def session_cookies(data):
        url = f"https://www.amazon.{Endpoint.get_endpoint(data['region'])}/portal-migration/hz/glow/address-change?actionSource=glow"
        response = requests.post(
            url,
            data=json.dumps(Payloads.location_change(data["region"])),
            headers=Headers.secret_headers(),
        )
        cookies = dict(response.cookies)
        cookies["location-session-id"] = cookies["session-id"]
        cookies.pop("session-id")
        return cookies

    @staticmethod
    def csrf_token(region):
        response = requests.get(
            f"https://www.amazon.{Endpoint.get_endpoint(region)}/stores/slot/{StoreSlots.get_store_slot(region)}",
            params=Parameters.store_secrets(region),
            headers=Headers.secret_headers(),
        )
        csrf_token = (
            re.search(r"amazonApiCsrfToken\":\"(.*?)\"", response.text).group(1)
        )
        session_id = (
            re.search(r"\"sessionId\":\"(.*?)\"", response.text).group(1)
        )
        return {"csrf-token": csrf_token, "session-id": session_id}

    @staticmethod
    def inv_token(data, session_cookies):
        region = data["region"]
        url = f"https://www.amazon.{Endpoint.get_endpoint(region)}/gp/product/ajax/ref={Parameters.inv_ref(region)}"
        response = requests.get(
            url,
            params=Parameters.fetch_inv(InvAsin.get_asin(data["region"])),
            headers=Headers.inv_token_headers(region, session_cookies["session-id"]),
        )
        cookies = dict(response.cookies)
        cookies.update({
            "inv-csrf-token": re.search(r'value="(1@.*?)"', response.text).group(1),
            "inv-session-id": cookies["session-id"],
        })
        return cookies

    def create(self, validated_data):
        csrf_token = self.csrf_token(validated_data["region"])
        inv_token = self.inv_token(validated_data, csrf_token)
        validated_data["config"] = {**csrf_token, **inv_token}
        self.perform_create(validated_data)
        return validated_data

    def perform_create(self, validated_data):
        Marketplace.objects.update_or_create(
            name=validated_data["name"],
            region=validated_data["region"],
            updated_on__date=timezone.now().date(),
            defaults={**validated_data},
        )
