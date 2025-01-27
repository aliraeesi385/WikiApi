import requests

class Mobile:
    def Mobile(text:str):
        """
        `text` Require

        Searching Mobile

        His exit is Json
        """
        return requests.get("https://open.wiki-api.ir/apis-1/MobileSearch",{"q":text}).json()