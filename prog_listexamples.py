# ------------------ Slicing Examples ------------------

fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# All elements from start
print(f"1 :{fruits[0:]}")

# Index 1 to 2
print(f"2 : {fruits[1:3]}")

# # Last element
print(f"3 : {fruits[-1]}")

# Empty, invalid forward slice
print(f"4 : {fruits[-1:-4]}")

 # Every second element
print(f"5: {fruits [0::2]}")

 # Empty, invalid forward step
print(f"6 : {fruits[-1:-4:2]}")
 

## From -4 to -2, skipping every second
print(f"7: {fruits[-4:-1:2]}") 

 # Empty
print(f"8: {fruits[-1:1]}")
# All except last two

print(f"9: {fruits[0:-2]}") 



# ------------------ Basic List Problems (Beginner) ------------------


# 1. Print the first element of the list.
fruits = ["apple", "banana", "cherry", "date"]
print(fruits[0]) 

# 2. Print the last element using negative indexing.
print(fruits[-1])

#3.# 3. Print all elements using a loop.
for fruit in fruits:
    print(fruit)
    
    
#4.# 4. Find the length of the list.
print(len(fruits))


# 5. Append a new element "orange" to the list.
fruits = ["apple", "banana", "cherry"]
print("before append:",fruits)
fruits.append("mango")
print("after append:",fruits)


#6.# 6. Insert "grape" at index 2.
fruits = ["apple", "banana", "cherry"]
fruits.insert(2,"grape")
print("after append",fruits)


# 7. Remove the element "banana".

fruits.remove("banana")
print(fruits)

# 8. Remove the last element using pop().
fruits.pop()
print(fruits)

# 9. Check if "apple" exists in the list.
fruits = ["apple", "banana", "cherry"]
print("yes,apple is there in list" if "apple" else "not in list")

#10.
# 10. Count how many times "apple" appears.
print(fruits.count("apple"))



# ------------------ Indexing & Slicing ------------------

# 11. Print the first 3 elements.
fruits = ["apple", "banana", "cherry", "date", "orange"]
print(fruits[:3])

# 12. Print all elements except the last one.
print(fruits[:4])

# 13. Reverse the list using slicing.
fruits = ["apple", "banana", "cherry", "date"]
print(fruits[::-1])

# 14. Print every second element.
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(fruits[::2])

# 15. Print all elements from index 2 onward.
print(fruits[2:])

# 16. Get a sublist from index 1 to 3.
print(fruits[1:4])

# 17. Print the list in reverse using a loop.
for i in range(len(fruits)-1,-1,-1):
    print(fruits[i])
    
#18.# 18. Replace the second element with "kiwi".
fruits = ["apple", "banana", "cherry"]
fruits[2] = "kiwi"
print(fruits)

# 19. Swap the first and last elements.
fruits = ["apple", "banana", "cherry", "date"]
fruits[0],fruits[-1] = fruits[-1],fruits[0]
print(fruits)

# 20. Delete the first 3 elements using slicing.
fruits = ["apple", "banana", "cherry", "date", "orange"]
fruits = fruits[3:]
print(fruits)


# ------------------ Sorting & Math ------------------


# 21. Sort the list alphabetically.
words = ["grape", "apple", "banana", "cherry"]
words.sort()
print(words)

# 22. Sort a list of numbers in descending order.
numbers =[5,2,9,1,7]
length =len(numbers)
for i in range(length):
    for j in range(0,length -i-1):
        if numbers[j] < numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
print(numbers)


## 23. Find the maximum number in a list.
numbers = [45, 22, 89, 33, 67]
max_value = numbers[0]
for i in numbers:
    if i > max_value:
        max_value = i
print(max_value)
    
    
print(max(numbers))
    
#24.# 24. Find the minimum number in a list.
numbers = [45, 22, 89, 33, 67]
min_value = numbers[0]
for i in numbers:
    if i < min_value:
        min_value = i
print(min_value)

print(min(numbers))


#25.# 25. Find the average of numbers.
numbers = [45, 22, 89, 33, 67]
avg_num = sum(numbers) / len(numbers)

print(avg_num)

# ------------------ List Comprehension & Filtering ------------------

# 26. List of squares and cube from 1 to 10.

square = [i **2 for i in range(1,11)]
cube = [i **3 for i in range(1,11)]


print(square)
print(cube)

# 27. Filter even numbers.
n = int(input("enter number:"))
if n %2 ==0:
   print(f"{n} is even number")
   
else:
    print(f"{n} is odd number")
    
# 28. Strings with more than 5 characters

names = ["apple", "pineapple", "kiwi", "banana", "grapes"]

long_names = [i for i in names if len(i) >5] 
print(long_names)


#29.# 29. Extract all vowels from a string.
text = "Programming is fun and educational"
vowels = [i for i in text if i.lower() in ["a","e","i","o","u"]]
print(vowels)


# 30. Find common elements in two lists.

list1 = ["apple", "banana", "cherry"]
list2 = ["banana", "date", "cherry"]
comman = [i for i in list1 if i in list2]
print(comman)







   









