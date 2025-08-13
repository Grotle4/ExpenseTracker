# ExpenseTracker
To run this program, make sure current version of python is installed on your PC.

1. Open Command Prompt or Windows Powershell
2. Navigate to the directory that the python file is stored in(ie. User\Documents\Python\ExpenseTracker)
3. Run commmands through the command line by using the command "py main.py (command)"
4. To view list of commmands do py main.py -h

List of commands and usage(all commands are assumed to be run prior to entering py main.py on same line)

Add: add -d (description of expense) -a (amount of the expense) | Adds an expense alongside with the amount of the expense
List: list | Will list all added expenses alongside with date added and amount
Clear: clear | Will clear expense file of all expenses
Update: update -i(id value of expense) -d(new description of expense) -a (new amount of expense) | Will update an existing expense to a new description and/or amount, use list to find the id values of expenses
Delete: delete -i(id value of expense) | Will delete an expense, use list to find ID value of expense
Summary: summary | will give a total summary of the amount of expenses, use -m followed by the number of the month to search for total cost of expenses for only that month


