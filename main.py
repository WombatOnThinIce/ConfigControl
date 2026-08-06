import json

from constants import *
from main_menu import main_menu
from project import Project


def main():

    active_project = Project()

    # Print welcome and menu
    print(f"Welcome to ConfigControl v{VERSION}")
    main_menu()

if __name__ == "__main__":
    main()
