class decrator_class:
    def __init__(self, original):
        self.original = original
    
    def __call__(self, *args, **kwargs):
        print('call() executed this before "{}()" is run.'
        .format(self.original.__name__)) 
        return self.original(*args, **kwargs)

@decrator_class
def display():
    print("display() is ran.")

@decrator_class
def display_info(name, age):
    print(f"display_info() run with arguments: ({name}, {age})")

display()
display_info("John", 23)
