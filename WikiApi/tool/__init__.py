from .createcaptcha import CreateCaptcha
from .googletranslate import GoogleTranslate

class Tool(
    GoogleTranslate,
    CreateCaptcha
):
    pass