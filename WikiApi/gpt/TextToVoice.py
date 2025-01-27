import requests

class TextToVoice:
    def TextToVoice(Text:str):
        """
        `Text` Require

        it turns your text into a voice message.

        His exit is Json
        """
        return requests.get("https://open.wiki-api.ir/apis-1/TextToVoice",{"text":Text}).json()