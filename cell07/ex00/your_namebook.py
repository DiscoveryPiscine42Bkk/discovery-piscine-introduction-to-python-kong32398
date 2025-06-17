def array_of_names(name_dict):
    """
    Takes a dictionary associating first names with last names as a parameter.
    It will build an array with the full names of the people, with the first letter capitalized.
    Returns this array.
    """
    full_names = []
    
    for first_name, last_name in name_dict.items():
        
        capitalized_first = first_name.capitalize()
        capitalized_last = last_name.capitalize()
        
        
        full_name = f"{capitalized_first} {capitalized_last}"
        full_names.append(full_name)
    
    return full_names

def main():
    
    persons = {
        "jean": "valjean",
        "grace": "hopper",
        "xavier": "niel",
        "fifi": "brindacier"
    }
    
    
    result = array_of_names(persons)
    print(result)

if __name__ == "__main__":
    main()