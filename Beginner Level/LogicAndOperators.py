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
