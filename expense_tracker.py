import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"

def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])

def add_expense():
    category = input("Enter Category: ")
    amount = float(input("Enter Amount: "))
    description = input("Enter Description: ")

    date = datetime.now().strftime("%d-%m-%Y")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])

    print("Expense Added Successfully!")

def view_expenses():
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        print("\n===== ALL EXPENSES =====\n")

        for row in reader:
            print(row)

def total_expenses():
    total = 0

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            total += float(row["Amount"])

    print(f"\nTotal Expenses: ₹{total}")

def search_category():
    category = input("Enter Category to Search: ")

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        print("\nMatching Expenses:\n")

        found = False

        for row in reader:
            if row["Category"].lower() == category.lower():
                print(row)
                found = True

        if not found:
            print("No expenses found.")

def main():
    initialize_file()

    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Search By Category")
        print("5. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            total_expenses()

        elif choice == "4":
            search_category()

        elif choice == "5":
            print("Thank You For Using Expense Tracker!")
            break

        else:
            print("Invalid Choice!")

if __name__ == "__main__":
    main()