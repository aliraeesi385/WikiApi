from concurrent.futures.thread import ThreadPoolExecutor


class StopTransmission(Exception):
    pass


class StopPropagation(StopAsyncIteration):
    pass


class ContinuePropagation(StopAsyncIteration):
    pass

from .gpt import Gpt
from .downloader import Downloader
from .search import Search
from .info import Info
from .entertainment import Entertainment
from .tool import Tool

crypto_executor = ThreadPoolExecutor(1, thread_name_prefix="CryptoWorker")