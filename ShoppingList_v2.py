import json
import os


# Constants
STORE_FILE = "shopping_lists_v2.json"


def input_validation_selector(prompt, valid_options):
    """
    Validate user input against a list of predefined options.
    """
    while True:
        # Normalize input to lowercase to ensure case-insensitive comparison
        user_input = input(prompt).strip().lower()
        if user_input in valid_options:
            return user_input
        else:
            print(f"Invalid input — please enter one of: {', '.join(valid_options)}")


def required_input(prompt):
    """
    Request input from the user and ensure it is not empty.
    """
    while True:
        user_input = input(prompt).strip()
        # Ensure we don't return an empty string, which would break data consistency
        if user_input:
            return user_input
        else:
            print("This field cannot be empty. Please provide a valid input.")


def input_price(prompt):
    """
    Request a price input, ensuring it is a valid float.
    Returns 0.0 if input is empty.
    """
    while True:
        user_input = input(prompt).strip()
        # Allow empty input to default to 0.0 for free items or optional pricing
        if user_input == "":
            return 0.0
        try:
            # Round to 2 decimal places to maintain standard currency formatting
            value = round(float(user_input), 2)
            return value
        except ValueError:
            print("Invalid input — please enter a valid number.")


def start_select():
    """
    Display the main menu and route the user to the chosen action.
    """
    print(f"\n----------PYTHON SHOPPING LIST----------\n")
    user_choice = input_validation_selector(
        f"[n] New shopping list \n[b] Browse shopping lists \n"
        f"[q] Quit program \n \n",
        ("n", "b", "q"),
    )
    if user_choice == "q":
        print("Exiting program. Goodbye!")
        # Use exit() to cleanly terminate the script execution immediately
        exit()
    elif user_choice == "n":
        print("Starting a new shopping list...")
        create_new_list()
    elif user_choice == "b":
        print("Browsing existing shopping lists...")
        load_list_from_record(import_lists())


def create_new_list():
    """
    Initialize a new shopping list and enter the handling loop.
    """
    # Strip whitespace to prevent creating lists with names that appear empty
    list_name = required_input("Enter the name of your new shopping list: ").strip()
    entries = []
    print(f"New shopping list '{list_name}' created.")
    print(f"Add your first item to the shopping list.")
    add_entry(entries)
    # Pass saved=False because a new list hasn't been persisted to disk yet
    shopping_list_handling_loop(entries, list_name, False)


def shopping_list_handling_loop(entries, list_name, saved=True):
    """
    Main loop for managing a specific shopping list (add, modify, delete).
    """
    while True:
        render_shopping_list(entries, list_name)
        user_choice = input_validation_selector(
            f"[a] Add entry \n[m] Modify entry \n[d] Delete entry \n"
            f"[s] Save list \n[q] Quit to main menu \n"
            f"[r] Remove shopping list \n \n",
            ("a", "m", "d", "s", "q", "r"),
        )
        if user_choice == "q":
            # Check for unsaved changes to prevent accidental data loss
            if not saved:
                print("You have unsaved changes. Do you want to quit before saving.")
                while True:
                    user_input = input_validation_selector(
                        "Type 'y' to quit without saving, or 'n' to return: ",
                        ("y", "n"),
                    )
                    if user_input == "y":
                        print("Exiting to main menu without saving...")
                        return
                    elif user_input == "n":
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
            user_input = input_validation_selector(
                "Type 'y' to remove or 'n' to return: ", ("y", "n")
            )
            if user_input == "y":
                remove_list_from_file(list_name)
                return


def render_shopping_list(entries, list_name):
    """
    Format and print the current shopping list to the console.
    """
    header_row = ("Item", "Quantity", "Price")
    print(f"\nShopping List: {list_name}\n")

    cols = len(header_row)
    # Calculate widths based on content to ensure the table layout adapts to data
    col_widths = [len(str(h)) for h in header_row]
    for row in entries:
        for i in range(cols):
            val = str(row[i]) if i < len(row) else ""
            col_widths[i] = max(col_widths[i], len(val))

    # Add padding to prevent columns from visually merging together
    padding = 2
    col_widths = [w + padding for w in col_widths]

    # Use dynamic formatting to align columns correctly based on calculated widths
    row_fmt = " | ".join(f"{{:<{w}}}" for w in col_widths)

    header_line = " " * 5 + "| " + row_fmt.format(*header_row)
    print(header_line)
    print("-" * len(header_line))

    for idx, row in enumerate(entries, start=1):
        cells = [str(row[i]) if i < len(row) else "" for i in range(cols)]
        print(f"{idx:>3}  | " + row_fmt.format(*cells))

    print("\n")


def add_entry(entries):
    """
    Prompt user for item details and append to the entries list.
    """
    item = required_input("Enter the item name: ").strip()
    quantity = input("Enter the quantity: ").strip()
    price = input_price("Enter the price: ")
    entries.append((item, quantity, price))
    print(f"Added entry: {item} - {quantity} - {price}")
    return entries


def modify_entry(entries):
    """
    Modify an existing entry in the list by index.
    """
    if not entries:
        print("No entries to modify.")
        return
    while True:
        try:
            entry_num = int(input("Enter the entry number to modify: ").strip())
            # Validate index range to avoid IndexError
            if 1 <= entry_num <= len(entries):
                old = entries[entry_num - 1]
                user_choice = input_validation_selector(
                    f"select field to modify: \n[i] Item \n[q] Quantity \n"
                    "[p] Price \n[a] All fields \n",
                    ("i", "q", "p", "a"),
                )
                if user_choice == "i":
                    item = required_input(
                        f"Old name: {old[0]} \nEnter the new item name: "
                    ).strip()
                    entries[entry_num - 1] = (item, old[1], old[2])
                    print(f"Modified entry {entry_num} to: {item} - {old[1]} - {old[2]}")
                    return entries
                elif user_choice == "q":
                    quantity = input(
                        f"Old quantity: {old[1]} \nEnter the new quantity: "
                    ).strip()
                    entries[entry_num - 1] = (old[0], quantity, old[2])
                    print(f"Modified entry {entry_num} to: {old[0]} - {quantity} - {old[2]}")
                    return entries
                elif user_choice == "p":
                    price = input_price(
                        f"Old price: {old[2]} \nEnter the new price: "
                    )
                    entries[entry_num - 1] = (old[0], old[1], price)
                    print(f"Modified entry {entry_num} to: {old[0]} - {old[1]} - {price}")
                    return entries
                elif user_choice == "a":
                    item = required_input(
                        f"Old name: {old[0]} \nEnter the new item name: "
                    ).strip()
                    quantity = input(
                        f"Old quantity: {old[1]} \nEnter the new quantity: "
                    ).strip()
                    price = input_price(
                        f"Old price: {old[2]} \nEnter the new price: "
                    )
                    entries[entry_num - 1] = (item, quantity, price)
                    print(f"Modified entry {entry_num} to: {item} - {quantity} - {price}")
                    return entries
            else:
                print(f"Invalid number. Enter between 1 and {len(entries)}.")
        except ValueError:
            print("Invalid input. Please enter a valid entry number.")


def delete_entry(entries):
    """
    Remove an entry from the list by index.
    """
    if not entries:
        print("No entries to delete.")
        return
    while True:
        try:
            entry_num = int(input("Enter the entry number to delete: ").strip())
            # Ensure the user selects a valid index to prevent runtime errors
            if 1 <= entry_num <= len(entries):
                deleted = entries.pop(entry_num - 1)
                print(f"Deleted: {deleted[0]} - {deleted[1]} - {deleted[2]}")
                return entries
            else:
                print(f"Invalid number. Enter between 1 and {len(entries)}.")
        except ValueError:
            print("Invalid input. Please enter a valid entry number.")


def load_list_from_record(all_lists):
    """
    Display available lists and load the selected one.
    """
    print(f"Available shopping lists:")
    for idx, lst in enumerate(all_lists, start=1):
        # Use .get() with a default to handle cases where 'name' might be missing
        print(f"{idx}. {lst.get('name', 'Unnamed List')}")
    while True:
        try:
            list_num = int(
                input(
                    "Enter number of the shopping list to load (0 to cancel): "
                ).strip()
            )
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
                print(
                    f"Invalid number. Please enter a number between 1 and "
                    f"{len(all_lists)}, or 0 to cancel."
                )
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def import_lists():
    """
    Load all shopping lists from the JSON store file.
    """
    global STORE_FILE
    if os.path.exists(STORE_FILE):
        try:
            with open(STORE_FILE, "r", encoding="utf-8") as fh:
                data = json.load(fh)
                if isinstance(data, list):
                    # Return a shallow copy to ensure we have a mutable list
                    return data[:]
        # Catch specific exceptions to handle file corruption or read errors gracefully
        except (OSError, json.JSONDecodeError):
            print(f"Error reading {STORE_FILE}. Starting with an empty list.")
            return []
    else:
        return []


def save_list_to_file(entries, list_name):
    """
    Save the current list to the JSON store file (upsert logic).
    """
    global STORE_FILE
    record = {"name": list_name, "entries": entries}

    all_lists = import_lists()

    # Iterate to find if the list already exists; if so, update it (upsert)
    for i, r in enumerate(all_lists):
        if r.get("name") == list_name:
            all_lists[i] = record
            break
    else:
        # If the loop completes without finding the name, append as a new list
        all_lists.append(record)

    with open(STORE_FILE, "w", encoding="utf-8") as fh:
        json.dump(all_lists, fh, ensure_ascii=False, indent=2)

    print(f"Saved shopping list '{list_name}' to {STORE_FILE}")


def remove_list_from_file(list_name):
    """
    Delete a specific shopping list from the JSON store file.
    """
    global STORE_FILE

    all_lists = import_lists()
    # Filter out the list to be deleted using a list comprehension
    all_lists = [lst for lst in all_lists if lst.get("name") != list_name]

    with open(STORE_FILE, "w", encoding="utf-8") as fh:
        json.dump(all_lists, fh, ensure_ascii=False, indent=2)
    print(f"Deleted shopping list '{list_name}' from {STORE_FILE}")


def main():
    """
    Main application entry point.
    """
    while True:
        start_select()


# Enclose main execution in a block to allow safe importing as a module
if __name__ == "__main__":
    main()