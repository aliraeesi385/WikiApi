import requests

class DigiKala:
    def DigiKala(text:str):
        """
        `text` Require

        Searching for DigiKala

        His exit is Json
        """
        return requests.get("https://open.wiki-api.ir/apis-1/SearchDigikala",{"q":text}).json()