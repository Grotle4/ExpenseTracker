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

def update_expense(args):
    with open(data_file, "r+") as f:
        reader = csv.reader(f)
        list_reader = list(reader)
        for row in list_reader:
            print(row)
            if row[0].startswith(str(args.id)):
                if args.new_amount:
                    row[1] = args.new_amount
                if args.new_description:
                    row[2] = args.new_description
                print(f"Updated ID {row[0]} with new values")
                break
        clean(data_file, list_reader)
        

def clean(file, list_reader):
    with open (data_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(list_reader)


parser = argparse.ArgumentParser(description="Parse user input over multiple command lines")

subparsers = parser.add_subparsers(dest="command", help="Available commands")
args_list = []

add_parser = subparsers.add_parser("add", help= "Add new item to list")
add_parser.add_argument("-d", "--description",type= str, required=True, help="Description for the expense")
add_parser.add_argument("-a", "--amount", type= float, required=True, help="Amount of money for the expense")

list_parser = subparsers.add_parser("list", help="Lists all expenses")

clear_parser = subparsers.add_parser("clear", help= "Clears list of expenses")

update_parser = subparsers.add_parser("update", help="Update existing parser")
update_parser.add_argument("-i", "--id", type= int, help="ID number for expense you want to update, use list to view id numbers")
update_parser.add_argument("-nd", "--new_description",type= str , help="Description for the expense")
update_parser.add_argument("-na", "--new_amount", type= float, help="Amount of money for the expense")

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
    update_expense(args)
else:
    parser.print_help()
