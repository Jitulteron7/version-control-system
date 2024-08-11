from abc import ABC, abstractmethod

class BaseCommand(ABC):
    def __init__(self, flag:str, commitSHA:str):
        self.flag = flag 
        self.commitSHA = commitSHA
    
    @abstractmethod
    def execute(self):
        pass 
    
        
        