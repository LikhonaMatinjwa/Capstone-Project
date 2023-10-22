# Create a task management program for a small business.
# The user should be able to log in using a username and password.
# Display a menu of options once the user has logged in.
# Format the program to only allow admin to register users.
# Add a statistics section for admin only.

from datetime import date

login_details = {}  # Stores username and password

# Read login details from the file and populate the dictionary
with open("user.txt", "r") as file:
    for line in file:
        name, password = line.strip().split(",")
        login_details[name] = password

# Set username and password attempts to be equal 3
# when the user enters an incorrect name or password.
user_attempts = 3
password_attempts = 3

# Login in section
while user_attempts > 0:
    user_name = input("Enter username:").lower()

    if user_name in login_details:
        stored_password = login_details[user_name]

        while password_attempts > 0:
            user_password = input("Enter password:")

            if user_password == stored_password.strip():
                print("You have successfully logged in")
                break  # Exit the password loop when the password is correct
            else:
                password_attempts -= 1
                print(f"Incorrect password. {password_attempts} attempts left.")

        else:
            print("Max password attempts reached. Access denied.")

        # Exit the username loop when access is granted or attempts are exhausted.
        break

    else:
        user_attempts -= 1
        print(f"User not found. {user_attempts} attempts left.")

if user_attempts == 0:
    print("Max user attempts reached. Access denied.")

while True:

    # Present the menu to the user and
    # present a different menu for admin.
    if user_name == "admin":

        menu = input("Select one of the following options:\n"
                     "r - register a user\n"
                     "a - add task\n"
                     "va - view all tasks\n"
                     "vm - view my tasks\n"
                     "s - view statistics\n"
                     "e - exit\n"
                     ": ").lower()
    else:
        menu = input("Select one of the following options:\n"
                     "a - add task\n"
                     "va - view all tasks\n"
                     "vm - view my tasks\n"
                     "e - exit\n"
                     ": ").lower()

    # Registration menu, only shows for the admin.
    if menu == 'r':

        new_password_attempts = 3
        new_user_name = input("Enter new user name:").lower()
        new_user_password = input("Enter new user password:")

        while new_password_attempts > 0:
            confirm_new_password = input("Confirm password:")

            if confirm_new_password == new_user_password:
                with open("user.txt", "a") as file:
                    file.write("\n"+new_user_name + ", " + confirm_new_password)
                    print(f"{new_user_name} was successfully added.")
                break
            else:
                new_password_attempts -= 1
                print(f"Incorrect password. {new_password_attempts} attempts left.")

            break
        if new_password_attempts == 0:
            print("Max password attempts reached. Please try again.")

        break
        pass

    # Adding a new task section.
    elif menu == 'a':

        person_responsible = input("Enter the username of"
                                   " the person whom the"
                                   "task was assigned to:").lower()
        task_title = input("Provide the title of the task:")
        task_description = input("Provide task description:")
        due_date = input("Provide the due date for the task:")

        with open("tasks.txt", "a") as file:
            file.write("\n" + person_responsible + ", " + task_title +
                       ", " + task_description + ", " + str(date.today()) +
                       ", " + due_date + ", " + "No")

            print(f"New task was assigned to {person_responsible}")

        break
        pass

    # Reads all the tasks in task.txt and prints them out
    elif menu == 'va':

        with open("tasks.txt", "r") as file:
            for line in file:
                my_lines = line.split(",")

                print(f"Task:               {my_lines[1]}\n"
                      f"Assigned to:         {my_lines[0]}\n"
                      f"Date assigned:      {my_lines[3]}\n"
                      f"Due date:           {my_lines[4]}\n"
                      f"Task complete?       {my_lines[5].strip()}\n"
                      f"Task description:   \n{my_lines[2]}\n")

        break

        pass

    # Reads tasks for the user that logged in.
    elif menu == 'vm':

        with open("tasks.txt", "r") as file:

            for line in file:
                my_name = line.strip().split(",")

                if user_name == my_name[0]:
                    print(f"Task:               {my_name[1]}\n"
                          f"Assigned to:         {my_name[0]}\n"
                          f"Date assigned:      {my_name[3]}\n"
                          f"Due date:           {my_name[4]}\n"
                          f"Task complete?       {my_name[5].strip()}\n"
                          f"Task description:   \n{my_name[2]}\n")
        break
        pass

    # Statistics section for admin only.
    elif menu == "s":

        with open("tasks.txt", "r") as file:
            number_of_tasks = len(file.readlines())
            print(f"Number of tasks: {number_of_tasks}")
        with open("user.txt", "r") as file:
            number_of_users = len(file.readlines())
            print(f"Number of users: {number_of_users}")

        break
        pass

    # Exits the menu.
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made entered an invalid input. Please try again")
