from .freepik import FreePik
from .spotify import Spotify
from .soundcloud import SoundCloud

class Downloader(
    FreePik,
    Spotify,
    SoundCloud
):
    pass