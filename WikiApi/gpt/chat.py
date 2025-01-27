import requests

class ChatGpt:
    def ChatGpt(Message:str):
        """
        `Message` Require

        it takes your question and is answered by ai.

        His exit is Json
        """
        return requests.get("https://open.wiki-api.ir/apis-1/ChatGPT",{"q":Message}).json()