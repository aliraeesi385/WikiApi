from .wikipedia import WikiPedia
from .digikala import DigiKala
from .ahangify import Ahangify
from .shazm import Shazm
from .soundcloude import SoundCloude
from .youtube import YouTube
from .mobile import Mobile

class Search(
    WikiPedia,
    DigiKala,
    Ahangify,
    Shazm,
    SoundCloude,
    YouTube,
    Mobile
):
    pass