from constants import *
from models import Project


def main():

    active_project: Project() | None = None
    current_filepath = ""

    while True:

    # Print welcome and menu
        print(f"Welcome to ConfigControl v{VERSION}")
        if active_project == None:
            print()
            print("No project is loaded")
            print("Select from the following options:")
            print()
            print("[1] OPEN EXISTING PROJECT")
            print("[2] CREATE NEW PROJECT")
            print()
            selection = input(">> ")

        else:
            pass

        if selection == "q":
            break

if __name__ == "__main__":
    main()
