from abc import ABCMeta, abstractmethod

class MethodInterface(metaclass=ABCMeta):
    @abstractmethod
    def justDoit(self, controller):
        pass