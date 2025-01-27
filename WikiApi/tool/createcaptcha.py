import requests

class CreateCaptcha:
    def CreateCaptcha():
        """


        Captcha making and receiving photos and code inside the photo

        His exit is Json
        """
        return requests.get("https://open.wiki-api.ir/apis-1/CreateCaptcha").json()