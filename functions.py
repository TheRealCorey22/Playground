from typing import Tuple


def getFirstLast() -> Tuple[str, str]:
    first_name = input("\nEnter First Name: ").strip()
    last_name = input("\nEnter Last Name: ").strip()
    return first_name, last_name
    

def getName() -> str:
    
    first_name, last_name = getFirstLast()
    full_name = first_name + " " + last_name
    return full_name


def greeting(name: str) -> None :
    
    try:
        
        if name.lower() == 'corey lazenby':
            print("\nMY MAN!!")
            
        else:
            print(f"\nWelcome, {name.title()}")


    except ValueError:
        print("\nInvalid! Try Again!")


greeting(getName())

