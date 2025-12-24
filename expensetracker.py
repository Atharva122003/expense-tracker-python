def add_expense(expenses):
    try:
        amt = float(input("Enter amount: "))
        if amt <= 0:
            print("Amount must be greater than 0.\n")
            return
    except ValueError:
        print("Invalid input! Please enter a number.\n")
        return
    
    category = input("Enter category (e.g., Food, Transport, Bills): ").strip()
    if not category:
        category = "Misc"
    
    expenses.append({"amount": amt, "category": category})
    print(f"Added: {amt} under {category}\n")

def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded.\n")
        return
    
    print("\nExpenses List:")
    for i, exp in enumerate(expenses, 1):
        print(f"{i}. {exp['amount']} - {exp['category']}")
    
    total = sum(exp["amount"] for exp in expenses)
    print(f"\nTotal Spending: {total}")
    
    # Category-wise total
    category_totals = {}
    for exp in expenses:
        category_totals[exp["category"]] = category_totals.get(exp["category"], 0) + exp["amount"]
    
    print("Category-wise Spending:")
    for cat, amt in category_totals.items():
        print(f"{cat}: {amt}")
    print()

def delete_expense(expenses):
    view_expenses(expenses)
    if not expenses:
        return
    try:
        idx = int(input("Enter expense number to delete: "))
        removed = expenses.pop(idx - 1)
        print(f"Removed: {removed['amount']} - {removed['category']}\n")
    except (ValueError, IndexError):
        print("Invalid selection.\n")

def main():
    expenses = []
    print("💰 Python Expense Tracker")
    
    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Exit")
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            delete_expense(expenses)
        elif choice == "4":
            print("Goodbye! Keep tracking your expenses! 💵")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
