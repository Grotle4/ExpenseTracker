import argparse
import os
import csv
import pandas as pd

data_file = "expenses.csv"


def load_expenses():
    expenses = []
    if os.path.exists(data_file):
        with open(data_file, newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                expenses.append(row)
    return expenses

def save_expense(expense):
    file_exists = os.path.exists(data_file)
    with open(data_file, "r+", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["ID", "amount", "description"])
        data = list(csv.reader(f))
        rows = len(data)
        expense["ID"] = rows
        if not file_exists or os.path.getsize(data_file) == 0:
            writer.writeheader()
            expense["ID"] = 1
        writer.writerow(expense)
        
        

def add_expense(args):
    expense = {
        "ID": None,
        "amount": args.amount,
        "description": "".join(args.description)
    }
    save_expense(expense)

def list_expenses(args):
    expenses = load_expenses()
    if not expenses:
        print("No expenses found")
        return
    for idx, exp in enumerate(expenses, 1):
        print(f"{idx}. {exp["amount"]} - ({exp["description"]})")

def clear_csv():
    with open(data_file, "w") as f:
        pass

parser = argparse.ArgumentParser(description="Parse user input over multiple command lines")

subparsers = parser.add_subparsers(dest="command", help="Available commands")
args_list = []

add_parser = subparsers.add_parser("add", help= "Add new item to list")
add_parser.add_argument("-d", "--description",type= str, required=True, help="Description for the expense")
add_parser.add_argument("-a", "--amount", type= float, required=True, help="Amount of money for the expense")

list_parser = subparsers.add_parser("list", help="Lists all expenses")

clear_parser = subparsers.add_parser("clear", help= "Clears list of expenses")

update_parser = subparsers.add_parser("update", help="Update existing parser")
add_parser.add_argument("-nd", "--new description",type= str , help="Description for the expense")
add_parser.add_argument("-na", "--new amount", type= float, help="Amount of money for the expense")

args = parser.parse_args()
print(args)
if args.command == "add":
    print(f"Adding item {(args.description)} with amount of {(args.amount)}")
    add_expense(args)
elif args.command == "list":
    list_expenses(args)
elif args.command == "clear":
    clear_csv()
elif args.command == "update":
    pass
else:
    parser.print_help()
