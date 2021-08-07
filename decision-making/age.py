age = int(input("Enter your age: "))
if age > 0 and age < 16:
    print("Child")
elif age >= 16 and age <= 100:
    print("Adult")
else:
    print("Invalid data")

