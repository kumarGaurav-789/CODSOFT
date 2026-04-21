import csv
from datetime import datetime
import os

# File name
FILE_NAME = "expenses.csv"

# Allowed categories
CATEGORIES = ["Food", "Travel", "Grocery", "FD", "Rent"]

# Create file if not exists
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Amount", "Category", "Date"])


# Add Expense
def add_expense():
    try:
        amount = float(input("Enter amount: "))

        print("\nSelect Category:")
        for i, cat in enumerate(CATEGORIES, start=1):
            print(f"{i}. {cat}")

        choice = int(input("Enter category number: "))
        category = CATEGORIES[choice - 1]

        date = datetime.now().strftime("%Y-%m-%d")

        with open(FILE_NAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([amount, category, date])

        print("✅ Expense added successfully!")

    except:
        print("❌ Invalid input! Try again.")


# View Expenses
def view_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            print("\nAmount | Category | Date")
            print("-" * 35)
            next(reader)
            for row in reader:
                print(f"{row[0]} | {row[1]} | {row[2]}")
    except:
        print("❌ No data found!")


# Total Expense
def total_expense():
    total = 0
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                total += float(row[0])

        print("💰 Total Expense:", total)

    except:
        print("❌ No data found!")


# Category-wise Expense
def category_expense():
    data = {}
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                category = row[1]
                amount = float(row[0])

                if category in data:
                    data[category] += amount
                else:
                    data[category] = amount

        print("\n📊 Category-wise Expense:")
        for cat, amt in data.items():
            print(cat, ":", amt)

    except:
        print("❌ No data found!")


# Main Menu
def main():
    while True:
        print("\n==== Expense Tracker ====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Category-wise Expense")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expense()
        elif choice == "4":
            category_expense()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("❌ Invalid choice!")


# Run program
if __name__ == "__main__":
    main()