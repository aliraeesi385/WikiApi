import requests

class Jok4:
    def Jok4(Page:int=None):
        """
        `Page` Optional

        A rather funny joke in Persian.

        His exit is Json
        """
        if Page in None:
            return requests.get("https://open.wiki-api.ir/apis-1/4Jok").json()
        else:
            return requests.get("https://open.wiki-api.ir/apis-1/4Jok",{"page":Page}).json()