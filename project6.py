import os
from datetime import datetime

file = "journal.txt"

print("Welcome to personal journal manager!")

print("\n please select an option:")
print("1. Add a New Entyry")
print("2. View All Entries")
print("3. Search for an Entry")
print("4. Delete all Entries")
print("5. Exit")

while True:

    choice = input("\nEnter Your Choice:")

    if choice == "1":

        entry = input("\nEntyer Your journal entry:")
        date = datetime.now().strftime("%d-%m-%y %H:%M:%S")

        with open(file, "a") as f:
            f.write("[" + date + "]\n")
            f.write(entry + "\n")

        print("\nEntry added successfully!")

    elif choice == "2":

        print("\nYour Journal Entries:")
        print("----------------------------")

        try:
            with open("journal.txt", "r") as f:
                entries = f.read()

            print(entries)

        except FileNotFoundError:
           
            print("No journal entries found.start by adding a new entry!")

    elif choice == "3":

        keyword = input("\nEnter a keyword or date to search:")

        if os.path.exists(file):

            with open(file, "r") as f:
                dat = f.read()

            if keyword.lower() in dat.lower():
                print("\nMatching Entries:")
                print("------------------------------")
                print(dat)

            else:
                print("\nNo entries were found for the keyword:", keyword)

        else:
            print("\nNo entries were found for the keyword:", keyword)


    elif choice == "4":

        if os.path.exists(file):

            answer = input("\nAre you sure you want to delete all entries? (yes/NO):")

            if answer.lower() == "yes":
                os.remove(file)

                print("\noutput:")
                print("all journal entries have been deleted.")

            else:
                print("\nDelete operation cancelled:")

        else:
            print("output:")
            print("No journal entries to delete.")

    elif choice == "5":

        print("\noutput:")
        print("Thank you for using personal journal manager. Goodbye!")
        break

    else:

        print("\noutput:")
        print("Invalid option. please select a valid option from the menu.")
