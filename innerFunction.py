def outer_function():
    message = 'Hello, World!'
    def inner_function():
        print(message)
    
    return inner_function

# outer_function()
f = outer_function()
f()
f()