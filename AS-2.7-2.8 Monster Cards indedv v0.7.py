"""Monster card program for AS 2.7-2.8. indev v07 edited none checkers and debugged current code."""

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
        edit_card(add_cards())
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
    global cards
    card_name = None
    while card_name is None:
        card_name = eg.enterbox("Please enter the name of the card you are adding:", "Add Card")
    new_card = {}  # create the new card's dictionary
    stats = ["Strength", "Speed", "Stealth", "Cunning"]  # define the stats that will be given values
    for item in stats:
        while True:
            value = eg.integerbox(f"Please enter the value for {card_name}'s {item}", "Enter stat value", upperbound=25,
                                  lowerbound=1)  # go through each stat getting the user to enter a value
            if value is not None:
                break
        new_card[item] = value  # add the stat and value to the dictionary
    cards |= {card_name: new_card}  # add the new card to the main dictionary
    return card_name


def edit_card(card_name):
    while True:
        card = cards[card_name]
        msg = f"The card you are currently editing is {card_name}\n\n"  # create the message for the first dialogue box
        msg += f"Strength:\t {card['Strength']}\n"
        msg += f"Speed:   \t {card['Speed']}\n"
        msg += f"Stealth: \t {card['Stealth']}\n"
        msg += f"Cunning: \t {card['Cunning']}\n"
        eg.msgbox(msg, f"Edit {card_name}")
        choice = eg.buttonbox("What would you like to edit?", "Editing Menu",  # editing menu
                              choices=["Edit stat", "Change name", "Exit"])
        if choice == "Edit stat":
            attribute = eg.choicebox("What stat will you edit?", "Edit Stat",  # stat editing code
                                     choices=["Strength", "Speed", "Stealth", "Cunning"])
            if attribute is None:
                eg.msgbox("Cancelled stat edit")
            else:
                card[attribute] = eg.integerbox(f"What will be {card_name}'s {attribute}?", "Assign Value",
                                                upperbound=25, lowerbound=1)
        elif choice == "Change name":
            new_card_name = None
            while new_card_name is None:  # name change code
                new_card_name = eg.enterbox("Please enter the new name for the card", "New Name")
                if new_card_name in cards and new_card_name != card_name:  # check for duplicates
                    eg.msgbox(f"There is already a card named {new_card_name}, please enter a new name",
                              "Card already exists")
                    new_card_name = None
            card_name = new_card_name  # change name of card to the new name
        else:
            break


welcome()
main_menu()
