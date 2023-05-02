"""Monster card program for AS 2.7-2.8. indev v05 Start on the edit cards function."""

import easygui as eg  # import the easygui library for GUI and import it as eg for ease of use

cards = {  # Create a 2D dictionary to store the cards and their stats
    "Stoneling": {
        "Strength": 7,
        "Speed": 1,
        "Stealth": 25,
        "Cunning": 15,
    },
    "Vexscream": {
        "Strength": 1,
        "Speed": 6,
        "Stealth": 21,
        "Cunning": 19
    },
    "Dawnmirage": {
        "Strength": 5,
        "Speed": 15,
        "Stealth": 18,
        "Cunning": 22
    },
    "Blazegolem": {
        "Strength": 15,
        "Speed": 20,
        "Stealth": 23,
        "Cunning": 6,
    },
    "Websnake": {
        "Strength": 7,
        "Speed": 15,
        "Stealth": 10,
        "Cunning": 5,
    },
    "Moldvine": {
        "Strength": 21,
        "Speed": 18,
        "Stealth": 14,
        "Cunning": 5
    },
    "Vortexwing": {
        "Strength": 19,
        "Speed": 13,
        "Stealth": 19,
        "Cunning": 2
    },
    "Rotthing": {
        "Strength": 16,
        "Speed": 7,
        "Stealth": 4,
        "Cunning": 12
    },
    "Froststep": {
        "Strength": 14,
        "Speed": 14,
        "Stealth": 17,
        "Cunning": 4,
    },
    "Wispghoul": {
        "Strength": 17,
        "Speed": 19,
        "Stealth": 3,
        "Cunning": 2
    }
}


def welcome():  # Create a Welcome function to welcome the user and ask if they want instructions
    instructions = eg.buttonbox("Welcome to my Monster Cards Program! \n"  # buttonbox to eliminate user error
                                "If you want instructions, please press {Display Instructions}\n"
                                "If you don't want instructions, press {Skip}", "Welcome!",
                                choices=["Display Instructions",
                                         "Skip"])
    if instructions == "Display Instructions":  # if they want instructions, display them
        eg.msgbox("You will be prompted with buttons and choices,\n"
                  "So Please navigate through them and select the options you want.\n"
                  "You may be asked to type in something\n"
                  "so if that happens please type into the box provided.", "Instructions")


def main_menu():  # create the main menu function that will be called upon multiple times
    global cards
    choice = eg.buttonbox("What do you want to do?", "Main Menu",  # use a buttonbox to ask user for choice
                          choices=["Add Cards", "Search for cards", "Delete cards",
                                   "Print cards to console", "Exit"])
    if choice == "Add Cards":
        new_card = add_cards()
        cards |= new_card  # add the returned value of the add_cards function to the cards dictionary
        edit_card(new_card)  # edit the newly made card
        main_menu()  # call main menu again
    elif choice == "Search for cards":
        print("search for cards")  # Placeholder for the find_cards() function
    elif choice == "Delete cards":
        print("Delete cards")  # Placeholder for the delete_cards() function
    elif choice == "Print cards to console":
        print(cards)  # Placeholder for the print_cards() function, printing the dictionary for testing purposes
    else:
        print("exit")


def add_cards():  # add cards function gets the user to create a monster card then returns that card
    card_name = str(eg.enterbox("Please enter the name of the card you are adding:", "Add Card"))  # user inputs name
    new_card = {}  # create the new card's dictionary
    stats = ["Strength", "Speed", "Stealth", "Cunning"]  # define the stats that will be given values
    for item in stats:
        value = eg.integerbox(f"Please enter the value for {card_name}'s {item}", "Enter stat value", upperbound=25,
                              lowerbound=1)  # go through each stat getting the user to enter a value
        new_card[item] = value  # add the stat and value to the dictionary
    return {card_name: new_card}  # Return the dictionary of the newest card


def edit_card(card):
    


welcome()
main_menu()
