import requests

class SoundCloude:
    def SoundCloude(text:str):
        """
        `text` Require

        Searching for SoundCloude

        His exit is Json
        """
        return requests.get("https://open.wiki-api.ir/apis-1/SoundcloudeSearch",{"q":text}).json()