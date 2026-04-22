# Task 1 -> Store application log messages in a file

def write_log(message):
    with open("app.log", "a") as file:
        file.write(message + "\n")

# write_log("App Started")
# write_log("User logged in")
# write_log("App stopped")

# Task 2 -> Cleans email addresses and splits them into structured data
# (username and domain)

email = input("Enter email: ")

def clean_email(email):
    cl_email = email.strip().lower()
    if cl_email.count("@") != 1:
        print("Incorrect email")

    [username, domain] = cl_email.split("@")
    if not username or not domain:
        print("Incorrect email")
    else:
        print(f"Username: {username}")
        print(f"Domain: {domain}")

clean_email(email)

# Task 3 -> Check whether the password meets the minimum requirement of 8 char
password = input("Enter password: ")

def check_password(password):
    if len(password) < 8:
        print("Invalid Password")
    else:
        print("Valid Password")

check_password(password)



