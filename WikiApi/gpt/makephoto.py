import requests

class MakePhotoAi:
    def MakePhotoAi(q:str):
        """
        `q` Require

        it turns yout description into a photo.

        His exit is Json
        """
        return requests.get("https://open.wiki-api.ir/apis-1/MakePhotoAi",{"q":q}).json()