#number = int(input("Enter a number:"))
#is_odd = number % 2 != 0
#print("Number is odd:", is_odd)

#2.
#age = int(input("Enter your age:"))
#age_in_days = age * 365
#print("Years = ", age_in_days, "days.")

#3.
#minutes = int(input("Enter minutes: "))
#hours = minutes / 60
#remaining_minutes = minutes % 60
#print(f'{minutes} is {int(hours)} Hours and {remaining_minutes} Minutes')

#4.
#integer = int(input("Enter integers: "))
#last_digit = integer % 10
#print("Last digit of the number is:", last_digit)

#5.
# role = input("Enter your role: ")
# age = int(input("Enter your age: "))
# print("Eligible :", role == "student" and age >= 21)

# #6.
# a = int(input("Enter A number: "))
# b = int(input("Enter B number: "))
# print("Before swap : a=",a,"b =",b)
# a = a + b
# b = a - b
# a = a - b
# print("After Swap : a=",a,"b =",b)

#7.
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to drive.")
else:
    print("You are not eligible to drive.")