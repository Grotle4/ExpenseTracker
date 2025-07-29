def main():
    print("Welcome to Expense Tracker")
    print(f"Here are a list of available commands:\n")
    print(f"add\nupdate\ndelete\nlist\nsummary\nsummary month\nhelp")
    while True:
        if not user_prompt():
            break
        

def user_prompt():
    user = input("Please enter a command or enter help if assistance is needed: ")
    return False

main()