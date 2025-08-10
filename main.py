import argparse
import os
import csv
import datetime

current_date = datetime.date.today()


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
        writer = csv.DictWriter(f, fieldnames=["ID", "date", "amount", "description"])
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
        "date": current_date,
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
        print(f"{idx}: {exp["description"]} Date: {exp["date"]} Amount: {exp["amount"]}")

def clear_csv():
    with open(data_file, "w") as f:
        pass

def update_expense(args):
    amount_found = None
    description_found = None
    with open(data_file, "r+") as f:
        reader = csv.reader(f)
        list_reader = list(reader)
        for row in list_reader:
            print(row)
            if row[0].startswith(str(args.id)):
                if args.amount:
                    row[1] = args.amount
                    amount_found = True
                if args.description:
                    row[2] = args.description
                    description_found = True
                update_message(row[0],row[1],row[2], amount_found, description_found)
                break
        clean(data_file, list_reader)

def delete_expense(args):
    found_lists = []
    row_list = []
    iteration = 0
    found_error = False
    with open(data_file, "r+") as f:
        reader = csv.reader(f)
        list_reader = list(reader)
        print("l:", list_reader)
        try:
            for row in list_reader:
                row_list.append(row[0])
            for row in list_reader:
                if str(args.id) not in row_list:
                    found_error = True
                    print(row_list)
                    print("doesnt exist")
                    clean(data_file,list_reader)
                    break
                if not row[0].startswith(str(args.id)):
                    if row[0].startswith("ID"):
                        print("id found")
                        found_lists.append(row)
                        continue
                    iteration += 1
                    print("found it: ", iteration)
                    row[0] = iteration
                    found_lists.append(row)
        except IndexError:
            pass
        if found_error == False:
            clean(data_file, found_lists)
                

def summary_expense(args):
    expense_list = []
    with open(data_file, "r+") as f:
        reader = csv.reader(f)
        list_reader = list(reader)
        if not args.month:
            try:
                for row in list_reader[1:]:
                    expense_list.append(row[2])
                float_list = [float(item) for item in expense_list]
                total_sum = sum(float_list)
                print(total_sum)
            except IndexError:
                pass
        else:
            summary_month_expense(args)

def summary_month_expense(args):
    expense_list = []
    with open(data_file, "r+") as f:
        reader = csv.reader(f)
        list_reader = list(reader)
        try:
            for row in list_reader[1:]:
                date_string = row[1]
                date_object = datetime.datetime.strptime(date_string, "%Y-%m-%d")
                month = date_object.strftime("%m")
                if month.startswith("0"):
                    month = month[1:]
                print("args: ", args.month)
                if int(month) == args.month:
                    expense_list.append(row[2])
            float_list = [float(item) for item in expense_list]
            total_sum = sum(float_list)
            print(total_sum)
        except IndexError:
            pass
                
        
def update_message(id, new_amount, new_description, amount_found, description_found):
    if amount_found and description_found is None:
        print(f"Updating ID {id} with new amount: {new_amount}")
    elif description_found and amount_found is None:
        print(f"Updating ID {id} with new description: {new_description}")
    elif amount_found and description_found:
        print(f"Updating ID {id} with new amount({new_amount}) and new description({new_description})")
    


def clean(data_file, list_reader):
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
update_parser.add_argument("-d", "--description",type= str , help="Description for the expense")
update_parser.add_argument("-a", "--amount", type= float, help="Amount of money for the expense")

delete_parser = subparsers.add_parser("delete", help="Delete existing expense")
delete_parser.add_argument("-i", "--id", type= int, help="ID number for expense you want to update, use list to view id numbers")

summary_parser = subparsers.add_parser("summary", help="Will add all of your funds together to show total expenses")
summary_parser.add_argument("-m", "--month", type=int, required=False, help="Enter the month number you would like to view expenses for(ex. August is 8)")


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
elif args.command == "delete":
    delete_expense(args)
elif args.command == "summary":
    summary_expense(args)
else:
    parser.print_help()
