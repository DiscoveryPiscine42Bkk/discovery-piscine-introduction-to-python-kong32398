def add_one(parameter):
    """
    Takes a parameter and adds 1 to the parameter passed to the method.
    This creates a local variable inside the function scope.
    """
    parameter = parameter + 1
    return parameter

def main():
    
    my_variable = 10
    
    
    print(f"Before calling add_one: {my_variable}")
    
    
    result = add_one(my_variable)
    print(f"Result from add_one: {result}")
    
    
    print(f"After calling add_one: {my_variable}")
    
    print("\nWhat do you observe?")
    print("The original variable 'my_variable' remains unchanged!")
    print("This demonstrates that the parameter in add_one() is a local variable.")
    print("Changes made inside the function don't affect the original variable.")
    print("This is because Python passes arguments by value for immutable types like integers.")

if __name__ == "__main__":
    main()