import abc

from flask import Flask

class Router(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self, app: Flask):
        return

    @abc.abstractmethod
    def defineRoutes(self):
        return

