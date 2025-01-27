from .TextToVoice import TextToVoice
from .gemini import GeminiPro
from .makephoto import MakePhotoAi
from .chat import ChatGpt

class Gpt(
    TextToVoice,
    GeminiPro,
    MakePhotoAi,
    ChatGpt
    ):
    """
    APIs taken from ai
    """
    pass