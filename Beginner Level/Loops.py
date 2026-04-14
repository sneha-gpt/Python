# Task 1 -> Print 7 Multiplication table in as it is format
# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# 7 x 4 = 28
# 7 x 5 = 35
# 7 x 6 = 42
# 7 x 7 = 49
# 7 x 8 = 56
# 7 x 9 = 63
# 7 x 10 = 70

for i in range(11):
    print(f"7 X {i} = {7*i}")

# Task 2 -> Print Star Pattern 
# *
# **
# ***
# ****
# *****
# ******

n = int(input("Enter number: "))

for i in range(1, n+1):
    print("*" * i)

# Task 3 -> Loop through a list of days and print only the working days, skipping the weekends

days = ["Mon", "Sat", "Tue", "Sun"]
weekends = ["sat", "sun"]

for day in days:
    if day.lower() in weekends:
        continue
    print(f"{day}")

# Task 4 -> Check if all files are CSV files

files = ["abc.csv", "xyz.txt", "pqr.csv"]
for file in files:
    if not file.endswith(".csv"):
        print("Not all files are CSV")
        break
else:
    print("All files are CSV")

# Task 5 -> Check whether any filname appears more than once

file_list = ['report.csv',
             'data.xlsx',
             'summary.docx',
             'report.csv',
             'data.csv']

for file in file_list:
    if file_list.count(file) > 1:
        print("Duplicate found")
        break
else:
    print("All files are unique")

# Task 6 -> WAP that kepps asking "Do you agree?" until the user types "yes"

answer = None
# while answer != "yes":
#     answer = input("Do you agree?(yes/no)")
# print("Thank you")

# Task 7 -> In  task 3 only max 3 attempts are allowed

attempt = 0
while attempt < 3:
    answer = input("Do you agree?(yes/no)")
    if(answer == "yes"):
        break
    attempt = attempt+1
else:
 print("3 Strikes, You are Out!!")
