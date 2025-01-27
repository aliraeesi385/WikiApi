import requests

class ReadyAnswer:
    def ReadyAnswer(Message:str):
        """
        `Message` Require

        He'll talk to you quickly to upset you.

        His exit is Json
        """
        return requests.get("https://open.wiki-api.ir/apis-1/ReadyAnswer",{"q":Message}).json()