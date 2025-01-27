import requests

class GeminiPro:
    def GeminiPro(Message:str):
        """
        `Message` Require

        it takes your question and is answered by ai GeminiPro.

        His exit is Json
        """
        return requests.get("https://open.wiki-api.ir/apis-1/GeminiPro",{"q":Message}).json()