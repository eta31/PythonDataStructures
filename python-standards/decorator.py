def checkName(func):
    def wrapper():
        print("What is your name?")
        func()
        print("Of course. It's you")

    return wrapper


@checkName
def printName():
    print("My name is Enkhtulga!")


printName()
