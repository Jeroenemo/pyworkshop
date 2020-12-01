# A Basic Function that accepts no arguments and returns nothing.
def hello_world():
    print("Hello, World!")


# A Function that accepts two arguments, and returns the value of
# those numbers added together.
def add_numbers(x, y):
    return x + y

# No default arguments
def say_greeting(greeting, name):
    print(f"{greeting}, {name}")

# Default argument - greeting will always be
# Hello, if one isn't provided.
def say_greeting_with_default(name, greeting="Hoi", punctuation="!"):
    print(f"{greeting}, {name}, {punctuation}")

# Don't do this!
def foo(a, b=[]):
    b.append(a)
    print(b)

    
# Do this instead.
def foo(a, b=None):
    if b is None:
        b = []
    b.append(a)
    print(b)