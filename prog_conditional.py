# #1.Enter a number to check if it's positive or negative:

# num = float(input("enter a value of number:"))
# if num > 0:
    # print("+ve number")
# elif num ==0:
    # print("zero")
# else:
    # print(f"{num} is negative")
    
# #2.age should be major ,minor and senior
# age = int(input("enter age:"))
# if age < 18:
    # result = "minor"
# elif age < 60:
    # result = "senior"
# else:
    # "adult"
    
    
# print(f" The age category you entered is {result}.")


# #3.numeric to check if it is a leap year
# year = int(input("enter a year :"))
# if (year %4 ==0 and year %100!=0) or (year %400 ==0):
    # print(year,"leap year")
    
# else:
    # print(year,"not leap year .")

# #4.enter a number to check its Even or Odd.
# num = int(input("enter a number:"))
# if num %2 ==0:
    # print("even number")
# else:
    # print("odd number")
    
    
# #5.grade_percentage
# grade = int(input("enter a perchange:"))
# if grade > 90 :
    # result ="grade a"
# elif grade >= 70:
    # result = "grade b"
# elif grade >=60:
    # result = "grade c"
# elif grade >= 40:
    # result = "grade d"
# else:
    # result = "grade E"

# print(f" you got good {result}")   


# #6.largest number
# num1 = int(input("enter num1"))
# num2 = int(input("enter num2"))
# if num1 > num2 :
    # res = num1
# else:
    # res = num2
    
# print(f"largest number is {res}")

# #7.largest number among three number.
# num1 = float(input("enter the 1st number:num1."))
# num2 = float(input("enter the 2nd number:num2."))
# num3 = float(input("enter the 3rd number:num3."))
# if num1 == num2 == num3:
    # print("all numbers are equal")
# elif num1 == num2:
    # if num1 > num3:
        # print(f"{num1} and {num2} are equal and larger than {num3}")
    # else:
        # print(f"{num3} are largest")
# elif num1 == num3:
    # if num1 > num2:
        # print(f"{num1} and {num3} are equal and larger than {num2} ")
    # else:
        # print(f"{num2} is larger")
        
# elif num2 == num3:
    # if num2 >num1:
        
        # print(f"{num2} and {num3} are equal and larger than {num1}")
    # else:
        # print(f"{num1} is larger")
        
# else:
    # if num1 > num2 and num1 >num3:
        # print(f"{num1} is largest")
    # elif num2 > num1 and num2 > num3:
        # print(f"{num2} is larger")
    # else:
        # print(f"{num3} is largest")
        




# #8.check wheather its palindrome or not

# value = []
# while True:
    # data = input("Enter a word to check if it's a palindrome or not (type 'x' to exit): ")
    # if data.lower() == "x":
        # break
    # else:
        # value.append(data)
 
# result = []      
# for val in value:
       # reverse = val[::-1]
       # result.append("It's Palindrome." if reverse == val else "It's not Palindrome.")
       
       
#9. #Formula to check valid triangle 
     # a + b > c
     # a + c > b
     # b + c > a
     
# side1 =float(input("enter side1 number:"))
# side2 = float(input("enter side2 number:"))
# side3 =float(input("enter side3 number:"))

# if (side1+side2 > side3) and  (side1+side3 > side2) and  (side2+side3 > side1):
    # print("3 sides froms triangle")
# else:
     # print("3 sides can not from triangle")
     
     
#10.enter a character to check if it's a vowel or consonant:
# alphabet = input("enter a alphabet ")
# if len(alphabet) == 1:
    # if alphabet.lower() in 'aeiou':
        # print("its vowels")
    # else:
        # print("its constant")
# else:
    # print("enter a single charactor")
    
# a =input("nter a alphabet")
# if len(a) ==1:
    # if (a.lower() in 'aeiou') and (a.upper() in 'AEIOU'):
        # print("its vowel")
    # # else:
        # # print("its constant")
# # else:
    # # print("enter a single charator")
    
    
# #11.multiple of both 3 and 5.
# num = int(input("enter number"))
# if(num%3 ==0) and (num%5) == 0:
    # print(f"{num} is multiple by 3 and 5")
# else:
    # print(f"{num} is not multiplied by 3 n 5")
    
# #12.Enter the temperature in Celsius
# # temp = float(input("enter a temperature in celsius:"))

# # if temp >= 30:
    # # print("its a hot.")
# # elif temp <=15 and temp<30:
    # # print("its moderate")
# # else:
    # # print("its cold")
    
    
# # #13.perform add ,sub,mul and div operation.

# operator = ["+","-","*","/"]
# choose_operator =input("select an operator:")

# if choose_operator in operator:
    # n1 = int(input("enter number n1:"))
    # n2 = int(input("enter number n2:"))
    # if choose_operator == "+":
        # result = n1 + n2
    # elif choose_operator == "-":
        # result = n1 - n2
    # elif choose_operator =="*":
        # result = n1 *n2
    # elif choose_operator =="/":
        # if num2 !=0:
            # result = num1 /num2
        # else:
            # result= "Undefined (cannot divide by zero)"
            
    # print("Result:", result)
# else:
    # print("Not a valid option.")
    

# #14.
# year = int(input("enter a leap year:"))
# if year %100 ==0:
    # if year %400 ==0:
        # print("its century leap year")
    # else:
        # print("its century year not an leap year")
        
# else:
    # print("its not an century year")
    
# #15.number to check if it's between {min_value} and {max_value}:
# min_value = 10
# max_value = 50

# number = int(input("enter a number if its between min_value and max_value:"))

# if (min_value <= number <= max_value):
    # print(f"{number} is within range")
# else:
    # print(f"{number} is outof range")
    

# #16.# Formula to check a valid triangle 
# # a + b > c
# # a + c > b
# # b + c > a


# side1 = float(input("enter sides of triangle side1:"))
# side2 = float(input("enter sides of triangle side2:"))
# side3 = float(input("enter sides of triangle side3:"))

# if (side1 + side2 > side3) and (side1 +side3 > side2) and (side2 + side3 > side1):
    # if side1 == side2 ==side3:
        # print("equilateral triangle: exctly three sides are equal")
    # elif side1 == side2 or side1 == side3 or side2 == side3:
        # print("isocelus triangle: exctly two sides are equal")
    # else:
        # print("scalus triangle: exctly two sides are equal")
        
# else:
    # print("entered the lenght of triangle not forms a triangle")
    
    
#17.number to check the number is divisible by 2 and 3
num = int(input("enter a number :"))
if num %2 ==0 and num %3 ==0:
    print(f"{num} both it is divisble by 2 and 3")
elif num %2 ==0:
    print(f"{num} is divisible by 2")
elif num %3 ==0:
    print(f"{num} is divisible by 3")
else:
    print(f"{num} is not divible by 2 and 3")

#18.score = float(input("Enter your score: "))
if score >= 50:
    print("You pass!")
else:
    print("You fail.")

#19.user_input = input("Enter a string: ")
if user_input.isupper():
    print("Its a uppercase.")
elif user_input.islower():
    print("Its a lowercase.")
else:
    print("Mix")

#By Manual
is_upper = False
is_lower = False

for char in user_input:
    if 'A' <= char <= 'Z':
        is_upper = True
    elif 'a' <= char <= 'z':
        is_lower = True

if is_upper and is_lower:
    print("The string is a mix of uppercase and lowercase letters.")
elif is_upper:
    print("The string is uppercase.")
elif is_lower:
    print("The string is lowercase.")
else:
    print("The string contains no letters.")
    
    
#20.number = int(input("Enter a number to check a prime number: "))

if number % 2 == 0 or number % 3 == 0 or number % 5 == 0 or number % 7 == 0 or number % 11 == 0 or number % 13 ==0:
    print("Its not a prime number.")
else:
    print("prime number.")

#By loop
if number > 1:
    for i in range(2, number):
        if number % i == 0:
            print("Not a prime number:")
            break
    else:
        print("Prime number")
else:
    print("Prime number.")
    