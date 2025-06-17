import sys

def downcase_it(text):
    """
    Takes a string as an argument and returns the string in lowercase.
    """
    return text.lower()

def main():
    
    if len(sys.argv) > 1:
        
        for arg in sys.argv[1:]:
            result = downcase_it(arg)
            print(result)
    else:
        
        print("none")

if __name__ == "__main__":
    main()