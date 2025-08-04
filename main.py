import argparse
import os
import csv

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
    with open(data_file, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["amount", "description"])
        if not file_exists or os.path.getsize(data_file) == 0:
            print("working")
            writer.writeheader()
        writer.writerow(expense)
        print("writer: ", writer)

def add_expense(args):
    expense = {
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

args = parser.parse_args()
print(args)
if args.command == "add":
    print(f"Adding item {(args.description)} with amount of {(args.amount)}")
    add_expense(args)
elif args.command == "list":
    list_expenses(args)
elif args.command == "clear":
    clear_csv()
else:
    parser.print_help()
