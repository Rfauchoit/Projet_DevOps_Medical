from abc import ABC, abstractmethod
class abstractController(ABC):
    
    @abstractmethod
    def create(self):
        pass
    
    
    @abstractmethod
    def treateCreate(self):
         pass
    
      
    @abstractmethod
    def update(self):
        pass
    
    # @abstractmethod
    # def treateUpdate():
    #     pass
    
    @abstractmethod
    def delete(self):
        pass
    
    # @abstractmethod
    # def treatDelete():
    #     pass
    
    @abstractmethod
    def read(self):
        pass
    # @abstractmethod
    # def treatRead():
    #     pass
    
    