from abc import ABC, abstractmethod

class Car(metaclass=ABC):
    @abstractmethod
    def Drive(self):
        pass