from base import Base 

from src.set_model import set_model_

class Engine(Base):
    def __init__(self):
        super().__init__(child=__class__.__name__)
        
    def set(self):
        super().set()
        
    def set_dataset(self):
        super().set_dataset()
        
    def set_model(self):
        super().set_model()
        
        set_model_()
        
        
if __name__ == '__main__':
    engine = Engine()
    
    engine.set_log()
    engine.set()
    engine.set_dataset() 
    engine.set_model()
    engine.test_log()
        
        