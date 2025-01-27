import requests

class GoogleTranslate:
    def GoogleTranslate(to:str,text:str):
        """
        `to` Require
        `text` Require

        Google translator

        His exit is Json
        """
        return requests.get("https://open.wiki-api.ir/apis-1/GoogleTranslate",{"to":to,"text":text}).json()