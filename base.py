from logger import create_logger

class Base:
    def __init__(self, name=None, config_json='logging.json'):
        self._logger = create_logger(name=name, config_json=config_json)
    
    def set(self):
        self._logger.info("set")
        
    def set_dataset(self):
        self._logger.info("set_dataset")
        
    def set_model(self):
        self._logger.info("set_model")
        

if __name__ == '__main__':
    base = Base()
    
    base.set()
    base.set_dataset()
    base.set_model()        
        