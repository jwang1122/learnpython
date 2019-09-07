import logging

logging.basicConfig(filename='C:/python/python_error.log', filemode='w+', level='DEBUG')
logger = logging.getLogger()

print(logger.level)
logger.info("Our first message...")
