from enum import Enum


class Region(Enum):
    US = "US"
    IN = "IN"
    CA = "CA"
    MX = "MX"
    BR = "BR"
    AU = "AU"
    JP = "JP"
    SG = "SG"
    AE = "AE"
    SA = "SA"
    TR = "TR"
    EG = "EG"
    PL = "PL"
    SE = "SE"
    IT = "IT"
    NL = "NL"
    ES = "ES"
    UK = "UK"
    FR = "FR"
    DE = "DE"

    @classmethod
    def get_choices(cls):
        return [(item.value, item.value) for item in cls]
    
    @classmethod
    def get_list(cls):
        return [item.value for item in cls]


class Endpoint:
    ENDPOINTS = {
        Region.US.value: "com",
        Region.IN.value: "in",
        Region.CA.value: "ca",
        Region.MX.value: "com.mx",
        Region.BR.value: "com.br",
        Region.AU.value: "com.au",
        Region.JP.value: "co.jp",
        Region.SG.value: "sg",
        Region.AE.value: "ae",
        Region.SA.value: "sa",
        Region.TR.value: "com.tr",
        Region.EG.value: "eg",
        Region.PL.value: "pl",
        Region.SE.value: "se",
        Region.IT.value: "it",
        Region.NL.value: "nl",
        Region.ES.value: "es",
        Region.UK.value: "co.uk",
        Region.FR.value: "fr",
        Region.DE.value: "de",
    }

    @staticmethod
    def get_endpoint(region):
        return Endpoint.ENDPOINTS.get(region)


class CurrencyCode(Enum):
    USD = "USD"
    INR = "INR"
    CAD = "CAD"
    MXN = "MXN"
    BRL = "BRL"
    EUR = "EUR"
    GBP = "GBP"
    SEK = "SEK"
    PLN = "PLN"
    EGP = "EGP"
    TRY = "TRY"
    SAR = "SAR"
    AED = "AED"
    AUD = "AUD"
    JPY = "JPY"
    SGD = "SGD"


class Localization:
    CURRENCY_CODES = {
        Region.US.value: CurrencyCode.USD,
        Region.IN.value: CurrencyCode.INR,
        Region.CA.value: CurrencyCode.CAD,
        Region.MX.value: CurrencyCode.MXN,
        Region.BR.value: CurrencyCode.BRL,
        Region.ES.value: CurrencyCode.EUR,
        Region.UK.value: CurrencyCode.GBP,
        Region.FR.value: CurrencyCode.EUR,
        Region.NL.value: CurrencyCode.EUR,
        Region.DE.value: CurrencyCode.EUR,
        Region.IT.value: CurrencyCode.EUR,
        Region.SE.value: CurrencyCode.SEK,
        Region.PL.value: CurrencyCode.PLN,
        Region.EG.value: CurrencyCode.EGP,
        Region.TR.value: CurrencyCode.TRY,
        Region.SA.value: CurrencyCode.SAR,
        Region.AE.value: CurrencyCode.AED,
        Region.SG.value: CurrencyCode.SGD,
        Region.AU.value: CurrencyCode.AUD,
        Region.JP.value: CurrencyCode.JPY,
    }

    LANGUAGE_CODES = {
        Region.US.value: "en-US",
        Region.IN.value: "en-IN",
        Region.CA.value: "en-CA",
        Region.MX.value: "en-MX",
        Region.BR.value: "en-BR",
        Region.AU.value: "en-AU",
        Region.JP.value: "en-JP",
        Region.SG.value: "en-SG",
        Region.AE.value: "en-AE",
        Region.SA.value: "en-SA",
        Region.TR.value: "en-TR",
        Region.EG.value: "ar-EG",
        Region.PL.value: "en-PL",
        Region.SE.value: "en-SE",
        Region.IT.value: "en-IT",
        Region.NL.value: "en-NL",
        Region.ES.value: "en-ES",
        Region.UK.value: "en-GB",
        Region.FR.value: "en-FR",
        Region.DE.value: "en-DE",
    }

    @staticmethod
    def get_currency_code(region):
        return Localization.CURRENCY_CODES.get(region).value

    @staticmethod
    def get_language_code(region):
        return Localization.LANGUAGE_CODES.get(region)


class InvAsin:
    ASIN = {
        Region.US.value: "B0BHSXFTGH",
        Region.IN.value: "B01BVDS1BE",
        Region.CA.value: "B0962Y8BZ5",
        Region.MX.value: "B08XXGD5MP",
        Region.BR.value: "B0DHNFCLWK",
        Region.AU.value: "B0CYP88LLX",
        Region.JP.value: "B0CV4S2W32",
        Region.SG.value: "B0BLTMD8L8",
        Region.AE.value: "B0B41NL1JC",
        Region.SA.value: "B0B41NL1JC",
        Region.TR.value: "B07TLVN8TP",
        Region.EG.value: "B0B41NL1JC",
        Region.PL.value: "B07XJ8C8F5",
        Region.SE.value: "B0C84P2JBG",
        Region.IT.value: "B0D4QW13R1",
        Region.NL.value: "B0BHSXFTGH",
        Region.ES.value: "B0764HS4SL",
        Region.UK.value: "B0D9Q1S8FP",
        Region.FR.value: "B0764HS4SL",
        Region.DE.value: "B0764HS4SL",
    }

    @staticmethod
    def get_asin(region):
        return InvAsin.ASIN.get(region)


class PinCodes:
    PINS = {
        Region.US.value: "10115",
        Region.IN.value: "560034",
        Region.CA.value: "K1A 0A0",
        Region.MX.value: "50310",
        Region.BR.value: "27460-000",
        Region.JP.value: "028-8392",
        Region.SG.value: "118547",
        Region.TR.value: "34000",
        Region.PL.value: "50-001",
        Region.IT.value: "20100",
        Region.ES.value: "35530",
        Region.UK.value: "SW1W 0NY",
        Region.FR.value: "78000",
        Region.DE.value: "10115",
    }

    @staticmethod
    def get_pin(region):
        return PinCodes.PINS.get(region)


class RegionMap(Enum):
    West = "WEST"
    Central = "CENTRAL"
    East = "EAST"

    @staticmethod
    def promotions_domain(region):
        return {
            "us-east-1": "d2in0p32vp1pij.cloudfront.net",
            "eu-west-1": "d3sbedvipl8ovw.cloudfront.net",
        }.get(region, "d3sbedvipl8ovw.cloudfront.net")


class RnrEnums:
    REGEX = {
        Region.MX.value: r"(\d+)\s+calificaciones\s+totale[s]\s+(\d+)\s+con\s+opini[ones|ón[s]]?",
        Region.BR.value: r"(\d+)\s+classificaçõe[s]\s+no\s+total[s]\s+(\d+)\s+com\s+avaliaçõe[s]?",
        Region.SE.value: r"(\d+)\s+totalt\s+betyg\s+(\d+)\s+med recensioner?",
        Region.PL.value: r"Łącznie ocen: (\d+(?:[\s.,]\d+)*), (\d+(?:[\s.,]\d+)*) z ocenami?",
        Region.TR.value: r"(\d{1,3}(?:,\d{3})*) toplam puan, (\d{1,3}(?:,\d{3})*) yorumlu?",
        Region.IT.value: r"(\d{1,3}(?:,\d{3})*) valutazioni totali, (\d{1,3}(?:,\d{3})*) con recensioni?",
        Region.FR.value: r"(\d{1,3}(?:,\d{3})*) évaluation[s]? au total, (\d{1,3}(?:,\d{3})*) avec avis?",
        Region.ES.value: r"(\d{1,3}(?:,\d{3})*) valoraciones totales, (\d{1,3}(?:,\d{3})*) con reseñas?",
        Region.NL.value: r"(\d{1,3}(?:,\d{3})*) beoordelingen in totaal, (\d{1,3}(?:,\d{3})*) met recensies?",
        Region.DE.value: r"(\d+(?:\.\d+)?) Gesamtbewertungen, (\d+(?:\.\d+)?) mit Rezensionen?",
        Region.JP.value: r"(\d+(?:\.\d+)?)件の合計評価、レビュー付き:(\d+(?:\.\d+)?)?",
        "default": r"(\d+)\s+total\s+rating[s]\s+(\d+)\s+with\s+review[s]?"
    }
    
    SECRETS = {
        Region.US.value: 'x-main="JDN@9veLo?es0ZwmyEyk?MjthPY4hlyKtub6DUD185@2OqMqdKCDILFrVEPs3eEl"; ',
        Region.IN.value: 'x-acbin="n8F@6FLeD?TjDZ3?36T3eDZA2eVO5uzE8BCQQdRCYxCnY4IixWLa1oEzbvLRzU4q"; ',
        Region.CA.value: 'x-acbca="y7mfCnl3DM4VJWQQfQuRD?k4e5pRCs7NEX6NrFR43WwJgKJSekgji0YUzyVKOyqk"; ',
        Region.MX.value: 'x-acbmx="4u53THvzkk@iwyiasIkQJ5J61sSuJGpFoklYKw4KgoJ7xUV1aQ9MVQ3rA5cmyq3d"; ',
        Region.FR.value: 'x-acbfr="ItozgK7fPil1J@oVtJFV5D?ZksosDVrKuZOX@uA0@xsS?gXCara7nGcs5DbXQP4E"; ',
        Region.BR.value: 'x-acbbr="JljiNBk8h27gFBbMQ?noWuxIoXztcaYcuCjmFMNWFplH373ZH1HN9U8GW5SnXD3d"; ',
        Region.SE.value: 'x-acbse="H@iaMdWV4XZzuKMpN0poJqTw5C2t3kTgvhXRIEvKUilWkH47?96rL2nRipTSG8Id"; ',
        Region.UK.value: 'x-acbuk="cJC1TYTdmpc7iixv0uNxfupsSDpKFkKnMW?u38QvQnLbfBRZsYDx?8dyanKNE@7a"; ',
        Region.NL.value: 'x-acbnl="iBc4Kc9CHpH3V4eKTkpSwdUzT6sEhNBsJTpeDa94jnlFYoPMRSSEG?vOqMHaTcYz"; ',
        Region.EG.value: 'x-acbeg="n3Ksv6gOOzRTqtMt3MyNLbPXimqf4DNUoal2gFPcokSeC?2LjHxD5laHUOCbQd2Y"; ',
        Region.DE.value: 'x-acbde=uqsO4eF7mqvnkpCn5pDzM5ffSZwx3rzKze99SBqAhNOkXDkqQRD2UfDW3gXkDQzf; ',
        Region.SA.value: 'x-acbsa="YL2T7JdML3vmql?dkpbDNaaZyAsghbzlrbohLD2XpEsMjmcHfyI6xgO4EYVeSfgr"; ',
        Region.AE.value: 'x-acbae="FhsvPiXWd?6PjblOICTmLl4diL?X3JfOSlQ1K4Jy4p8vw8te9QfEluKHjVjy2QA1"; ',
        Region.AU.value: 'x-acbau=hFAyQpqYvLwDZ5rLGYI6oULfenG8ZNDL4c0ko2ufrGJsxWvswtv9BZFyvNyJOgBf; ',
        Region.SG.value: 'x-acbsg="FYSHe?X6Az0RmTVOnfII?Z2y0KHnnEFfJ1dxC7eqobx@gYgCNRI7kgCgvCkX?JWJ"; ',
        Region.ES.value: 'x-acbes="42J9HXYf8W91mYLooSdSxtvMSR@ksw8qE3lbS6gzApP1rAgRPj8edT727u4unyL7"; ',
        Region.IT.value: 'x-acbit="XVHx0E5pjUpnGY4DsRqrtgyJWJhPfLXjneUcWwFEnc4qkfUTXMmQWUTd6d@HSDY4"; ',
        Region.PL.value: 'x-acbpl="7bcktxxxn0YZz6?0FSjArWVSX@S4gUUrSw7gSaSY4R6fLnSACsVuRGeE5PRoZ52h"; ',
        Region.TR.value: 'x-acbtr="s3jVlS?ocRJc7J4Z9JwcLhhGRH5e0PTLWvRpMCKEaWLTDAODBbR7IpSZkPeCOZfH"; ',
        Region.JP.value: 'x-acbjp="rh3H2lxJfQH5dCAuOnwngz9XdzG3AaIq6INtWRWTPxRT2fxnU?7mFoKExDRblrOF"; '
    }
    
    @staticmethod
    def get_secrets(region):
        return RnrEnums.SECRETS.get(region)
    
    @staticmethod
    def get_regex(region):
        return RnrEnums.REGEX.get(region, RnrEnums.REGEX["default"])


class RnrEventTypes(Enum):
    CHILD_VERIFIED = "CHILD_VERIFIED"
    CHILD_TOTAL = "CHILD"
    PARENT_VERIFIED = "PARENT_VERIFIED"
    PARENT_TOTAL = "PARENT"
    
    @staticmethod
    def get_choices():
        return [(item.value, item.value) for item in RnrEventTypes]
    
    @staticmethod
    def get_list():
        return [item.value for item in RnrEventTypes]


class StoreSlots:
    STORE_SLOT_ID = {
        Region.IN.value: "suev4aowpn",
        Region.US.value: "Ekvezgnqe3",
        Region.AE.value: "r4mnwtxmar",
        Region.SA.value: "Ei5rbxiapo",
        Region.BR.value: "k296yq02me",
        Region.NL.value: "Yqaz1e85vx",
        Region.CA.value: "Lay5kt6ep0",
        Region.DE.value: "Z15rqo60wn",
        Region.EG.value: "jgzad8ymvo",
        Region.ES.value: "nh6z0quxok",
        Region.FR.value: "4t6ezq5239",
        Region.IT.value: "kr6hf0avqc",
        Region.JP.value: "Lgjs7uld73",
        Region.TR.value: "uqj8s9p542",
        Region.SG.value: "4mtmy9rg5b",
        Region.PL.value: "Pwmsksitr6",
        Region.MX.value: "opz85rualy",
        Region.UK.value: "G3txbtnqvi",
        Region.AU.value: "k19n70z6h8",
        Region.SE.value: "clotjvl7pd"
    }
    
    @staticmethod
    def get_store_slot(region):
        return StoreSlots.STORE_SLOT_ID[region]
