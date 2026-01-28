#!/usr/bin/env python3
import random

def main():
    print("\n" + " Fashion bot 9000".center(50))

    name = input("What is your first name? ").title().strip()
    
    try:
        age_input = input("How old are you? ")
        age = int(age_input)
    except ValueError:
        age = 0 
        # Not using age currently, but keeping the input to match original flow

    # Hat
    hat = input("Do you wear hats? ").lower().strip()
    hat_type = None

    if hat == "yes":
        hat_type = input(f"So, {name} What type of hats do you wear? ").lower().strip()
        if hat_type == "beanie":
            print("Beanies Are Great For The Cold")
        elif hat_type == "baseball hat":
            print("Baseball Hats Are My Favorite!")
        else:
            print("Not My First Choice But Its Still Good")
    elif hat == "no":
        print("That's Okay")
    else:
        # Default fallback if they say something else
        pass

    # Top
    top = input(f"So, {name} What Is Your Favorite Top? ").strip()
    top_response = random.choice(["That's a good choice.", "Ayy that’s lit.", "I like where this is going."])
    
    if top == "":
        print("Beach Day?")
    else:
        print(top_response)

    # Bottom
    bottom = input("What about your choice of bottom? ").lower().strip()
    if bottom == "cargo pants":
        print("I Also Like Cargo Pants.")
    elif bottom == "sweatpants":
        print("Sweatpants Are My Favorite!")
    elif bottom == "swimsuit":
        print("Beach Day!!!")
    elif bottom == "":
        print("Weird")
    else:
        print(f"You Can’t Go Wrong With {bottom}.")
    
    # Shoes
    shoes = input("What shoes do you like? ").lower().strip()
    if shoes == "adidas":
        print("I Love Adidas!")

    # Final Fit Output
    print("\n" + f"Final Outfit For: {name}".center(50))
    
    if hat == "yes" and hat_type:
        print(hat_type.title().center(50))
    else:
        print("No Hat".center(50))
    
    if top.lower() in ["", "none"]:
        print("No Top".center(50))
    else:
        print(top.title().center(50))

    if bottom.lower() in ["", "none"]:
        print("No Bottoms, Weirdo".center(50))
    else:
        print(bottom.title().center(50))
    
    if shoes.lower() in ["", "none"]:
        print("Barefoot".center(50))
    else:
        print(shoes.title().center(50))

    # Response Verdict
    verdict = random.choice(["Looking Good!", "Fire Fit!", "Looks Good"])
    if top == "" and bottom == "":
        print("Go Put Some Clothes On!!".center(50))
    elif top == "" and bottom == "swimsuit":
        print("Beach Day!!!".center(50))
    else:
        print(verdict.center(50))

if __name__ == "__main__":
    main()
