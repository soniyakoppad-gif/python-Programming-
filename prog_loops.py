# #1. Print numbers from 1 to 20 using a for loop.

# n = int(input("enter a number max_ range "))
# for i in range(0,n+1):
    # print(i)
    # i +=1
# print("----------------------------")
  
# #2.# Use a while loop to print even numbers from 1 to 50.
# i =0
# while i<= 50:
    # print(i)
    # i +=2


# #3.  Write a program to calculate the sum of all numbers between 1 and 100.

# #while loop
# i =0
# summ = 0
# while i <= 100:
    # summ +=i
    # i+=1
    
# print("summation",summ )



# #for loop


# summ =0
# for i in range(0,101):
    # summ +=i
    # i +=1
# print("summation:",summ)

# #4.# Print the multiplication table of a given number

# n = int(input("enter a multiplication table:"))
# for i in range(1,11):
    # print(f"{n} X {i} = {n * i}")
    
# #while loop
# n = int(input("enter a multiplication table:"))
# i =1
# while i<=10:
   # print(f"{n} X {i} = {n * i}")
   # i +=1
   
#5.# Print all odd numbers between 1 and 100 using a loop
# i =1
# while i <=100:
    # print(i)
    # i+=2
    
# #6.# Use a for loop to print each character of a string.
# string = input("enter a string:")
# for i in string:
    # print(i)
# print(len(string))

# #7. Find the factorial of a number using a while loop.

# num =int(input("enter number:"))
# i = 1
# fact = 1
# while i <=num:
    # fact *=num
    # num -=1
    
# print("fact:",fact)

# #8.# Use a for loop to print numbers from 10 down to 1.
# num = int(input("enter number:"))
# for i in range(num,0,-1):
    # print(i)
    

# for i in range(1,num+1):
    # print(num)
    # num -=1
    
# #9.# Write a program to print the first 10 Fibonacci numbers
# limit =int(input("enter the limit:"))

# i =1
# a =0
# b = 1

# while i<= limit:
    # print(a)
    # c = a+b
    # a = b
    # b = c
    # i +=1
    
 # #10.# Use a loop to count the number of digits in an integer.
# digit = int(input("enter the number:"))

# count = 0
# for i in str(abs(digit)):
    # count +=1
    
# print("number of digits:",count)

# #11.# Print the reverse of a given number.

# text = input("enter a string:")
# reversed_string = ""

# for chr in text:
    # reversed_string  = chr + reversed_string
    
    
# print("reversed_string:",reversed_string)

# rev_string = text[::-1]
# print (rev_string)


# #12.Print all prime numbers between 1 and 50.
# limit = int(input("Enter the limit: "))

# for num in range(2, limit + 1):
    # is_prime = True
    # for i in range(2, num):
        # if num % i == 0:
            # is_prime = False
            # break
    # if is_prime:
        # print(f"{num} is a prime number.")
        
        
        
        
# #13.# Use nested loops to print a pyramid pattern of *.
# row = int(input("enter the number of rows to build pyramid"))

# for i in range(1,row+1 ):
    # for j in range(row - i):
        # print(" ",end = " ")
    # for k in range(2 * i -1):
        # print(" *",end = "")
    # print()   
        

# #14.
# while True:
    # user_input=input("enter something(type 'exit' to stop):")

    # # if user_input.lower() == 'exit':
        # # print("existing the loop")
        # # break
    # # else:
        # # print(f"you entered :{user_input}")
    

# #15.# Print the sum of even and odd numbers separately up to a given number.

# limit = int(input("enter a number:"))
# even_sum = 0
# odd_sum = 0
# for num in range(1,limit+1):
    # if num %2 ==0:
        # even_sum += num
    # else:
        # odd_sum += num
        
# print(f"Sum of even numbers up to {limit}: {even_sum}")
# print(f"Sum of even numbers up to {limit}: {even_sum}")


# ##16. Create a program to calculate the sum of the digits of an inputted integer.
# num =int(input("enter number:"))
# sum_of_digits = 0

# while num >0:
    # d = num % 10
    # sum_of_digits +=d
    # num //=10
# print("sum_of_digits",sum_of_digits) 


# #18. Use a loop to print numbers in reverse order within a given range.
# start = int(input("Enter the starting number: "))
# end = int(input("Enter the ending number: "))
# for i in range(end,start-1, -1):
    # print(i)
    
#19.# Use a for loop to print the square of each number from 1 to 10
n = int(input("enter number:"))
for i in range(1,11):
    square = n * n
    
print(square)

#20.
import time  # Importing time module for sleep function

countdown_start = int(input("Enter a number to start the countdown: "))

for i in range(countdown_start, -1, -1):
    print(i)
    time.sleep(1)

print("Countdown complete!")

import time
countdown_start = int(input("enter count dwn num:"))

for i in range(countdown_start, -1 ,-1):
    print(i)
    time.sleep(1)
print("countdown complete!")