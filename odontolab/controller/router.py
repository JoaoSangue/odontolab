import abc

from flask import Flask

class Router(metaclass=abc.ABCMeta):
    _app: Flask

    @abc.abstractmethod
    def __init__(self, app: Flask) -> None:
        return

    @abc.abstractmethod
    def defineRoutes(self) -> None:
        return

