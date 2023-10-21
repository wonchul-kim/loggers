from logger import Logger

class Base:
    def __init__(self, child=None):
        self._child = child
        self._logger = None
        
    def set_log(self, log_dir=None, \
                        log_stream_level="DEBUG", log_file_level="DEBUG"):
        
        if self._child != None:
            log_name = self._child 
        else:
            log_name = None
        self._logger = Logger(name=log_name, log_dir=log_dir, \
                                log_stream_level=log_stream_level, log_file_level=log_file_level)
    
    def set(self):
        self._logger.info("set")
        
    def set_dataset(self):
        self._logger.info("set_dataset")
        
    def set_model(self):
        self._logger.info("set_model")

    def test_log(self):        
        self._logger.debug("This is a debug message")
        self._logger.info("This is an info message")
        self._logger.warning("This is a warning message")
        self._logger.error("This is an error message")
        self._logger.critical("This is a critical message")

if __name__ == '__main__':

    log_stream_level = 'INFO'
    log_file_level = 'INFO'
    log_dir = None

    base = Base()
    base.set_log(log_stream_level=log_stream_level, log_file_level=log_file_level)

    base.set()
    base.set_dataset()
    base.set_model()   
    base.test_log()     

    def func(a, b, c=None):
        print(a, b)
        print(c)
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    
    base._logger.try_except_log(lambda: func(1), 'waht', post_action=lambda: func(1, 2))
    print("awelkfjawlkefjawlkjfawlkejfawlkejf")