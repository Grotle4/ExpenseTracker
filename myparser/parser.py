import argparse

def run_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("command")
    parser.add_argument("--description")
    parser.add_argument("--amount")
    

    args = parser.parse_args()
    return args


if __name__ == "__main__":
    run_parser() 
