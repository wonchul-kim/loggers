from base import Base 

from src.set_model import set_model_

class Engine(Base):
    def __init__(self, name=None, config_json='logging.json'):
        super().__init__(name=name, config_json=config_json)
        
    def set(self):
        super().set()
        
    def set_dataset(self):
        super().set_dataset()
        
    def set_model(self):
        super().set_model()
        
        set_model_()
        
        
if __name__ == '__main__':
    engine = Engine(name="main")
    
    engine.set()
    engine.set_dataset() 
    engine.set_model()
        
        