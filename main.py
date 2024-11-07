# simple greeting program

def greet(name):
    "prints a personalized greeting"
    print(f"Hello, {name}!")
          
def main():
    """gets user's name and print greetings"""
    name = input("what's your name? ")
    greet(name)     

if __name__ == "__main__":
    main()