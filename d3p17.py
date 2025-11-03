#Write a Python program to manage student information using a dictionary.

#The program should allow the user to:
#Add a student by entering their ID and Name.
#Search for a student by ID and display their name if found.
#View all students in the system.
#Exit the program.
students = {} 
while True:
    print("\n1. Add Student")
    print("\n2. View Student")
    print("\n3. Exit")

    choice=input("\nEnter the choice: ")

    if choice == '1':
        sid = input("Enter the ID: ")
        name = input("Enter the name: ")
        students[sid] = name
        print("student added!😍")

    elif choice == '2':
        for sid,name in students.items():
            print(f"ID:{sid}, name:{name}")
    elif choice == '3':
        print("good bye!😁")
    else:
        print("Invalid number🙂")
        break