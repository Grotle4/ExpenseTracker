import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--amount")
    parser.add_argument("-d", "--description")

    args = parser.parse_args()

main() 
