#Code I Did Below

import random

print (str("\nFashion bot 9000".center(50)))


name=str(input("What is your first name? ")).title()
age=int(input("How old are you? "))

#hat

hat=str(input("Do you wear hats? ")).lower().strip()

if hat=="yes":
    hattype=input("So, "+name+" What type of hats do you wear? ").lower().strip()
if hat=="no":
    print("Thats Okay")
elif hattype=="beanie":
    print("Beanies Are Great For The Cold")
elif hattype=="baseball hat":
    print("Baseball Hats Are My Favorite!")
else:
    print("Not My First Choice But Its Still Good")

#top

top=str(input("So, "+name+" What Is Your Favorite Top? ")).lower().strip()
topresponse=random.choice(["That's a good choice.", "Ayy that’s lit.", "I like where this is going."])
if top=="none":
    print("Beach Day?")
else:
    print(topresponse)

#bottom

bottom=str(input("What about your choice of bottom? ")).lower().strip()
if bottom=="cargo pants":
    print("I Also Like Cargo Pants.")
elif bottom=="sweatpants":
    print("Sweatpants Are My Favorite!")
elif bottom=="swimsuit":
    print("Beach Day!!!")
elif bottom=="none":
    print("Weird")
else:
    print("You Can’t Go Wrong With "+bottom+".")
    
#shoes

shoes=str(input("What shoes do you like? ")).lower().strip()
if shoes=="adidas":
    print("I Love Adidas!")
elif shoes=="none":
    print("Going Barefoot? Bold Move.")
    
#fit

print("\nFinal Outfit For: "+name.strip())
if hat=="yes":
    print(hattype.title().strip().center(50))
else:
    print("No Hat".center(50))
    
if top=="none":
    print("No Top".center(50))
else:
    print(top.title().strip().center(50))

if bottom=="none":
    print("No Bottoms, Werido".center(50))
else:
    print(bottom.title().strip().center(50))
    
if shoes=="none":
    print("Barefoot".center(50))
else:
    print(shoes.title().strip().center(50))

#response

verdict=random.choice(["Looking Good!", "Fire Fit!","Looks Good"])
if top=="none" and bottom=="none":
    print("Go Put Some Clothes On!!".center(50))
elif top=="none" and bottom=="swimsuit":
    print("Beach Day!!!".center(50))
else:
    print(verdict.center(50))