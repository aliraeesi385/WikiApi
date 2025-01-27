import requests

class YouTube:
    def YouTube(text:str):
        """
        `text` Require

        Searching for YouTube

        His exit is Json
        """
        return requests.get("https://open.wiki-api.ir/apis-2/SearchYouTube",{"q":text}).json()