def greetings(name="noble stranger"):
    """
    Takes a name as a parameter and displays a welcome message with that name.
    If called without an argument, default parameter will be 'noble stranger'.
    If called with a non-string argument, displays an error message.
    """
    if not isinstance(name, str):
        print("Error! It was not a name.$")
    else:
        print(f"Hello, {name}.$")

def main():
    
    greetings('Alexandra')
    greetings('Wil')
    greetings()
    greetings(42)

if __name__ == "__main__":
    main()