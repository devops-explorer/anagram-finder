from abc import ABC, abstractmethod

class AnagramStrategy(ABC):
    @abstractmethod
    def generate(self, corpus):
        pass