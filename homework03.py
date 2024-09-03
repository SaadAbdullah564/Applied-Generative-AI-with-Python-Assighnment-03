#Write a python program to check whether a number is odd aur even
num:int = int(input("Enter a Number: "))
if num % 2 == 0:
    print("Number is Even")
else :
    print("Number is Odd")

#Write a python program too find if a person is elligeble to vote aur note first get his nationality
age:int = int(input("Enter your age: "))
nationality:str = str(input("Enter your Nationality: "))
if age > 18  and nationality=="pakistani" : 
    print("You are  elligeble too cast vote ")
else : 
    print("Please obtain a valid ID too cast vote")


#write a python program too check who are the categary of citizens according to their age
age:int = int(input("Enter your age: "))
if age > 1 and age < 13:
    print("You are  a child")
elif age > 12 and age < 20:
    print("You are a Teenager ")
elif age > 20 and age < 60: 
    print("You are a Adult")
else : 
    print("You are a Senoir Citizen")


#Write a python progarm to find the number of dayz in different months 
monthNumber:int = int(input("Enter the number of Month: "))
if monthNumber == 1:
    print("31 Dayz")
elif monthNumber == 2:
    print("28 Dayz")
elif monthNumber == 3:
    print("31 Dayz")
elif monthNumber == 4:
    print("30 Dayz")
elif monthNumber == 5:
    print("31 Dayz")
elif monthNumber == 6:
    print("30 Dayz")
elif monthNumber == 7:
    print("31 Dayz")
elif monthNumber == 8:
    print("31 Dayz")
elif monthNumber == 9:
    print("30 Dayz")
elif monthNumber == 10:
    print("31 Dayz")
elif monthNumber == 11:
    print("30 Dayz")
elif monthNumber == 12:
    print("31 Dayz")


#Write a python program too find whether an year is leap or not
dayOfFeburary:int = int(input("Enter the number of dayz: "))
if dayOfFeburary == 29:
    print("It is a Leap year")
else : 
    print("It is not a Leap Year")



#Write a python program to find if a number is positive and negitive ur zero
num:int = int(input("Enter the num: "))
if num < 0:
    print("Num is Negitive")
elif num > 0:
    print("Num is Positive")
elif num == 0:
    print("The Number is itself Zero")



#Write a python program to check a number is divisible by 2 and 3 aur by none of them
num:int = int(input("Enter the Number: "))
if num % 2 == 0 :
    print("Num is Divisible by 2")
elif num % 3 == 0:
    print("Num is Divisible by 3")
elif num % 2 != 0 and num % 3 != 0:
    print("Num is not  Divisible by Both")