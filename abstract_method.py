from abc import ABC,abstractmethod
class computer(ABC):
    @abstractmethod
    def process(self):
         #print("running")
         pass
com =computer()
com.process()         