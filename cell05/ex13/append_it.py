import sys

def main():
    
    args = sys.argv[1:]
    
    
    if len(args) == 0:
        print("none")
        return
    
    
    for arg in args:
        
        if arg.endswith('ism'):
            
            continue
        else:
            
            print(arg + 'ism')

if __name__ == "__main__":
    main()