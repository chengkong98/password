# Creating a Password to a new user
# Michael Lee - Fun Project - Create a new Username and a password

# 1. Create the variable that I would like on the password
# 2. Ensure that the password that is selected will match varables otherwise it will not work
# 3. Store that new password into a new file (likely a .txt file for this projects)
# 4. Re-call that file back when aske to enter the username and the product into a mimic log-in

# Create a variable equating to a list that will be and objective that is complete once satisfied
import random
import string
import time

f_name = input("Please input you first name: ")
l_name = input("Please input your last name: ")

def mail():
    mail_tld = ["@yahoomail.com", "@gmail.com", "@hotmail.com", "@aoL.com", "@protonmail.com", "@zoho.com", "@yandex.com", "@gmx.com" ]
    while True:
        email = input("Please input your preferred e-mail: ").lower()
        if any(email.endswith(tld) for tld in mail_tld):  # 'if any' refers to having any part of the input email entered. 'endswith()' allows for the list of proper tld's to be used at the end of the input
            print(f"welcome {f_name}! at {email} you are now in the system.")
            with open("email.txt", "a") as emailfile:
                emailfile.write(f"{f_name}, {l_name}, {email}\n")
            break
        else:
            print("please enter a valid email adddress")


class UsersInformation:
    def __init__(self):
        self.f_name = None
        self.l_name = None


    def first_last_name(self):
        with open("email.txt", "r") as emailfile:
            lines = emailfile.readlines()
            if lines:
                last_line = lines[-1].strip().split(",") # this line will read the last line in the txt.file
                if len(last_line) == 3:  # will check if the list has three criterias (i.e. f_name, l_name, email)
                    self.f_name, self.l_name, _ = last_line  # This takes only the first two options(i.e. f_name, l_name) from the email.txt file


    def username():
        choice = input("Would you like to use your first and last name as a default username? (y/n): ").lower()
        if choice == "y" or "yes":
            with open("email.txt", "r") as emailfile:
                first_last = emailfile.readlines()
                for names in first_last:
        if choice == "n" or "no":
            new_user = input("Please create a new username for your log-in: ")
            with open("username.txt", "a") as user:
                user.write(new_user + "\n")
            return new_user

# time.sleep(1)

# def ran_password():
#     lower_random = string.ascii_lowercase
#     upper_random = string.ascii_uppercase
#     special_random = string.punctuation
#     number_random = string.digits

#     random_password = [
#         random.choice(lower_random),
#         random.choice(upper_random),
#         random.choice(special_random),
#         random.choice(number_random)
#     ]

#     remaining_length = 12 - len(random_password)
#     random_password.extend(random.choice(lower_random + upper_random + special_random + number_random) for _ in range(remaining_length))

#     random.shuffle(random_password)

#     generate_random = ''.join(random_password)
#     print(f"Your generated random password is: '{generate_random}'")
#     return generate_random



# def identity():
#     choices = input("Would you like to generate a random password? (Yes/No): ").lower()

#     time.sleep(1)

#     if choices == "no":
#         print('''Create a new password that...
#         Contains at least 8 characters
#         Contains Lower case and Upper case
#         Contains A Special character (e.g, !@#$%^&*()-_+?/><|\=[])
#         Contains A Numbers''')

#         while True:
#             l, u, s, n = 0, 0, 0, 0
#             new_password = input("New Password: " )
#             lower_case = "abcdefghijklmnopqrstuvwxyz"
#             upper_case = lower_case.upper()
#             special_char = "!@#$%^&*()-_+?/><|\=[]"
#             numbers = "1234567890"

#             if len(new_password) >= 8:
#                 for satisfy in new_password:
#                     if satisfy in lower_case:
#                         l += 1
#                     if satisfy in upper_case:
#                         u += 1
#                     if satisfy in special_char:
#                         s +=1
#                     if satisfy in numbers:
#                         n += 1

#                 if l >= 1 and u >= 1 and s >= 1 and n >= 1 and len(new_password) == l + u + s + n:
#                     print("Password satisfies requirements")
#                     break
#                 else:
#                     print("That password does not meet the requirements please try again")

#         while True:
#             confirm_password = input("Re-enter your password to confirm it: ")
#             if new_password == confirm_password:
#                     print("Congratulations you created a new password")
#                     with open("passwords.txt", "a") as password_file:
#                         password_file.write(confirm_password + "\n")
#                     break
#             else:
#                 print("Wrong! try again")
#     elif choices == "yes":
#         with open("passwords.txt", "a") as password_file:
#             password_file.write(ran_password() + "\n")


# def associated(identity, username):
#     shared = []

mail()
username()
# identity()
