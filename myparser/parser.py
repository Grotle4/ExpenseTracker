import argparse
print("this is going first")

def run_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("command")
    parser.add_argument("--description")
    parser.add_argument("--amount")

    args = parser.parse_args()
    final_args = get_parse(args)
    return final_args


def get_parse(args):
        if args.command == "add":
            if args.description:
                if args.amount:
                    return args
                else:
                    missing_key("amount")
            else:
                missing_key("description")


def missing_key(text):
    print(f"missing {text}, add {text} using --{text} if you would like to add an expense")


final_args = run_parser()
print(final_args)

