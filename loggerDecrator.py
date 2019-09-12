# from functools import wraps

def my_logger(original):
    import logging
    FORMAT = '[%(levelname)-8s] %(asctime)-15s %(clientip)s (%(name)s) %(message)s'
    logging.basicConfig(filename=f'{original.__name__}.log', level=logging.DEBUG, 
        format=FORMAT, datefmt='%m/%d/%Y %I:%M:%S %p')
    logger = logging.getLogger(original.__name__)
    d = {'clientip': 'Host Runner', 'user': 'jw'}
    
    # @wraps(original)
    def wrapper(*args, **kwargs):
        logger.info('Problem: %s', f'Run with args = {args}.', extra=d)
        return original(*args, **kwargs)

    return wrapper

def my_timer(original):
    import time

    # @wraps(original)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = original(*args, **kwargs)
        t2 = time.time() - t1
        print(f'{original.__name__} ran in {t2} seconds.')
        return result
    return wrapper

@my_timer
def display():
    import time
    time.sleep(1)
    print("display() is ran.")

# @my_timer
@my_logger
def display_info(name, age):
    # import time
    # time.sleep(1)
    print(f"display_info() run with arguments: ({name}, {age})")

display()
display_info("John", 23)