def find_the_redheads(family_dict):
    """
    This method takes a dictionary as a parameter, representing family members
    with their first name as the key and their hair color as the value.
    
    This method uses the filter function to gather the first names of the red-haired
    individuals into a new list, which it will return.
    """
    
    redheads = filter(lambda name: family_dict[name] == "red", family_dict.keys())
    
    
    return list(redheads)

def main():
    
    dupont_family = {
        "florian": "red",
        "marie": "blond",
        "virginie": "brunette",
        "david": "red",
        "franck": "red"
    }
    
    
    result = find_the_redheads(dupont_family)
    print(result)

if __name__ == "__main__":
    main()