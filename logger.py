import logging
import coloredlogs
import logging.config
import json

def create_logger(name=None, config_json='logging.json'):
    with open(config_json, 'r') as f:
        config = json.load(f)

    # Set up the logger using the configuration
    logging.config.dictConfig(config)

    # Now, you can use the logger with colorful output
    logger = logging.getLogger(name)
    
    return logger 


if __name__ == '__main__':
    logger = create_logger()
    
    # Log messages
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")
