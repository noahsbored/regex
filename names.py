import re

def validate_names(names):
    
    pattern = r'^[A-Z][a-zA-Z]*\s(?:[A-Z][a-zA-Z]*\s?)*$'
    
    for name in names:
        if re.match(pattern, name):
            print(name)
        else:
            print("Invalid name")


names = ["Abraham Lincoln", "Andrew P Garfield", "peter pan", "Connor Milliken", "Jordan Alexander Williams", "Madonna", "programming is cool"]
validate_names(names)



