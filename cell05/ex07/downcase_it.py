#!/usr/bin/env python3
import sys

def main():
    # Check if exactly one argument is provided
    if len(sys.argv) != 2:
        print("none")
    else:
        # Get the string argument and convert to lowercase
        input_string = sys.argv[1]
        print(input_string.lower())

if __name__ == "__main__":
    main()