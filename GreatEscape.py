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
    print("  i______i\n  I______I\n  I      I\n  I______I\n /      /I\n(______( I\nI ^    I ^\nI      I")
    if 'chair' in options:
        options.remove('chair')
    while True:
        location = input("Would you like to check the top, side, or bottom...? (top/side/bottom/back) ")
        if location == "top":
            print("It's a slightly worn out chair, nothing special on top. The seats still a little warm...")
            time.sleep(2)
        elif location == "side":
            print("The side isn't anything special... the metal looks worn out...")
            time.sleep(2)
        elif location == "bottom":
            print("You find a piece of paper stuck to the chair with a piece of gum and you pull it out.")
            print("The paper reads " + chair_hint)
            if chair_hint not in hints:
                hints.append(chair_hint)
            time.sleep(2)
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
        location = input("Would you like to check the top, inside, or bottom...? (top|inside|bottom|go back) ")
        if location == "top":
            print("You spot a piece of paper, a pencil and some eraser shavings")
            choice = input("You go to inspect the... (paper|pencil) ")
            if choice == "paper":
                print("It looks like a cheat sheet with only useless information... ")
                time.sleep(2)
            elif choice == "pencil":
                pencil()
            else:
                print("A rumbling sound comes from.... is that the cabinet?")
        elif location == "inside":
            print("You find a piece of paper that states: " + table_hint)
            if table_hint not in hints:
                hints.append(table_hint)
            time.sleep(2)
        elif location == "bottom":
            print("You touch the rough bottom of the desk and feel some bumpy areas only to realize it's old gum.")
            time.sleep(2)
        elif location == "go back":
            break
        else:
            print("You inspect the table again")

def teacher_desk():
    print("You approch the teacher's desk...")
    if 'teacher\'s desk' in options:
        options.remove('teacher\'s desk')
    while True:
        location = input("Would you like to check the top, inside, or bottom...? (top|inside|bottom|go back) ")
        if location == "top":
            print("Here lies the laptop and some papers...")
            choice = input("Would you like to inspect the laptop or papers...? (laptop|papers) ")
            if choice == "laptop":
                laptop()
            elif choice == "papers":
                print("It's just some notes that professor left about class... ")
                time.sleep(2)
            else:
                print("A rumbling sound comes from.... is that the cabinet?")
                if 'cabinet' not in options:
                    options.append('cabinet')
                time.sleep(2)
                break
        elif location == "inside":
            print("The inside seems to be locked and needs a key... ")
            time.sleep(2)
        elif location == "bottom":
            print("There's nothing but dust bunnies down there... nothing too exciting. ")
            time.sleep(2)
        elif location == "go back":
            break
        else:
            print("You inspect the teacher's desk again")

def board():
    board_hint = "'To truly be free you must first find the keys to your success.'"
    print("You walk up to the smartboard and look at it...")
    if 'board' in options:
        options.remove('board')
    while True:
        choice = input("Would you like to turn it on...? (yes|no|go back) ")
        if choice == "yes":
            print("The smartboard slowly turns on and reveals another clue!...")
            print("On the board it says: " + board_hint)
            print("Oddly... the screen fades back to black... that's weird maybe it's broken.")
            if board_hint not in hints:
                hints.append(board_hint)
            time.sleep(2)
        elif choice == "no":
            print("The smartboard is off and will continue to stay off")
            time.sleep(2)
        elif choice == "go back":
            break
        else:
            print("You inspect the board again")

def laptop():
    print("You inspect the laptop...")
    print("   .===========.       \n   |           |        \n   |   |***|   |        \n   |           |        \n   |___________|        \n   |_________-_|_,-.    \n  [_____________]   )   \n  .,,,,,,,,,, ,,.  (_   \n /,,,,,,,,,,, ,,,\ (>`\ \n(______.-``-._____) \__)")
    if 'laptop' in options:
        options.remove('laptop')
    while True:
        choice = input("Would you like turn it on...? (yes|no|go back) ")
        if choice == "yes":
            print("You attempt to turn on the laptop but sadly it is protected by a password")
            enter_laptop = input("Can you crack the code? Enter the password...")
            if enter_laptop == "Stevens1870":
                print("The laptop opens to a screen with a background that reads '0264'")
                print("The cabinet grumbles and slowly opens...")
                options.append('safe')
                time.sleep(3)
            else:
                print("The laptop screen goes black and maniacal laughter echoes around you")
                time.sleep(2)
        elif choice == "no":
            print("You inspect it... it's odd that somebody left their laptop here huh?... ")
            time.sleep(2)
        elif choice == "go back":
            break
        else:
            print("You inspect the laptop again")

def cabinet():
    print("You walk over to the cabinet...")
    if 'cabinet' in options:
        options.remove('cabinet')
    while True:
        location = input("Would you like to check the top, inside, or bottom...? (top|inside|bottom|go back) ")
        if location == "top":
            print("It's just some old supplies and stuff, nothing else important here... ")
            time.sleep(2)
        elif location == "inside":
            print("Looks like it might need a little budging")
            time.sleep(2)
        elif location == "bottom":
            print("The cabinet legs left marks on the ground... looks like it was dragged here")
            time.sleep(2)
        elif location == "go back":
            break
        else:
            print("You inspect the cabinet again")

def safe():
    print("A safe inside the cabinet? Who would have thought...")
    if 'safe' in options:
        options.remove('safe')
    while True:
        choice = input("Would you like to open it...? (yes|no|go back)")
        if choice == "yes":
            code = input("You are prompted with a 4 number pinpad... What are those 4 numbers...? (Enter 4 numbers) ")
            if code == "0264":
                print("YOU FOUND THE KEY! Congratulations and have a beautiful break(:")
            else:
                print("Hmm that didn't seem to work... ")
        elif choice == "no":
            print("You ignore the safe... ")
        elif choice == "go back":
            break
        else:
            print("You inspect the safe again")

def pencil():
    pencil_hint = "ad astra"
    while True:
        choice = input("Would you like to pick up the pencil...? (yes|no) ")
        if choice == "yes":
            print("It looks like someone scratched a message... " + pencil_hint)
            if pencil_hint not in hints:
                hints.append(pencil_hint)
        elif choice == "no":
            print("You leave the pencil...")
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
        print("So many items to explore ", options)
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
            time.sleep(2)
            explore = input("A small violin plays in the background... you begin to approach the... (enter object) ")
    else:
        print("Then I guess you'll be here forever...")
    # if the user enters in a location that is not an option "There is nothing there..."

main()