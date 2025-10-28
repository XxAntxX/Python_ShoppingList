#--------- Initiate variables
list_name = 0
entries = []
header_row = ("Item", "Quantity")





#---------- input validation predefined options
def input_validation_selector(input, valid_options):    
    while True:
        if input in valid_options:
            return input
        else:
            print(f"Invalid input — please enter one of: {', '.join(valid_options)}")
            return False


#---------- start selection
def start_select():
    print(f"\n----------PYTHON SHOPPING LIST----------\n")
    while True:
        terminal_input=input(f"[n] New shopping list \n[b] Browse shopping lists \n[q] Quit program \n \n").strip().lower()
        return input_validation_selector(terminal_input, ("n", "b", "q"))
    

#---------- get shopping lists


#---------- import file (shopping list)


#---------- create new shopping list
def create_new_list():
    global list_name, entries
    list_name = input("Enter the name of your new shopping list: ").strip()
    entries = []
    print(f"New shopping list '{list_name}' created.")
    print(f"Add your first item to the shopping list.")
    add_entry()
    shopping_list_handling_loop()
    
#---------- render shopping list
def render_shopping_list():
    global entries
    print(f"\nShopping List: {list_name}\n")
    print(f" " * 5 + f"| {header_row[0]:<25} | {header_row[1]:<15}")
    print("-" * 50)
    for item, quantity in entries:
        index = entries.index((item, quantity)) + 1
        print(f"{index:>3}  | {item:<25} | {quantity:<15}")
    print("\n")
    
#---------- shopping list selection
def shopping_list_select():
    while True:
        terminal_input = input(f"[a] Add entry \n[m] Modify entry \n[d] Delete entry \n[s] Save list \n[q] Quit to main menu \n \n").strip().lower()
        return input_validation_selector(terminal_input, ("a", "m", "d", "s", "q"))
            
            
#---------- shopping list handling loop
def shopping_list_handling_loop():
        saved = False
        while True:
            render_shopping_list()
            user_choice = shopping_list_select()
            if user_choice == "q":
                if not saved:
                    print("You have unsaved changes. Do you want to quit before saving.")
                    while True:
                        terminal_input = input("Type 'y' to quit without saving, or 'n' to return: ").strip().lower()
                        if input_validation_selector(terminal_input, ("y", "n")):
                            if terminal_input == 'y':
                                print("Exiting to main menu without saving...")
                                return
                            elif terminal_input == 'n':
                                break
                else:
                    print("Returning to main menu...")
                    break
            elif user_choice == "a":
                add_entry()
            elif user_choice == "m":
                print("Modify entry feature coming soon!")
            elif user_choice == "d":
                print("Delete entry feature coming soon!")
            elif user_choice == "s":
                saved = True
                print("Save list feature coming soon!")

#---------- add new entry
def add_entry(): 
    global entries
    item = input("Enter the item name: ").strip()
    quantity = input("Enter the quantity: ").strip()
    entries.append((item, quantity))
    print(f"Added entry: {item} - {quantity}")



#---------- modify entry


#---------- delete entry


#---------- save list to file

    




#---------- main loop
while True:
    user_choice = start_select()
    if user_choice == "q":
        print("Exiting program. Goodbye!")
        break
    elif user_choice == "n":
        print("Starting a new shopping list...")
        create_new_list()
    elif user_choice == "b":
        print("Browsing existing shopping lists...")
        # Code to browse existing shopping lists would go here
