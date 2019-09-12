def decrator(original):
    def wraper(*args, **kwargs):
        # new functionality added without changing display() function
        print('wrapper executed this before "{}()" is run.'
        .format(original.__name__)) 
        return original(*args, **kwargs)

    return wraper

@decrator
def display():
    print("display() is ran.")

@decrator
def display_info(name, age):
    print(f"display_info() run with arguments: ({name}, {age})")

display()
display_info("John", 23)

# decrator_display = decrator(display)
# print(decrator_display.__name__)
# decrator_display()  # this function call is exactly same as the following
# display()  