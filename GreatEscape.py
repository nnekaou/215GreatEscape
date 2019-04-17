# -*- coding: utf-8 -*-
"""
Created on Tues Mar 12 9:50:00 2019
Updated 

The goal of this project is to create an escape room for individuals to go through

@author: nu
@author: jl
"""

# create space for player to save name, keep track of hints, and maybe keep track of current location
class player:
    def __init__(self, name, hints, position):
        self.name = name
        self.hints = hints
        self.position = position
    
    

player.position = currentroom

player.hints = knowledge

# create each object and add prompts for interacting with each object
# when the player runs into a hint, it should be saved to their notes stash

def chair:
    print("You approach the chair...")
    location = print(input("Would you like to check the top, side, or bottom...? (top/side/bottom) "))
    if location == "top":
        print("It's a slightly worn out chair, nothing special on top. The seats still a little warm...")
    elif location == "side":
        print("The side isn't anything special... the metal looks worn out...")
    elif location == "bottom":
        print("You find a piece of paper stuck to the chair with a piece of gum and you pull it out.")
        print("The paper reads 'INSIDE DESK'")
        #Add this clue to note stash not sure how to do that lol!!!

def table:
    print("It's a pretty average table ... there are many like it in this classroom but you are drawn to this one")
    location = print(input("Would you like to check the top, inside, or bottom...? (top/inside/bottom) "))
    if location == "top":
        print("There's nothing suspicious on this table. It's a little smudged and there's there's some eraser shavings")
    elif location == "inside":
        print("You find a piece of paper that states 'The cabinet lies the answers' ")
    elif location == "bottom":
        print("You touch the rough bottom of the desk and feel some bumpy areas only to realize it's old gum.")

def teacher_desk:
    print("You approch the teacher's desk...")
    location = print(input("Would you like to check the top, inside, or bottom...? (top/inside/bottom) "))
    if location == "top":
        print("Here lies the laptop and some papers...")
        choice = print(input("Would you like to inspect the laptop or papers...? (laptop/papers) "))
        if choice == "laptop":
        	laptop()
        elif choice == "papers":
        	print("It's just some notes that professor left about class... ")
    elif location == "inside":
        print("The inside seems to be locked and needs a key... ")
    elif location == "bottom":
        print("There's nothing but dust bunnies down there... nothing too exciting. ")

def board:
    print("You walk up to the smartboard and look at it...")
    choice = print(input("Would you like to turn it on...? (y/n) "))
    if choice == "y":
        print("The smartboard slowly turns on and reveals another clue!...")
        print("On the board it says: 'To truly be free you must first find the keys to your success.' ")
        print("Oddly... the screen fades back to black... that's weird maybe it's broken.")
        #Add this to the hints
    elif choice == "n":
        print("The smartboard is off and will continue to stay off")

def laptop:
    print("You inspect the laptop...")
    choice = print(input("Would you like turn it on...? (y/n) ")
    if choice == "y":
        print("You attempt to turn on the laptop but sadly it is protected by a password")
        #add another password element for this
    elif choice == "n":
        print("You inspect it... it's odd that somebody left their laptop here huh?... ")
def cabinet:
    print("You walk over to the cabinet...")
    location = print(input("Would you like to check the top, inside, or bottom...? (top/inside/bottom) "))
    if location == "top":
        print("It's just some old supplies and stuff, nothing else important here... ")
    elif location == "inside":
        print("The cabinet is locked... There's a small keyhole next to it")
    elif location == "bottom":
        print("The cabinet legs left marks on the ground... looks like it was dragged here")
        #make option to move cabinet or not
#make it so the option for the safe only shows up after the cabinet is unlocked. Also should we make different def's for like "inside the cabinet" and stuff like that "or inside laptop"
def safe:
    print("You look at the safe...")
    choice = print(input("Would you like to open it...? (y/n)"))
    if choice == "y":
        code = print(input("You are prompted with a 4 number pinpad... What are those 4 numbers...? (Enter 4 numbers) ")
        if code == "0264":
        	#TODO
        else:
        	print("Hmm that didn't seem to work... ")
    elif choice == "n":
        print("You ignore the safe... ")
def pencil:
    print("You inspect the pencil...")
    location = print(input("Would you like to take the pencil...? (y/n) "))
    if choice == "y":
        print("You take the pencil and add it to your inventory")
        #add to inventory and the option to go to the pencil disappears
    elif choice == "n":
        print("You leave the pencil...")

#create a main that prompts them to interact with the room "what do you want to inspect..."
#always give the option to check stored hints

#we can make all of this ugly then make it pretty when it works lol