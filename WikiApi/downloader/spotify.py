import requests

class Spotify:
    def Spotify(link:str):
        """
        `link` Require

        Download from Spotify

        His exit is Json
        """
        return requests.get("https://open.wiki-api.ir/apis-2/DownloadSpotify",{"link":link}).json()