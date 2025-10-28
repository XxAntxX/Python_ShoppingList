#--------- Initiate variables
list_name = 0
entries = []
header_row = ("Item", "Quantity", "Price")






#---------- input validation predefined options
def input_validation_selector(input, valid_options):    
    while True:
        if input in valid_options:
            return input
        else:
            print(f"Invalid input — please enter one of: {', '.join(valid_options)}")
            return False

#---------- required input (non-empty)
def required_input(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        else:
            print("This field cannot be empty. Please provide a valid input.")

#---------- start selection
def start_select():
    print(f"\n----------PYTHON SHOPPING LIST----------\n")
    while True:
        user_input=input(f"[n] New shopping list \n[b] Browse shopping lists \n[q] Quit program \n \n").strip().lower()
        return input_validation_selector(user_input, ("n", "b", "q"))
    

#---------- get shopping lists


#---------- import file (shopping list)


#---------- create new shopping list
def create_new_list():
    global list_name, entries
    list_name = required_input("Enter the name of your new shopping list: ").strip()
    entries = []
    print(f"New shopping list '{list_name}' created.")
    print(f"Add your first item to the shopping list.")
    add_entry()
    shopping_list_handling_loop()
    
#---------- render shopping list

def render_shopping_list():
    global entries, header_row, list_name
    print(f"\nShopping List: {list_name}\n")

    cols = len(header_row)
    # compute max width per column from headers and data
    col_widths = [len(str(h)) for h in header_row]
    for row in entries:
        for i in range(cols):
            val = str(row[i]) if i < len(row) else ""
            col_widths[i] = max(col_widths[i], len(val))

    # add small padding to each column
    padding = 2
    col_widths = [w + padding for w in col_widths]

    # build a format string for the row
    row_fmt = " | ".join(f"{{:<{w}}}" for w in col_widths)

    header_line = " " * 5 + "| " + row_fmt.format(*header_row)
    print(header_line)
    print("-" * len(header_line))

    for idx, row in enumerate(entries, start=1):
        cells = [str(row[i]) if i < len(row) else "" for i in range(cols)]
        print(f"{idx:>3}  | " + row_fmt.format(*cells))

    print("\n")
    
    
#---------- shopping list selection
def shopping_list_select():
    while True:
        user_input = input(f"[a] Add entry \n[m] Modify entry \n[d] Delete entry \n[s] Save list \n[q] Quit to main menu \n \n").strip().lower()
        return input_validation_selector(user_input, ("a", "m", "d", "s", "q"))
            
            
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
                        user_input = input("Type 'y' to quit without saving, or 'n' to return: ").strip().lower()
                        if input_validation_selector(user_input, ("y", "n")):
                            if user_input == 'y':
                                print("Exiting to main menu without saving...")
                                return
                            elif user_input == 'n':
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
    item = required_input("Enter the item name: ").strip()
    quantity = input("Enter the quantity: ").strip()
    price = input("Enter the price: ").strip()
    entries.append((item, quantity, price))
    print(f"Added entry: {item} - {quantity} - {price}")




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
