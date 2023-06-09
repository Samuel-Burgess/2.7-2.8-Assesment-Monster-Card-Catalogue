"""Monster card program for AS 2.7-2.8 V1.0."""

import \
    easygui as eg  # import the easygui library for GUI and import it as e.g. for ease of use
import pickle

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


def welcome():  # Create a Welcome function to welcome the user and ask if they
    # want instructions
    global cards
    instructions = eg.buttonbox("Welcome to my Monster Cards Program! \n"
                                # buttonbox to eliminate user error
                                "If you want instructions, please press "
                                "{Display Instructions}\n"
                                "If you don't want instructions, press {Skip}",
                                "Welcome!",
                                choices=["Display Instructions",
                                         "Skip"])
    if instructions == "Display Instructions":  # if they want instructions,
        # display them
        eg.msgbox("Welcome to the Monster Cards Catalogue!\n"
                  "This is where we save all of the cards for our "
                  "Monster Cards game!\n"
                  "Each cards has 4 stats, Strength, Stealth,"
                  " Speed and Cunning.\n"
                  "in this program you can add cards, find existing cards"
                  " and edit them,\n"
                  "delete them, or print the full list of cards out"
                  "You will be prompted with buttons and choices,\n"
                  "So Please navigate through them and select the options"
                  " you want.\n"
                  "You may be asked to type in something\n"
                  "so if that happens please type into the box provided.",
                  "Instructions")
    load_y_n = eg.buttonbox("Load data?", "Load", choices=["Yes", "No"])
    if load_y_n == "Yes":
        with open('cards_dictionary.pickle', 'rb') as handle:
            cards = pickle.load(handle)


def main_menu():
    global cards
    choice = eg.buttonbox("What do you want to do?", "Main Menu",
                          choices=["Add Cards", "Search for cards",
                                   "Delete cards",
                                   "Print cards to console", "Exit"])
    if choice == "Add Cards":
        card_name = add_cards()  # Get the new card name from add_cards()
        if card_name is None:  # if cancelled, return to menu
            main_menu()
        else:
            edit_card(card_name)  # Pass the card name to edit_card()
            main_menu()  # Call the main menu again
    elif choice == "Search for cards":
        card_name = find_cards()  # get the found card in a variable so that
        # I can use it several times in the code
        if card_name is None:  # check for a cancelled search
            main_menu()
        else:  # ask the user what they want to do with the card
            user_choice = eg.buttonbox(f"Do you want to edit {card_name} or"
                                       f" do you want to delete it?",
                                       "Edit or delete",
                                       choices=["Edit", "delete", "Cancel"])
            if user_choice == "Edit":
                edit_card(card_name)  # edit the card
                main_menu()
            elif user_choice == "delete":  # delete it
                del cards[card_name]
                eg.msgbox(f"{card_name} has been deleted", f"{card_name} "
                                                           f"deleted")
                main_menu()
            else:
                eg.msgbox("Returning to menu", "Return to menu")
                main_menu()  # return to menu if user cancels
    elif choice == "Delete cards":
        delete_card()
    elif choice == "Print cards to console":
        print_cards()
        main_menu()
    else:  # exit message
        eg.msgbox("Thank you for using my program! I hope it was helpful.",
                  "Goodbye")
        save_y_n = eg.buttonbox("Save data?", "Save", choices=["Yes", "No"])
        # ask user if they want to save data
        if save_y_n == "Yes":
            with open('cards_dictionary.pickle', 'wb') as handle:
                # open cards_dictionary.pickle file and dump cards
                pickle.dump(cards, handle, protocol=pickle.HIGHEST_PROTOCOL)
            eg.msgbox("Data saved", "Data saved")
        else:
            eg.msgbox("Data not saved", "Data not saved")


def add_cards():  # add cards function gets the user to create a monster
    # card then returns that card
    global cards
    card_name = eg.enterbox("Please enter the name of the card you are "
                            "adding:", "Add Card")  # get name
    if card_name is None or card_name.strip() == "":
        eg.msgbox("Cancelled card creation", "Cancelled card creation")
        # account for cancellation
    else:
        new_card = {}  # create the new card's dictionary
        stats = ["Strength", "Speed", "Stealth", "Cunning"]
        # define the stats that will be given values
        for item in stats:
            while True:
                value = eg.integerbox(f"Please enter the value for"
                                      f" {card_name}'s {item}, "
                                      f"(min 1, max 25)",
                                      "Enter stat value",
                                      upperbound=25, lowerbound=1)
                # go through each stat getting the user to enter a value
                if value is not None:
                    break
            new_card[item] = value  # add the stat and value to the dictionary
        cards |= {card_name: new_card}
        # add the new card to the main dictionary
        return card_name


def edit_card(card_name):
    original_card_name = card_name  # Store the original card name

    while True:
        card = cards[card_name]
        msg = f"The card you are currently editing is {card_name}\n\n"
        # create the message for the first dialogue box
        msg += f"Strength:\t {card['Strength']}\n"
        msg += f"Speed:   \t {card['Speed']}\n"
        msg += f"Stealth: \t {card['Stealth']}\n"
        msg += f"Cunning: \t {card['Cunning']}\n"
        eg.msgbox(msg, f"Edit {card_name}")

        choice = eg.buttonbox("What would you like to edit?", "Editing Menu",
                              # editing menu
                              choices=["Edit stat", "Change name", "Exit"])
        if choice == "Edit stat":
            attribute = eg.choicebox("What stat will you edit?", "Edit Stat",
                                     # stat editing menu
                                     choices=["Strength", "Speed", "Stealth",
                                              "Cunning"])
            if attribute is None:
                eg.msgbox("Cancelled stat edit", "Cancel")
            else:
                card[attribute] = eg.integerbox(f"What will be {card_name}'s "
                                                f"{attribute}?",
                                                "Assign Value",
                                                upperbound=25, lowerbound=1)
                # get new stat value
        elif choice == "Change name":
            new_card_name = None
            while new_card_name is None:  # loop until a new name is given
                new_card_name = eg.enterbox(
                    "Please enter the new name for the card", "New Name")
                if new_card_name == original_card_name:
                    # check if they just input the same name
                    eg.msgbox(
                        "The new name is the same as the current name. "
                        "Please enter a different name.",
                        "Invalid Name")
                    new_card_name = None
                elif new_card_name in cards:  # check for duplicates
                    eg.msgbox(
                        f"There is already a card named {new_card_name}. "
                        f"Please enter a new name.",
                        "Card already exists")
                    new_card_name = None
                elif new_card_name is not None and new_card_name.strip() != '':
                    cards[new_card_name] = cards.pop(
                        card_name)  # Update the card name in the dictionary
                    card_name = new_card_name
                    # Update the current card name variable
                else:
                    eg.msgbox("Please enter a valid name",
                              "Enter a valid name")
                    # handles all other invalid names
        else:
            break


def find_cards():
    if len(cards) > 0:
        # make sure there are cards to find, then list all cards and
        # put them in a choice-box
        card_name = eg.choicebox("What card do you want to find?", "Find Card",
                                 choices=list(cards.keys()))
        if card_name is not None:
            card = cards[card_name]  # format message
            msg = f"The card you have found is {card_name}\n\n"
            msg += f"Strength:\t {card['Strength']}\n"
            msg += f"Speed:   \t {card['Speed']}\n"
            msg += f"Stealth: \t {card['Stealth']}\n"
            msg += f"Cunning: \t {card['Cunning']}\n"
            eg.msgbox(msg, f"Found {card_name}")
            return card_name  # return the card name
        else:
            eg.msgbox("Cancelled search", "Cancelled search")
            return None  # handle search cancellations
    else:
        eg.msgbox("No cards to find.", "Error")  # handle no cards error


def delete_card():
    if len(cards) > 0:  # check if there are cards to delete,
        # make a choice-box of all the cards
        card_name = eg.choicebox("Choose a card to delete:", "Delete Card",
                                 choices=list(cards.keys()))
        if card_name is not None:
            del cards[card_name]  # delete chosen card
            eg.msgbox(f"The {card_name} card has been deleted.",
                      "Card Deleted")
        else:
            eg.msgbox("Cancelled delete",
                      "Cancelled delete")  # handle cancellations
        main_menu()
    else:
        eg.msgbox("No cards to delete.", "Error")  # handle no cards error
        main_menu()


def print_cards():
    print("Monster Cards:")  # print all cards nicely formatted
    print("-------------------")

    for card_name, card_stats in cards.items():  # go through each card,
        # printing each stat and stat value
        print(f"Card: {card_name}")
        print("Stats:")
        print(f"  Strength: {card_stats['Strength']}")
        print(f"  Speed: {card_stats['Speed']}")
        print(f"  Stealth: {card_stats['Stealth']}")
        print(f"  Cunning: {card_stats['Cunning']}")
        print("-------------------")

    print("End of Monster Cards")


welcome()  # call welcome function
main_menu()  # call main menu
