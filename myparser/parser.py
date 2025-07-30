import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--amount")
    parser.add_argument("--description")
    

    args = parser.parse_args()
    print("working")
    print(args)
    
def compare_command():
    pass


if __name__ == "__main__":
    main() 
