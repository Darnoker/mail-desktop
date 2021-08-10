from abc import ABC, abstractmethod


class BaseController(ABC):
    @abstractmethod
    def __init__(self, viewHandler):
        self.viewHandler = viewHandler
        self.emailService = None
