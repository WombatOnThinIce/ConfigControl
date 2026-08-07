from constants import *
from models import *


def main():

    projects = []
    active_project: int | None = None
    current_filepath = ""

    print()
    print(f"Welcome to ConfigControl v{VERSION}")

    while True:

        # Print welcome and menu
        print()
        if active_project == None:
            print("No project is currently loaded")
        else:
            print(f"{projects[active_project -1].proj_id} - {projects[active_project -1].name} is active")
        print("Select from the following options:")
        print()
        print("[1] OPEN EXISTING PROJECT")
        print("[2] CREATE NEW PROJECT")
        print("[3] CREATE NEW CONFIGURATION ITEM")
        print("[4] CREATE NEW VERSION OF CONFIGURATION ITEM")
        print("[5] CHANGE STATUS OF CONFIGURATION ITEM")
        print("[6] CREATE PROJECT BASELINE")
        print("[7] VIEW PROJECT SUMMARY")
        print()
        print("[s] SAVE CURRENT PROJECT")
        print("[q] QUIT WITHOUT SAVING")
        selection = input(">> ")

        if selection == "1":
            if len(projects) == 0:
                print("No stored projects")
                continue
            print("Choose a project:")
            for i, project in enumerate(projects):
                print(f"[{i}] {project.proj_id} - {project.name}")
            print("[b] Back to menu")
            selection = input(">>")
            if selection == "b":
                continue
            ## NEED TO COMPLETE

        elif selection == "2":
            print("CREATE A NEW PROJECT")
            new_name = input("Enter project name >> ")
            new_number = len(projects) + 1
            projects.append(Project(new_name, new_number))
            print(f"Your new project {projects[new_number -1].proj_id} - {projects[new_number -1].name} has been added")
            print("Would you like to make it the active project? (y/n)")
            selection = input(">>")
            if selection == "y":
                active_project = new_number
            elif selection == "n":
                continue
            else:
                print("Invalid entry. Project not made active")

        elif selection == "3":
            if active_project == None:
                print("No project is active. Select a project and try again.")
                continue
            print(f"CREATE A NEW CONFIGURATION ITEM IN {projects[active_project -1].proj_id} - {projects[active_project -1].name}")
            print("Select a configuration item type. Must be:")
            for type in CI_TYPES:
                print(f"    {type}")
            new_type = (">>")
            if new_type not in CI_TYPES:
                print("Invalid type. Try again")
                continue
            new_name = input("Enter CI title >>")


        elif selection == "q":
            break

        else:
            print("Enter one of the displayed options and try again")

if __name__ == "__main__":
    main()
