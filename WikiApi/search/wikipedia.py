import requests

class WikiPedia:
    def WikiPedia(text:str):
        """
        `text` Require

        Searching for Wikipedia

        His exit is Json
        """
        return requests.get("https://open.wiki-api.ir/apis-1/Wikipedia",{"q":text}).json()