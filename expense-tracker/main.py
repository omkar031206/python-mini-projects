print("!!Welcome to the Expense Tracker!!")
print("!!You can track your expenses in the following categories: Food, Travel, Bills. and also add other expenses as well!!")
print("\n")
expense = {
    "Food":{
        "Pizza"     :   370,
        "Burger"    :   100,
        "Chips"     :   50,
        "Shake"     :   80,
        "Dessert"   :   120
    },
    "Travel":{
        "Udaipur" : 18000,
        "Amritsar": 17550,
        "Mumbai"  : 55630,
        "London"  : 163500,
    },
    "Bills":{
        "EMI's"     : 25470,
        "Education" : 15825,
        "Rent"      : 35000,
        "Insurance" : 5655
    }
}
while True:
    print("1. Add Expense")
    print("2. View Expense")
    print("3. View Total Expense")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        category = input("Enter category (Food/Travel/Bills): ")
        item = input("Enter item name: ")
        amount = int(input("Enter amount: "))
        
        if category in expense:
            expense[category][item] = amount
        else:
            expense[category] = {item: amount}
    
    elif choice == 2:
        category = input("Enter category to view (Food/Travel/Bills): ")
        if category in expense:
            print(f"Expenses in {category}:")
            for item, amount in expense[category].items():
                print(f"{item}: {amount}")
        else:
            print("Category not found.")
    elif choice == 3:
        total_expense = sum(sum(items.values()) for items in expense.values())
        print(f"Total Expense: {total_expense}")                
    elif choice == 4:
        print("Exiting the program.")
        break   
    else:        print("Invalid choice. Please try again.")
    
