import argparse

def main():
    command, rest_words = user_prompt()
    run_command(command, rest_words)


def user_prompt():
    known_commands = {"add", "update", "delete", "list", "summary", "summary month", "help"}
    user = input("Please enter a command or enter help if assistance is needed: ")
    command, rest_words = extract_command(user, known_commands)
    return command, rest_words


def extract_command(user_input, known_commands):
    words = user_input.lower().split()
    if len(words) >= 2:
        two_word_command = f"{words[0]} {words[1]}"
        if two_word_command in known_commands:
            return two_word_command, words[2:]
    if len(words) >= 3:
        three_word_command = f"{words[0]} {words[1]} {words[2]}"
        if three_word_command in known_commands:
            return three_word_command, words[3:]
    return words[0], words[1:]

def run_command(command, rest_words):
    match command:
        case "add":
            sort_words(rest_words)
        case "update":
            pass
        case "delete":
            pass
        case "list":
            pass
        case "summary":
            pass
        case "summary month":
            pass
        case "help":
            pass


def sort_words(rest_words):
    parser = argparse.ArgumentParser(
        description= "Checks for description and amount of expense"
    )
    parser.add_argument("--description", type= str)
    parser.add_argument("--amount", type= float)
    print(parser)
    args = parser.parse_args()
    print(args)



##############################################################        
print("Welcome to Expense Tracker")
print(f"Here are a list of available commands:\n")
print(f"add\nupdate\ndelete\nlist\nsummary\nsummary month\nhelp")
parser = argparse.ArgumentParser(
        description= "Checks for description and amount of expense"
    )
parser.add_argument("-d", "--description", type= str, help="enter description")
parser.add_argument("-a", "--amount", type= int, help= "enter amount")

args = parser.parse_args()
print(args)
print("ran")
#while True:
    #main()