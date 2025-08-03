import parser

##############################################################        
print("Welcome to Expense Tracker")
print(f"Here are a list of available commands:\n")
print(f"add\nupdate\ndelete\nlist\nsummary\nsummary month\nhelp")
description = parser.run_parser()
print(description)