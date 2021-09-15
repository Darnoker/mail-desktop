from abc import ABC, abstractmethod


# an abstract controller, that is used for other controllers, as a parent.
class BaseController(ABC):
    @abstractmethod
    def __init__(self, viewHandler, emailManager):
        self.viewHandler = viewHandler
        self.emailManager = emailManager
