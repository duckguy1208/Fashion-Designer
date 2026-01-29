#!/usr/bin/env python3
import random

def get_hat_feedback(hat_yes_no, hat_type=None):
    """Returns feedback based on hat preference."""
    if hat_yes_no.lower().strip() == "yes":
        if not hat_type:
            return "Not My First Choice But Its Still Good"
        
        hat_type = hat_type.lower().strip()
        if hat_type == "beanie":
            return "Beanies Are Great For The Cold"
        elif hat_type == "baseball hat":
            return "Baseball Hats Are My Favorite!"
        else:
            return "Not My First Choice But Its Still Good"
    elif hat_yes_no.lower().strip() == "no":
        return "That's Okay"
    return None

def get_top_feedback(top_name):
    """Returns feedback for the chosen top."""
    if not top_name.strip():
        return "Beach Day?"
    return random.choice(["That's a good choice.", "Ayy that’s lit.", "I like where this is going."])

def get_bottom_feedback(bottom_name):
    """Returns feedback for the chosen bottom."""
    bottom = bottom_name.lower().strip()
    if bottom == "cargo pants":
        return "I Also Like Cargo Pants."
    elif bottom == "sweatpants":
        return "Sweatpants Are My Favorite!"
    elif bottom == "swimsuit":
        return "Beach Day!!!"
    elif bottom == "":
        return "Weird"
    else:
        return f"You Can’t Go Wrong With {bottom}."

def get_shoes_feedback(shoes_name):
    """Returns feedback for the chosen shoes."""
    if shoes_name.lower().strip() == "adidas":
        return "I Love Adidas!"
    return None

def get_final_verdict(top, bottom):
    """Returns the final fashion verdict."""
    if not top.strip() and not bottom.strip():
        return "Go Put Some Clothes On!!"
    if not top.strip() and bottom.lower().strip() == "swimsuit":
        return "Beach Day!!!"
    
    return random.choice(["Looking Good!", "Fire Fit!", "Looks Good"])

def main():
    print("\n" + " Fashion bot 9000".center(50))

    name = input("What is your first name? ").title().strip()
    
    try:
        age_input = input("How old are you? ")
        age = int(age_input)
    except ValueError:
        age = 0 

    # Hat
    hat = input("Do you wear hats? ")
    hat_type = None
    if hat.lower().strip() == "yes":
        hat_type = input(f"So, {name} What type of hats do you wear? ")
    
    feedback = get_hat_feedback(hat, hat_type)
    if feedback:
        print(feedback)

    # Top
    top = input(f"So, {name} What Is Your Favorite Top? ")
    print(get_top_feedback(top))

    # Bottom
    bottom = input("What about your choice of bottom? ")
    print(get_bottom_feedback(bottom))
    
    # Shoes
    shoes = input("What shoes do you like? ")
    shoe_feedback = get_shoes_feedback(shoes)
    if shoe_feedback:
        print(shoe_feedback)

    # Final Fit Output
    print("\n" + f"Final Outfit For: {name}".center(50))
    
    formatted_hat = hat_type.title() if (hat.lower().strip() == "yes" and hat_type) else "No Hat"
    print(formatted_hat.center(50))
    
    formatted_top = top.title() if top.strip() else "No Top"
    print(formatted_top.center(50))

    formatted_bottom = bottom.title() if bottom.strip() else "No Bottoms, Weirdo"
    print(formatted_bottom.center(50))
    
    formatted_shoes = shoes.title() if shoes.strip() else "Barefoot"
    print(formatted_shoes.center(50))

    # Response Verdict
    print(get_final_verdict(top, bottom).center(50))

if __name__ == "__main__":
    main()
