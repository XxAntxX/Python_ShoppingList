a# 🍕 PizzaRP – Pizzeria Reference Project (Console)

> 🚧 This is a template repository for student project in the course Programming Foundations at FHNW, BSc BIT.  
> 🚧 Do not keep this section in your final submission.

This project is intended to:

- Practice the complete process from **problem analysis to implementation**
- Apply basic **Python** programming concepts learned in the Programming Foundations module
- Demonstrate the use of **console interaction, data validation, and file processing**
- Produce clean, well-structured, and documented code
- Prepare students for **teamwork and documentation** in later modules
- Use this repository as a starting point by importing it into your own GitHub account.  
- Work only within your own copy — do not push to the original template.  
- Commit regularly to track your progress.

# 🍕 TEMPLATE for documentation
> 🚧 Please remove this paragraphs having "🚧". These are comments for preparing the documentations.
> 
## 📝 Analysis

**Problem** > 🚧 Describe the real-world problem your application solves. (Not HOW, but WHAT)

People have to go shopping from time to time. Most of them make lists in their mind or even go fully unprepared to the grocerie store. Because of this they tend to forget want they realy needed or they buy items that weren't really necessary.  

**Scenario** > 🚧 Describe when and how a user will use your application

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

> 🚧 In this section, document how your project fulfills each criterion.  
---
The application interacts with the user via the console. Users can:
- Create, edit, save, and delete lists
- List items, the quantity of it and the respective price (if known)
- Can get an overview of all items listed, the quantity and the price per piece

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

---


### 3. File Processing

The application reads and writes data using files:

- **Input file:** `menu.txt` — Contains the pizza menu, one item per line in the format `PizzaName;Size;Price`.
	- Example:
		```
		item = required_input("Enter the item name: ")
		quantity = input("Enter the quantity: ")
		price = input_price("Enter the price: ")
		```
	- The application reads this file at startup to display available pizzas.

- **Output file:** `invoice_001.txt` (and similar) — Generated when when the user  is completed. Contains a summary of the items, quantities, prices.
	- Example:
		```
		Shopping List: Weekly Groceries

   		   | Item       | Quantity | Price   
		----------------------------------------
 		1  | Milk       | 2        | 1.50    
		2  | Bread      | 1        | 0.99    
		```
		- The output file serves as a record for both the user and the pizzeria, ensuring accuracy and transparency.

## ⚙️ Implementation

### Technology
- Python 3.x
- Environment: GitHub Codespaces
- Uses only Python’s standard library

### 📂 Repository Structure
```text
ShoppingList/
├── main.py               # main program logic (console application)
├── shopping_lists.json   # JSON file storing all shopping lists
├── docs/                 # optional screenshots or project documentation
└── README.md             # project description and milestones
```

### How to Run
> 🚧 Adjust if needed.
1. Open the repository in **GitHub Codespaces**
2. Open the **Terminal**
3. Run:
	```bash
	python3 main.py
	```

### Libraries Used

- `os`: Used to check whether the JSON save file exists.
- `json`: Used to serialize and deserialize shopping lists for persistent storage.

These libraries are part of the Python standard library, so no external installation is required. They were chosen for their simplicity and effectiveness in handling file management tasks in a console application.


## 👥 Team & Contributions

> 🚧 Fill in the names of all team members and describe their individual contributions below. Each student should be responsible for at least one part of the project.

| Name       | Contribution                                 |
|------------|----------------------------------------------|
| Student A  | Menu reading (file input) and displaying menu|
| Student B  | Order logic and data validation              |
| Student C  | Invoice generation (file output) and slides  |


## 🤝 Contributing

> 🚧 This is a template repository for student projects.  
> 🚧 Do not change this section in your final submission.

- Use this repository as a starting point by importing it into your own GitHub account.  
- Work only within your own copy — do not push to the original template.  
- Commit regularly to track your progress.

## 📝 License

This project is provided for **educational use only** as part of the Programming Foundations module.  
[MIT License](LICENSE)
