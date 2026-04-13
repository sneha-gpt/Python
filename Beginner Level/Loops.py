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