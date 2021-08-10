from abc import ABC, abstractmethod


# an abstract controller, that is used for other controllers, as a parent.
class BaseController(ABC):
    @abstractmethod
    def __init__(self, viewHandler):
        self.viewHandler = viewHandler
        self.emailService = None
