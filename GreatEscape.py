# -*- coding: utf-8 -*-
"""
Created on Tues Mar 12 9:50:00 2019
Updated 

The goal of this project is to create an escape room for individuals to go through

@author: nu
@author: jl
"""
import time

# create space for player to save name, keep track of hints, and maybe keep track of current location
class player:
    def __init__(self, name, hints, position):
        self.name = name
        self.hints = hints

# ^need to know how to set up player info of if it matters

hints = []
options = ['chair','table','teacher\'s desk','board','laptop','cabinet','hints']

# create each object and add prompts for interacting with each object
# when the player runs into a hint, it should be saved to their notes stash

def chair():
    chair_hint = "'HTML, but make it Proper'"
    print("You approach the chair...")
    if 'chair' in options:
        options.remove('chair')
    while True:
        location = input("Would you like to check the top, side, or bottom...? (top/side/bottom/back) ")
        if location == "top":
            print("It's a slightly worn out chair, nothing special on top. The seats still a little warm...")
        elif location == "side":
            print("The side isn't anything special... the metal looks worn out...")
        elif location == "bottom":
            print("You find a piece of paper stuck to the chair with a piece of gum and you pull it out.")
            print("The paper reads " + chair_hint)
            #Add this clue to note stash not sure how to do that lol!!!
            hints.append(chair_hint)
        elif location =="back":
            break
        else:
            print("You inspect the chair again")

def table():
    table_hint = "'It is when it came first but now it is second, it started the clock for us all to be beckoned'"
    print("It's a pretty average table ... there are many like it in this classroom but you are drawn to this one")
    if 'table' in options:
        options.remove('table')
    while True:
        location = input("Would you like to check the top, inside, or bottom...? (top/inside/bottom/back) ")
        if location == "top":
            print("You spot a piece of paper, a pencil and some eraser shavings")
            choice = input("You go to inspect the... (paper|pencil)")
            if choice == "paper":
                print("It looks like a cheat sheet with only useless information... ")
            elif choice == "pencil":
                pencil()
            else:
                print("A rumbling sound comes from.... is that the cabinet?")
        elif location == "inside":
            print("You find a piece of paper that states: " + table_hint)
            hints.append(table_hint)
        elif location == "bottom":
            print("You touch the rough bottom of the desk and feel some bumpy areas only to realize it's old gum.")
        elif location == "back":
            break
        else:
            print("You inspect the table again")

def teacher_desk():
    print("You approch the teacher's desk...")
    if 'teacher\'s desk' in options:
        options.remove('teacher\'s desk')
    while True:
        location = input("Would you like to check the top, inside, or bottom...? (top|inside|bottom|back) ")
        if location == "top":
            print("Here lies the laptop and some papers...")
            choice = input("Would you like to inspect the laptop or papers...? (laptop|papers) ")
            if choice == "laptop":
                laptop()
            elif choice == "papers":
                print("It's just some notes that professor left about class... ")
            else:
                print("A rumbling sound comes from.... is that the cabinet?")
        elif location == "inside":
            print("The inside seems to be locked and needs a key... ")
        elif location == "bottom":
            print("There's nothing but dust bunnies down there... nothing too exciting. ")
        elif location == "back":
            break
        else:
            print("You inspect the teacher's desk again")

def board():
    board_hint = "'To truly be free you must first find the keys to your success.'"
    print("You walk up to the smartboard and look at it...")
    if 'board' in options:
        options.remove('board')
    while True:
        choice = input("Would you like to turn it on...? (y/n/back) ")
        if choice == "y":
            print("The smartboard slowly turns on and reveals another clue!...")
            print("On the board it says: " + board_hint)
            print("Oddly... the screen fades back to black... that's weird maybe it's broken.")
            hints.append(board_hint)
        elif choice == "n":
            print("The smartboard is off and will continue to stay off")
        elif choice == "back":
            break
        else:
            print("You inspect the board again")

def laptop():
    print("You inspect the laptop...")
    if 'laptop' in options:
        options.remove('laptop')
    while True:
        choice = input("Would you like turn it on...? (yes|no|back) ")
        if choice == "yes":
            print("You attempt to turn on the laptop but sadly it is protected by a password")
            enter_laptop = input("Can you crack the code? Enter the password...")
            if enter_laptop == "Stevens1870":
                print("The laptop opens to a screen with a background that reads '0264'")
            else:
                print("The laptop screen goes black and maniacal laughter echoes around you")
            #add another password element for this
        elif choice == "no":
            print("You inspect it... it's odd that somebody left their laptop here huh?... ")
        elif choice == "back":
            break
        else:
            print("You inspect the laptop again")

def cabinet():
    print("You walk over to the cabinet...")
    if 'cabinet' in options:
        options.remove('cabinet')
    while True:
        location = input("Would you like to check the top, inside, or bottom...? (top|inside|bottom|back) ")
        if location == "top":
            print("It's just some old supplies and stuff, nothing else important here... ")
        elif location == "inside":
            print("The cabinet is locked... There's a small keyhole next to it")
        elif location == "bottom":
            print("The cabinet legs left marks on the ground... looks like it was dragged here")
            #make option to move cabinet or not
    #make it so the option for the safe only shows up after the cabinet is unlocked. Also should we make different def's for like "inside the cabinet" and stuff like that "or inside laptop"
        elif location == "back":
            break
        else:
            print("You inspect the cabinet again")

def safe():
    print("You look at the safe...")
    if 'safe' in options:
        options.remove('safe')
    while True:
        choice = input("Would you like to open it...? (yes|no|back)")
        if choice == "yes":
            code = input("You are prompted with a 4 number pinpad... What are those 4 numbers...? (Enter 4 numbers) ")
            if code == "0264":
                print("YOU FOUND THE KEY! Congratulations and have a beautiful break(:")
            else:
                print("Hmm that didn't seem to work... ")
        elif choice == "no":
            print("You ignore the safe... ")
        elif choice == "back":
            break
        else:
            print("You inspect the safe again")

def pencil():
    pencil_hint = "ad astra"
    print("You inspect the pencil...")
    while True:
        choice = input("Would you like to take the pencil...? (yes|no|back) ")
        if choice == "yes":
            print("It looks like someone scratched a message... :" + pencil_hint)
            #add to inventory and the option to go to the pencil disappears
        elif choice == "no":
            print("You leave the pencil...")
        elif choice == "back":
            break
        else:
            print("You inspect the pencil again")

#create a main that prompts them to interact with the room "what do you want to inspect..."
#always give the option to check stored hints

def main():
    print("*Sound of door slamming closed*")
    print("“Huh? Why am I in my Software Engineering classroom?”")
    print("You see a note... would you like to pick it up?")
    begin = input("yes|no... ")

    if begin.lower() == "yes":
        print("Somewhere in this room, there lies a key, you need this key to escape, you can try to break the door but it won’t work, no one is coming for you, solve the puzzle and it is your only way to escape >:D")
        print("You begin to explore the room...")
        print("You can exit this game at any time by entering 'exit' and check your list of hints at any time by entering 'hints'")
        explore = input("You being to explore the room... what would you to check first? ")
        while explore != "exit":
            if explore == "chair":
                chair()
            elif explore == "table":
                table()
            elif explore == "teacher's desk":
                teacher_desk()
            elif explore == "board":
                board()
            elif explore == "laptop":
                laptop()
            elif explore == "cabinet":
                cabinet()
            elif explore == "hints":
                print("You think about the hints you've found... ", hints)
                time.sleep(4)
            print("You wonder what you haven't checked and look around... ", options)
            time.sleep(4)
            explore = input("A small violin plays in the background... you begin to approach the... (enter object) ")
    else:
        print("Then I guess you'll be here forever...")
    # if the user enters in a location that is not an option "There is nothing there..."

main()