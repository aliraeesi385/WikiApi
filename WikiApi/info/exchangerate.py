import requests

class ExchangeRate:
    def ExchangeRate(name:str=None):
        """
        `name` Optional

        Receiving the  exchange rate in Toman IR

        His exit is Json
        """
        gets= requests.get("https://open.wiki-api.ir/apis-1/ExchangeRate").json()
        if name == None:
            return gets
        else:
            listarz = {"usd": 0, "usd-hav": 1, "usd-ist": 2, "usd-herat": 3, "usd-sulaymaniyah": 4, "eur": 5, "eur-hav": 6, "eur-ist": 7, "try": 8, "gbp": 9, "aed": 10, "cad": 11, "cny": 12, "aud": 13, "myr": 14, "rub": 15, "iqd": 16, "sek": 17, "thb": 18, "amd": 19, "azn": 20, "gel": 21, "sar": 22, "inr": 23, "jpy": 24, "chf": 25, "afn": 26, "sgd": 27, "brl": 28, "dkk": 29, "kwd": 30, "nok": 31, "nzd": 32, "omr": 33, "pkr": 34, "ars": 35, "bhd": 36, "krw": 37, "syp": 38, "qar": 39, "hkd": 40, "kgs": 41, "tjs": 42, "tmt": 43}
            if listarz[name] in None:
                return gets['results'][listarz[name]]