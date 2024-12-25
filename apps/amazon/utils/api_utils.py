import json

from amazon.utils import Localization, Region, PinCodes, Endpoint, RnrEnums, RnrEventTypes
from sp_api.base.marketplaces import Marketplaces as SpMarketplaces

API_HEADERS = {
    "accept": "text/html,*/*",
    "accept-language": "en-GB,en;q=0.9",
    "content-type": "application/json",
    "cache-control": "no-cache",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
}

AMAZON_INVENTORY_HEADERS = {
    "accept": 'application/vnd.com.amazon.api+json; type="cart.add-items/v1"',
    "content-type": 'application/vnd.com.amazon.api+json; type="cart.add-items.request/v1"',
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    "accept-language": "en-US",
}

AMAZON_DATA_API_HEADERS = {
    "accept": 'application/vnd.com.amazon.api+json; type="collection(product/v2)/v1"; expand="productImages(product.product-images/v2),title(product.offer.title/v1),buyingOptions[].price(product.price/v1),featureBullets(product.offer.feature-bullets/v1),buyingOptions[].dealDetails(product.deal-details/v1),buyingOptions[].availability(product.availability/v2),buyingOptions[].delivery(product.delivery/v1),customerReviewsSummary(product.customer-reviews-summary/v1),buyingOptions[].quantity(product.quantity/v2),buyingOptions[].promotionsUnified(product.promotions-unified/v1)"',
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Safari/605.1.15",
}


class Headers:
    @staticmethod
    def secret_headers():
        return API_HEADERS

    @staticmethod
    def inv_token_headers(region, session_id):
        headers = API_HEADERS
        headers["Cookie"] = (
            f"i18n-prefs={Localization.get_currency_code(region)}; session-id={session_id}"
        )
        return headers

    @staticmethod
    def inv_headers(region, config):
        headers = AMAZON_INVENTORY_HEADERS
        headers.update(
            {
                "origin": f"https://www.amazon.{Endpoint.get_endpoint(region)}",
                "referer": f"https://www.amazon.{Endpoint.get_endpoint(region)}/",
                "x-api-csrf-token": config["inv-csrf-token"],
                "cookie": f'session-id={config["inv-session-id"]};',
            }
        )
        return headers

    @staticmethod
    def rnr_headers(region, config):
        return {
            'accept': 'text/html,*/*',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'origin': f'https://www.amazon.{Endpoint.get_endpoint(region)}',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
            'cookie': f'{RnrEnums.get_secrets(region)}; session-id={config["session-id"]};'
        }

    @staticmethod
    def seller_central_headers(region):
        return {
            'accept': 'application/json',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': f'https://sellercentral.amazon.{Endpoint.get_endpoint(region)}/hz/fba/profitabilitycalculator/index?lang=en_US',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        }
    
    @staticmethod
    def bsr_headers(region, config):
        return {
            'accept': 'application/json',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'priority': 'u=1, i',
            'referer': f'https://sellercentral.amazon.{Endpoint.get_endpoint(region)}/hz/fba/profitabilitycalculator/index',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
             'cookie': f'session-id={config["session-id"]};'
        }

    @staticmethod
    def product_headers(region, config):
        headers = AMAZON_DATA_API_HEADERS
        headers.update(
            {
                "x-api-csrf-token": config["csrf-token"],
                "cookie": f"session-id={config['session-id']}",
                "accept-language": "en-US",
                "origin": f"https://www.amazon.{Endpoint.get_endpoint(region)}",
                "referer": f"https://www.amazon.{Endpoint.get_endpoint(region)}/",
                "x-cc-currency-of-preference": Localization.get_currency_code(region),
            }
        )
        return headers


class Payloads:
    @staticmethod
    def location_change(region):
        return {
            Region.AE: {
                "city": "Abu Dhabi",
                "deviceType": "web",
                "locationType": "PCD",
                "state": "Abu Dhabi",
                "district": "Abu-Dhabi Bus Station",
                "storeContext": "generic",
                "pageType": "Gateway",
                "actionSource": "glow",
            },
            Region.SA: {
                "locationType": "CITY",
                "city": "Dammam",
                "cityName": "الدمّام",
                "deviceType": "web",
                "storeContext": "generic",
                "pageType": "Gateway",
                "actionSource": "glow",
            },
            Region.EG: {
                "locationType": "CITY",
                "city": "Port Fouad",
                "cityName": "Port Said",
                "deviceType": "web",
                "storeContext": "generic",
                "pageType": "Gateway",
                "actionSource": "glow",
            },
            Region.NL: {
                "locationType": "COUNTRY",
                "district": "NL",
                "countryCode": "NL",
                "deviceType": "web",
                "storeContext": "generic",
                "pageType": "Gateway",
                "actionSource": "glow",
            },
            Region.AU: {
                "locationType": "POSTAL_CODE_WITH_CITY",
                "zipCode": "3000",
                "city": "MELBOURNE",
                "deviceType": "web",
                "storeContext": "generic",
                "pageType": "Gateway",
                "actionSource": "glow",
            }
        }.get(region, {
            "locationType": "LOCATION_INPUT",
            "zipCode": PinCodes.get_pin(region),
            "deviceType": "web",
            "pageType": "Detail",
            "actionSource": "glow",
        })

    @staticmethod
    def fetch_inv(asin):
        return json.dumps({"items": [{"asin": asin, "quantity": 9999, "additionalParameters": {}}]})

    @staticmethod
    def fetch_rnr(asin, star_rating, event_type):
        match event_type:
            case RnrEventTypes.CHILD_VERIFIED.value:
                review_text = f"pageNumber=1&pageSize=10&asin={asin}&reviewerType=avp_only_reviews"
            case RnrEventTypes.CHILD_TOTAL.value:
                review_text = f"pageNumber=1&pageSize=10&asin={asin}"
            case RnrEventTypes.PARENT_TOTAL.value:
                review_text = f"pageNumber=1&pageSize=10&asin={asin}&reviewerType=all_reviews"
            case RnrEventTypes.PARENT_VERIFIED.value:
                review_text = f"pageNumber=1&pageSize=10&asin={asin}&reviewerType=avp_only_reviews"
            case _:
                raise ValueError("Invalid event type")
        if star_rating == "total":
            return review_text
        return f"{review_text}&filterByStar={star_rating}"


class Parameters:
    @staticmethod
    def store_secrets(region):
        match region:
            case Region.US.value:
                return {
                    "pageId": "CA071EDA-0C04-4402-A063-7575C165AA1C",
                    "ingress": 0,
                    "visitId": "76a30665-c8dc-42b9-9576-8836543cf820",
                }
            case Region.IN.value:
                return {
                    "pageId": "66DA735C-F21A-44DA-A448-ABAA7E0B4467",
                    "ingress": 0,
                    "visitId": "77c6ffdd-207c-4033-9150-ed2dc48e7ac7",
                }
            case Region.AE.value:
                return {
                    "pageId": "C2B83E97-6B83-404F-90A5-832F275A2D62",
                    "ingress": 0,
                    "visitId": "bc39b2d3-5624-4442-aab9-4bdc495dc35d",
                }
            case Region.SA.value:
                return {
                    "pageId": "ECDFDA0B-FA83-4A09-9051-EBD08747E13A",
                    "ingress": 0,
                    "visitId": "69666497-b07b-4df9-844b-2f8d1cc488da",
                }
            case Region.BR.value:
                return {
                    "pageId": "618AB3AB-3846-4F46-92D2-8D77CFD573D8",
                    "ingress": 0,
                    "visitId": "6b4b1647-973a-48c8-9dc6-0c2aca0cf211"
                }
            case Region.NL.value:
                return {
                    "pageId": "1451F4F0-5E4E-45FF-A901-980A62770797",
                    "ingress": 0,
                    "visitId": "5500c42d-7ca4-4a8f-b602-e3f110ac22a9"
                }
            case Region.CA.value:
                return {
                    "pageId": "2DDC8FD6-0D0E-42C7-9D14-24EA2D37104E",
                    "ingress": 0,
                    "visitId": "6363b5c7-8032-4d70-90f7-da72aa2dfd50"
                }
            case Region.DE.value:
                return {
                    "pageId": "79444D34-2AE8-4E84-831E-EE95A1288F21",
                    "ingress": 0,
                    "visitId": "06afd506-ccf6-4224-9ff5-2d566f7e2671"
                }
            case Region.EG.value:
                return {
                    "pageId": "0F115B13-B448-45B0-9A6E-CD3A7059F0BE",
                    "ingress": 2,
                    "visitId": "d7d6087c-61e0-4421-a92a-79a6d2ea1a5e"
                }
            case Region.ES.value:
                return {
                    "pageId": "DD0DC23A-4D13-46E7-927C-5F6CAE6B3BE7",
                    "ingress": 2,
                    "visitId": "60bf0b51-7821-4ce0-b138-d5ae99d7f180"
                }
            case Region.FR.value:
                return {
                    "pageId": "AEF4ED30-8135-4774-AD0D-DFD60138A052",
                    "ingress": 0,
                    "visitId": "157e488f-fd2f-4eb4-9ced-f9b5749aa30f"
                }
            case Region.IT.value:
                return {
                    "pageId": "5CBD04A6-7442-4BEF-A8DE-8C47972B84DF",
                    "ingress": 0,
                    "visitId": "04c59d48-e239-4feb-ae02-333c755b7cb1"
                }
            case Region.JP.value:
                return {
                    "pageId": "1B564C8D-831F-407D-BC71-6CB6BFCA25E0",
                    "ingress": 0,
                    "visitId": "7e0fa8a2-8fc2-48ac-bde3-40aab3dff4cb"
                }
            case Region.TR.value:
                return {
                    "pageId": "110AA19D-10F2-4F3C-8FF8-FE504A471F26",
                    "ingress": 0,
                    "visitId": "032e695b-58e3-451c-b7c9-aef605147f34"
                }
            case Region.SG.value:
                return {
                    "pageId": "2A8EB9B5-1FE0-4B98-A8A5-061F567C9256",
                    "ingress": 0,
                    "visitId": "85bfd95a-a665-451f-9a8b-6da0b25e5893"
                }
            case Region.PL.value:
                return {
                    "pageId": "233BE892-02F6-4087-B1FE-147F983A0D49",
                    "ingress": 0,
                    "visitId": "fa54bcdb-f2cc-4fe5-b6cc-5fb8f8ffebd3"
                }
            case Region.MX.value:
                return {
                    "pageId": "79352E35-4387-459C-835A-2CC0A0E5AEF4",
                    "ingress": 0,
                    "visitId": "7186a04c-a49d-4aff-8917-288be00ac883"
                }
            case Region.UK.value:
                return {
                    "pageId": "A4B1401E-5FDA-4DC4-9A94-0A7DF880B60D",
                    "ingress": 0,
                    "visitId": "b564f67e-588e-46a1-a80a-9b5676da97b5"
                }
            case Region.AU.value:
                return {
                    "pageId": "D680BAA3-F936-4EF5-AC7C-5D4F8C32350F",
                    "ingress": 0,
                    "visitId": "a4b587ed-52f4-42cc-bfde-be699f3db885"
                }
            case Region.SE.value:
                return {
                    "pageId": "4135DBE6-E23F-43AC-B7D8-757721819DF7",
                    "ingress": 0,
                    "visitId": "88e44847-b8a3-480c-853d-5dc41c472d2a"
                }

    @staticmethod
    def inv_ref(region):
        if region == "IN":
            return "dp_aod_NEW_mbc"
        return "dp_aod_ALL_mbc"

    @staticmethod
    def fetch_inv(asin):
        return {"asin": asin, "pc": "dp", "experienceId": "aodAjaxMain"}

    @staticmethod
    def fetch_promotions(asin, region):
        return {
            "asin": asin,
            "locale": Localization.get_language_code(region),
            "marketplaceId": SpMarketplaces[region].marketplace_id,
        }

    @staticmethod
    def fetch_bsr(asin, region):
        return {
            "countryCode": region, "searchKey": asin, "locale": Localization.get_language_code(region),
        }

    @staticmethod
    def fetch_sp(asin, region):
        return {
            "countryCode": region,
            "asin": asin,
            "locale": Localization.get_language_code(region),
        }
