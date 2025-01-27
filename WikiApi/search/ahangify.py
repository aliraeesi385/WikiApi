import requests

class Ahangify:
    def Ahangify(text:str):
        """
        `text` Require

        Searching for Ahangify

        His exit is Json
        """
        return requests.get("https://open.wiki-api.ir/apis-1/SearchAhangify",{"q":text}).json()