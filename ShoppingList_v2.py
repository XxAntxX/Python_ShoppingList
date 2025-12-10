store_file = "shopping_lists_v2.json"

########## validation ##########

#---------- input validation predefined options
def input_validation_selector(prompt, valid_options):    
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in valid_options:
            return user_input
        else:
            print(f"Invalid input — please enter one of: {', '.join(valid_options)}")
            
#---------- required input (non-empty)
def required_input(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        else:
            print("This field cannot be empty. Please provide a valid input.")
            
#---------- input is float
def input_price(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input == "":
            return 0.0
        try:
            value = round(float(user_input), 2)
            return value
        except ValueError:
            print("Invalid input — please enter a valid number.")


######### start & create new  ##########
#---------- start selection
def start_select():
    print(f"\n----------PYTHON SHOPPING LIST----------\n")
    user_choice = input_validation_selector(f"[n] New shopping list \n[b] Browse shopping lists \n[q] Quit program \n \n", ("n", "b", "q"))
    if user_choice == "q":
        print("Exiting program. Goodbye!")
        return exit()
    elif user_choice == "n":
        print("Starting a new shopping list...")
        create_new_list()
    elif user_choice == "b":
        print("Browsing existing shopping lists...")
        load_list_from_record(import_lists())

#---------- create new shopping list
def create_new_list():
    list_name = ""
    list_name = required_input("Enter the name of your new shopping list: ").strip()
    entries = []
    print(f"New shopping list '{list_name}' created.")
    print(f"Add your first item to the shopping list.")
    add_entry(entries)
    shopping_list_handling_loop(entries, list_name, False)

######### manage shopping list functions ##########
    
#---------- shopping list handling loop
def shopping_list_handling_loop(entries, list_name, saved = True):
        while True:
            render_shopping_list(entries, list_name)
            user_choice = input_validation_selector(f"[a] Add entry \n[m] Modify entry \n[d] Delete entry \n[s] Save list \n[q] Quit to main menu \n[r] Remove shopping list \n \n", ("a", "m", "d", "s", "q", "r"))
            if user_choice == "q":
                if not saved:
                    print("You have unsaved changes. Do you want to quit before saving.")
                    while True:
                        user_input = input_validation_selector("Type 'y' to quit without saving, or 'n' to return: ", ("y", "n"))
                        if user_input == 'y':
                            print("Exiting to main menu without saving...")
                            return
                        elif user_input == 'n':
                            break
                else:
                    print("Returning to main menu...")
                    break
            elif user_choice == "a":
                add_entry(entries)
                saved = False
            elif user_choice == "m":
                modify_entry(entries)
                saved = False
            elif user_choice == "d":
                delete_entry(entries)
                saved = False
            elif user_choice == "s":
                saved = True
                save_list_to_file(entries, list_name)
            elif user_choice == "r":
                print("You are about to delete shopping list: " + list_name)
                user_input = input_validation_selector("Type 'y' to remove or 'n' to return: ", ("y", "n"))
                if user_input == 'y':
                    remove_list_from_file(list_name)
                    return

    
#---------- render shopping list
def render_shopping_list(entries, list_name):
    header_row = ("Item", "Quantity", "Price")
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
          
#---------- add new entry
def add_entry(entries): 
    item = required_input("Enter the item name: ").strip()
    quantity = input("Enter the quantity: ").strip()
    price = input_price("Enter the price: ")
    entries.append((item, quantity, price))
    print(f"Added entry: {item} - {quantity} - {price}")
    return entries
    
#---------- modify entry
def modify_entry(entries):
    if not entries:
        print("No entries to modify.")
        return
    while True:
        try:
            entry_num = int(input("Enter the entry number to modify: ").strip())
            if 1 <= entry_num <= len(entries):
                old_entries = entries[entry_num - 1]
                user_choice = input_validation_selector(f"select field to modify: \n[i] Item \n[q] Quantity \n[p] Price \n[a] All fields \n", ("i", "q", "p", "a"))
                if user_choice == "i":
                    item = required_input(f"Old name: {old_entries[0]} \nEnter the new item name: ").strip()
                    entries[entry_num - 1] = (item, old_entries[1], old_entries[2])
                    print(f"Modified entry {entry_num} to: {item} - {old_entries[1]} - {old_entries[2]}")
                    return entries
                elif user_choice == "q":
                    quantity = input(f"Old quantity: {old_entries[1]} \nEnter the new quantity: ").strip()
                    entries[entry_num - 1] = (old_entries[0], quantity, old_entries[2])
                    print(f"Modified entry {entry_num} to: {old_entries[0]} - {quantity} - {old_entries[2]}")
                    return entries
                elif user_choice == "p":
                    price = input_price(f"Old price: {old_entries[2]} \nEnter the new price: ")
                    entries[entry_num - 1] = (old_entries[0], old_entries[1], price)
                    print(f"Modified entry {entry_num} to: {old_entries[0]} - {old_entries[1]} - {price}")
                    return entries
                elif user_choice == "a":
                    item = required_input(f"Old name: {old_entries[0]} \nEnter the new item name: ").strip()
                    quantity = input(f"Old quantity: {old_entries[1]} \nEnter the new quantity: ").strip()
                    price = input_price(f"Old price: {old_entries[2]} \nEnter the new price: ")
                    entries[entry_num - 1] = (item, quantity, price)
                    print(f"Modified entry {entry_num} to: {item} - {quantity} - {price}")
                    return entries
            else:
                print(f"Invalid entry number. Please enter a number between 1 and {len(entries)}.")
        except ValueError:
            print("Invalid input. Please enter a valid entry number.")

#---------- delete entry
def delete_entry(entries):
    if not entries:
        print("No entries to delete.")
        return
    while True:
        try:
            entry_num = int(input("Enter the entry number to delete: ").strip())
            if 1 <= entry_num <= len(entries):
                deleted_entry = entries.pop(entry_num - 1)
                print(f"Deleted entry: {deleted_entry[0]} - {deleted_entry[1]} - {deleted_entry[2]}")
                return entries
            else:
                print(f"Invalid entry number. Please enter a number between 1 and {len(entries)}.")
        except ValueError:
            print("Invalid input. Please enter a valid entry number.")

########## show lists from file ##########    
def load_list_from_record(all_lists):
        print(f"Available shopping lists:")
        for idx, lst in enumerate(all_lists, start=1):
            print(f"{idx}. {lst.get('name', 'Unnamed List')}")
        while True:
            try:
                list_num = int(input("Enter the number of the shopping list to load (or 0 to cancel): ").strip())
                if list_num == 0:
                    print("Cancelled loading a shopping list.")
                    break
                elif 1 <= list_num <= len(all_lists):
                    selected_list = all_lists[list_num - 1]
                    list_name = selected_list.get("name", "Unnamed List")
                    entries = selected_list.get("entries", [])
                    print(f"Loaded shopping list '{list_name}'.")
                    shopping_list_handling_loop(entries, list_name)
                    break
                else:
                    print(f"Invalid number. Please enter a number between 1 and {len(all_lists)}, or 0 to cancel.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

########## file functions ##########
#---------- import json
def import_lists():
    import json, os
    global store_file
    if os.path.exists(store_file):
        try:
            with open(store_file, "r", encoding="utf-8") as fh:
                data = json.load(fh)
                if isinstance(data, list):
                    all_lists = []
                    all_lists[:] = data
                    return all_lists
        except Exception:
            print(f"Error reading or parsing {store_file}. Starting with an empty list.")
            return []
    else:
        return []
        
#---------- save list to file
def save_list_to_file(entries, list_name):
    import json
    global store_file
    record = {"name": list_name, "entries": entries}

    all_lists=import_lists()
    
    # upsert by name
    for i, r in enumerate(all_lists):
        if r.get("name") == list_name:
            all_lists[i] = record
            break
    else:
        all_lists.append(record)

    # persist store
    with open(store_file, "w", encoding="utf-8") as fh:
        json.dump(all_lists, fh, ensure_ascii=False, indent=2)

    print(f"Saved shopping list '{list_name}' to {store_file}")
    
#---------- remove list from file 
def remove_list_from_file(list_name):
    import json, os
    global store_file

    all_lists = import_lists()
    all_lists = [lst for lst in all_lists if lst.get("name") != list_name]

    with open(store_file, "w", encoding="utf-8") as fh:
        json.dump(all_lists, fh, ensure_ascii=False, indent=2)
    print(f"Deleted shopping list '{list_name}' from {store_file}")
    


#---------- main loop
while True:
    user_choice = start_select()

        
