import sys

def main():
    
    if len(sys.argv) != 2:
        print("none")
        return
    
    
    input_string = sys.argv[1]
    
    
    z_count = 0
    for char in input_string:
        if char == 'z':
            z_count += 1
    
    
    if z_count == 0:
        print("none")
    else:
        
        for i in range(z_count):
            print("z")

if __name__ == "__main__":
    main()