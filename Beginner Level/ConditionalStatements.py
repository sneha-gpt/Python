# Task 1 ->  Validate the Quality and Correctness of Email Values
# Must not be empty
# Must contain '.' and '@'
# Must contain exactly one '@' symbol
# Must end with '.com', '.org', or '.net'
# Must not be longer than 254 characters
# Must start and end with a letter or digit

def is_valid_email(email):
    if not email:
        return False
    if "@" not in email or "." not in email or email.count("@") != 1:
        return False
    if (not email.endswith(".com")) and (not email.endswith(".org")) and (not email.endswith(".net")):
        return False
    if len(email) > 254:
        return False
    if (not email[0].isalnum()) or (not email[-1].isalnum()):
        return False
    return True

emails = ["sneha@gmail.com", 
          None, 
          "sneha", 
          "sneha.",
          "sneha@",
          "#sneha",
          ""]

passwords = ["abc", 
             None,
             "", 
             "  as   ", 
             "12", 
             "123456789",
             "asd12345"]

# for email in emails:
#     print(f"{email} is {is_valid_email(email)}")


# Task 2 -> Validate the Quality and Correctness of Passwords
# Must not be empty
# Must be at least 8 characters
# Must include at least 1 uppercase
# Must include at least 1 lowercase
# Must not be same as the email
# Must not contain any spaces
# Must start and end with a letter or digit

def is_valid_password(password, email):
    if not password:
        return False
    if len(password) < 8:
        return False
    if (not any(c.isLower() for c in password)) or (not any(c.isUpper() for c in password)):
        return False
    if password == email:
        return False
    if " " in password:
        return False
    if (not password[0].isalnum()) or (not password[-1].isalnum()):
        return False
    else:
        return True
    
for i in range(len(emails)):
    if not is_valid_email(emails[i]):
        print(f"{emails[i]} is not valid email.")
    elif not is_valid_password(passwords[i], emails[i]):
        print(f"{passwords[i]} is not valid password.")
    