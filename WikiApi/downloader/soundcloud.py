import requests

class SoundCloud:
    def SoundCloud(link:str):
        """
        `link` Require

        Download from SoundCloud

        His exit is Json
        """
        return requests.get("https://open.wiki-api.ir/apis-2/SoundcloudDownloader",{"url":link}).json()