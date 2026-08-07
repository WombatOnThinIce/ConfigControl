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
        print("[s] SAVE ALL")
        print("[q] QUIT WITHOUT SAVING")
        selection = input(">> ")

        if selection == "1":
            if len(projects) == 0:
                print("No stored projects")
                continue
            print("Choose a project:")
            for i, project in enumerate(projects):
                print(f"[{i + 1}] {project.proj_id} - {project.name}")
            print("[b] Back to menu")
            selection = input(">>")
            if selection == "b":
                continue
            if int(selection) > 0 and int(selection) <= len(projects):
                active_project = int(selection)
            else:
                print("invalid entry")

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
            new_type = input(">>")
            if new_type not in CI_TYPES:
                print("Invalid type. Try again")
                continue
            new_name = input("Enter CI title >>")
            notes = input("Enter any CI creation notes >>")
            new_ci = projects[active_project -1].add_new_ci(new_type, new_name, notes)
            print(f"New CI has been added {new_ci.ci_id} - {new_ci.name}")

        elif selection == "4":
            if active_project == None:
                print("No project is active. Select a project and try again.")
                continue
            print(f"CREATE A NEW VERSION OF AN EXISTING CONFIGURATION ITEM IN {projects[active_project -1].proj_id} - {projects[active_project -1].name}")
            print("Select an existing CI:")
            for i, ci in enumerate(projects[active_project -1].cis):
                print(f"[{i}] {ci.ci_id} - {ci.name} - v{ci.versions[-1].version}")
            print("[b] Back to menu")
            selection = input(">> ")
            if selection == "b":
                continue
            if int(selection) > 0 and int(selection) <= len(projects[active_project -1].cis):
                notes = input("Enter new version comment >> ")
                new_version = projects[active_project -1].cis[int(selection) - 1].add_new_version(notes)
                print(f"You have added version {new_version.version} of {projects[active_project -1].cis[int(selection) - 1].ci_id}")
            else:
                print("invalid entry")


        elif selection =="s":
            pass

        elif selection == "q":
            break

        else:
            print("Enter one of the displayed options and try again")

if __name__ == "__main__":
    main()
