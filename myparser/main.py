import parser
import sys
 
is_running = True
expenses = []

#while is_running == True:
print("Welcome to Expense Tracker")
print(f"Here are a list of available commands:\n")
print(f"add\nupdate\ndelete\nlist\nsummary\nsummary month\nhelp")
print(expenses)
if len(sys.argv) == 1:
    pass
else:
    print("this works!!")
    description = parser.run_parser()
    expenses.append(description)
user = input("Would you like to enter another command?(Yes/No): ")
if user.lower() == "yes":
    is_running = False
elif user.lower() == "no":
    is_running = True
    #break
else:
    print("command not valid")
