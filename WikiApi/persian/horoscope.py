import requests

class Horoscope:
    def Horoscope():
        """

        The fortune of the greatest and Best Iranian poet Hafiz

        His exit is Json
        """
        return requests.get("https://open.wiki-api.ir/apis-1/Horoscope").json()