def number():
        while True:
                try:
                        x = int(input("Please enter a number: "))
                        print("You entered a number: ", x)
                        break
                except ValueError:
                        print("Oops!, That was not a valid number. Try again please...")
