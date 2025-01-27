import requests

class Shazm:
    def Shazm(text:str):
        """
        `text` Require

        Searching for Shazm

        His exit is Json
        """
        return requests.get("https://open.wiki-api.ir/apis-2/SearchShazm",{"q":text}).json()