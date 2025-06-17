import sys

def shrink(text):
    """
    Takes a string as a parameter and displays the first eight characters of that string.
    Uses slices to get the first 8 characters.
    """
    print(text[:8])

def enlarge(text):
    """
    Takes a string as a parameter and appends 'Z' characters to make it a total of eight characters.
    Then it displays the resulting string.
    Uses concatenation operator to add characters.
    """
    if len(text) < 8:
        
        enlarged = text + 'Z' * (8 - len(text))
        print(enlarged)
    else:
        
        print(text)

def main():
    
    if len(sys.argv) < 2:
        print("none")
        return
    
    
    for arg in sys.argv[1:]:
        if len(arg) > 8:
            
            shrink(arg)
        elif len(arg) < 8:
            
            enlarge(arg)
        else:
            
            print(arg)

if __name__ == "__main__":
    main()