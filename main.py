import random
import string
import csv

def create_password(number_of_characters, character_list):
    password_character_list = []
    count = number_of_characters
    while count > 0:
        random_character = random.choice(character_list)
        password_character_list.append(random_character)
        count -= 1
    
    completed_password = ''.join(password_character_list)
    return completed_password

quit = False
while quit == False:
    print("\n\nWelcome to Pythword, the Python Password Manager!")

    menu_selection = input("""\nPlease enter a selection:
    1: Create a new password
    2: Find a saved password
    3: Quit

    Choice: 
    """)

    if menu_selection == "1":
        character_list = []
        password_makeup = input("""\nWhat would you like to include in your password?
        1: Characters only
        2: Characters and numbers
        3: Characters, numbers, and punctuation

        Choice: 
        """)
        if password_makeup == "1":
            character_list = string.ascii_letters
        elif password_makeup == "2":
            character_list = string.ascii_letters + string.digits
        elif password_makeup == "3":
            character_list = string.ascii_letters + string.digits + string.punctuation
        
        website = input("What is the name of the website? ")
        username = input("What is the username? ")
        number_of_characters = int(input("How many characters for the password? "))
        password = create_password(number_of_characters, character_list)
        print("Site: " + website)
        print("Name: " + username)
        print("Password: " + password)
        # open the file in the write mode
        password_file = open(r'C:\Users\Jesse\Desktop\Python\Pythword\passwords.csv', 'a', newline='\n')

        # create the csv writer
        writer = csv.writer(password_file)

        # create the fields to be inserted
        fields = [website, username, password]

        # write a row to the csv file
        writer.writerow(fields)

        # close the file
        password_file.close()
    
    elif menu_selection == "2":
        website = input("\nWhat is the name of the website? ")
        passwords_csv = csv.reader(open('passwords.csv', "r"), delimiter=",")
        #loop through the csv list
        for row in passwords_csv:
            if website == row[0]:
                print("\nSite: " + row[0])
                print("User: " + row[1])
                print("Password: " + row[2])

    elif menu_selection == "3":
        quit = True

