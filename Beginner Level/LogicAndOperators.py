# Task 1 -> Allow access only if the user is logged in or they are guest but they must not be banned.

is_logged_in = False
is_guest = True
is_banned = False

if (is_logged_in or is_guest) and not is_banned:
    print("Give access")
else:
    print("Denied access")

# Task 2 -> Validate that the domain is not on the banned list.

domain = "scam.com"
banned_list = ["scam.com", "fraud.com"]
if domain in banned_list:
    print(f"{domain} is banned.")
else:
    print(f"{domain} is authentic.")

# Task 3 -> Validate the email address it must be filled in and not empty.

email = None

if not email:
    print("Email is None or Empty.")
elif not email.strip():
    print("Email is empty.")
else:
    print(f"{email.strip()} is verified.")

# Task 4: Check if a user's name is not empty and the age is greater than or equal to 18

name = " Sneha "
age = 21

if not age or age < 18:
    print("Not eligible for vote")
elif not name:
    print("Name is either None or empty")
elif not name.strip():
    print("Name is empty.")
else:
    print(f"{name.strip()} is eligible to vote.")

# Task 5: Check if the password is at least 8 characters long and does not contain spaces

password = "asdfghj "

if not password or len(password) < 8 or len(password) != len(password.strip()):
    print("Password is not secure.")
else:
    print("Strong Password!!")
    
# Task 6: Check if a user’s email is not empty, contains '@', and ends with '.com'

user_email = "sneha@gmail.com"
if (not user_email) or ((user_email.count('@') != 1) or (not user_email.endswith(".com"))):
    print(f"{user_email} is not valid")
else:
    print(f"{user_email} is valid")

# Task 7: Check if a username is a string, is not None, and is longer than 5 characters

username = "heyy"
if (not username) or ((not isinstance(username, str)) or (len(username.strip()) <= 5)):
    print(f"{username} is Invalid")
else:
    print(f"{username} is valid")

# Task 8: Check if the user is either an admin or a moderator, and either they’re not banned or 
# they’ve verified their email

user_role = "Admin"
user_banned = False
email_verified = True
valid_roles = ["admin", "moderator"]

if ((user_role) and (email_verified)) and ((user_role.lower() in valid_roles) and (not user_banned)):
    print("Accepted")
else:
    print("Rejected")