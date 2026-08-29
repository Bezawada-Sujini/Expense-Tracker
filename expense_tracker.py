import json

expenses = []

def save_expenses():
    with open("expenses.json", "w") as f:
        json.dump(expenses, f, indent=4)

def load_expenses():
    try:
        with open("expenses.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

expenses = load_expenses()
deleted_expenses = []

def add_expense():
    try:
        amount = float(input("Enter amount: ₹"))
    except ValueError:
        print("Invalid amount. Please enter a number.\n")
        return
    category = input("Enter category (food/travel/groceries/utensils/other): ")
    note = input("Enter a short note: ")
    expense = {
        "amount": amount,
        "category": category,
        "note": note
    }
    expenses.append(expense)
    save_expenses()
    print("Expense added!\n")

def view_expenses():
    if not expenses:
        print("No expenses yet.\n")
        return
    print("\n--- All Expenses ---")
    for i, e in enumerate(expenses, start=1):
        print(f"{i}. ₹{e['amount']} | {e['category']} | {e['note']}")
    print()

def total_spending():
    if not expenses:
        print("No expenses yet.\n")
        return
    total = sum(e["amount"] for e in expenses)
    print(f"\nTotal spent: ₹{total}\n")

def filter_by_category():
    category = input("Enter category to filter (food/travel/groceries/utensils/other): ")
    filtered = [e for e in expenses if e["category"].lower() == category.lower()]
    if not filtered:
        print(f"No expenses found in '{category}'.\n")
        return
    print(f"\n--- Expenses in '{category}' ---")
    for i, e in enumerate(filtered, start=1):
        print(f"{i}. ₹{e['amount']} | {e['note']}")
    print()

def delete_expense():
    view_expenses()
    if not expenses:
        return
    try:
        choice = int(input("Enter the number of the expense to delete: "))
        removed = expenses.pop(choice - 1)
        deleted_expenses.append(removed)
        save_expenses()
        print(f"Deleted: ₹{removed['amount']} | {removed['note']}\n")
        print("(You can restore this using 'Restore Last Deleted' in the menu)\n")
    except (ValueError, IndexError):
        print("Invalid number, nothing deleted.\n")

def restore_expense():
    if not deleted_expenses:
        print("No deleted expenses to restore.\n")
        return
    last = deleted_expenses.pop()   # take the most recently deleted one
    expenses.append(last)
    save_expenses()
    print(f"Restored: ₹{last['amount']} | {last['note']}\n")

print("=" * 40)
print("   Welcome to Expense Tracker")
print("=" * 40)
def main():
    while True:
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Spending")
        print("4. Filter by Category")
        print("5. Delete Expense")
        print("6. Restore Last Deleted")
        print("7. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_spending()
        elif choice == "4":
            filter_by_category()
        #elif choice == "5":
            #delete_expense()
        elif choice == "6":
            restore_expense()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.\n")

main()

