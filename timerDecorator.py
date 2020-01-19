def my_timer(original):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = original(*args, **kwargs)
        t2 = time.time() - t1
        print(f'{original.__name__} ran in {t2:.3f} seconds.')
        return result
    return wrapper

@my_timer
def display_info(name, age):
    import time
    time.sleep(2) # simulate long process function
    print(f"display_info() run with arguments: ({name}, {age})")

display_info("John", 23)