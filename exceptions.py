# Try Except Blocks
try:
    age = int(input("Please type your age: "))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print(" Age cannot be zero")    
except ValueError:
    print("Invalid value, Try again")