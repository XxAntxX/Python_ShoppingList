# **📝 ShoppingList**

## Analysis

**Problem**

People have to go shopping from time to time. Most of them make lists in their mind or even go fully unprepared to the grocerie store. Because of this they tend to forget want they realy needed or they buy items that weren't really necessary.  

**Scenario**

With the ShoppingList people can list the items they need, the respective quantity, and even the price per item (if known). They can save and edit their list for future use.

**User stories:**
1. As a user, I want to list the items I need.
2. As a user, I want to add the quantity of the item (so I dont buy too little/much) and the price per piece (if I know it)
3. As a user, I want to reuse previous lists.
4. As a user, I want to delete lists if I don't need them anymore

**Use cases:**
- Create, edit, save and delete lists
- List items I want to buy
- Apply a qunatity and a price to an item
- Show all listed items

---

## ✅ Project Requirements

Each app must meet the following three criteria in order to be accepted (see also the official project guidelines PDF on Moodle):

1. Interactive app (console input)
2. Data validation (input checking)
3. File processing (read/write)

---

### 1. Interactive App (Console Input)

---
The application interacts with the user via the console. Users can:

- Navigate a main menu to create new lists or browse existing ones.  
- Modify lists by adding, modifying, or deleting specific entries.  
- View a formatted table of all items, quantities, and prices.
---

### 2. Data Validation

The application validates all user input to ensure data integrity and a smooth user experience. This is implemented in `ShoppingList.py` as follows:

- **Menu selection:** The user can choose between certain options at various parts in the program, the program checks if an input within the valid range is given:
	```python
	def input_validation_selector(prompt, valid_options):    
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in valid_options:
            return user_input
        else:
            print(f"Invalid input — please enter one of: {', '.join(valid_options)}")
	```
	This ensures only valid items can be listed.

- **Input validation:** When entering an input, the program checks whether an input is given or not:
	```python
	def required_input(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        else:
            print("This field cannot be empty. Please provide a valid input.")
	```

- **Float validation:** The program checks if a float is given, if the user inputs a price for an item:
	```python
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
	```

These checks prevent crashes and guide the user to provide correct input, matching the validation requirements described in the project guidelines.


---

### 3. File Processing

The application reads and writes data using a JSON file to ensure shopping lists are saved between sessions:

- **Storage file:** `shopping_lists.json` — This file acts as the database for the application.
    - **Writing:** When a user selects "Save list" or removes a list, the application serializes the list data into JSON format and writes it to this file.  
  	- **Reading:** When the application starts or when the user selects "Browse shopping lists," the application reads this file to retrieve and deserialize the stored lists.  
	- **Data Structure:** The data is stored as a list of dictionaries, where each dictionary represents a shopping list.
```
   [  
     {  
       "name": "Weekly Groceries",  
       "entries": [  
         ["Milk", "2 liters", 1.50],  
         ["Bread", "1 loaf", 2.00]  
       ]  
     }  
   ]
```


## ⚙️ Implementation

### Technology
- Python 3.x
- Environment: GitHub Codespaces
- Uses only Python’s standard library

### 📂 Repository Structure
```text
ShoppingList/
├── ShoppingList.py       # main program logic (console application)
├── shopping_lists.json   # JSON file storing all shopping lists (gets created on first run)
└── README.md             # project description and milestones
```

### How to Run
1. Open the repository in **GitHub Codespaces**
2. Open the **Terminal**
3. Run:
	```bash
	python3 ShoppingList.py
	```

### Libraries Used

- `os`: Used to check whether the JSON save file exists.
- `json`: Used to serialize and deserialize shopping lists for persistent storage.

These libraries are part of the Python standard library, so no external installation is required.


## 👥 Team & Contributions

| Name             | Contribution                                |
|------------------|---------------------------------------------|
| Anthony Kaufmann | Add, modify, delete and main loop functions |
| Silvan Aichholz  | Import, save, and load functions            |
| Jerry Wei        | Validation and render functions             |

## 🤝 Contributing

> 🚧 This is a template repository for student projects.  
> 🚧 Do not change this section in your final submission.

- Use this repository as a starting point by importing it into your own GitHub account.  
- Work only within your own copy — do not push to the original template.  
- Commit regularly to track your progress.

## 📝 License

This project is provided for **educational use only** as part of the Programming Foundations module.  
[MIT License](LICENSE)
