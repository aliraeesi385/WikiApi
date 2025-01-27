import requests

class FreePik:
    def FreePik(link:str):
        """
        `link` Require

        Download from FreePik

        His exit is Json
        """
        return requests.get("https://open.wiki-api.ir/apis-1/FreePikDownloader",{"img":link}).json()