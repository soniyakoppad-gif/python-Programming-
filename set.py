# ------------------ Set Problems (Beginner to Intermediate) ------------------

# 1. Create a set with 5 fruit names and print it.
fruits = {"apple", "banana", "cherry", "lychee", "mango", "mango"}  # duplicates ignored
print(fruits)

# 2. Add "kiwi" to the set.
fruits = {"apple", "banana", "cherry"}
fruits.add("kiwi")
print(fruits)

#3. Remove "banana" from the set.
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)


#4.# 4. Try to remove "orange" using discard (no error if missing).
fruits = {"apple", "banana", "cherry"}
fruits.discard("orange")
print(fruits)


# 5. Clear the entire set.
fruits = {"apple", "banana", "cherry"}
fruits.clear()
print(fruits)

#6.# 6. Print all elements of the set using a loop.
colors = {"red", "green", "blue"}
for i in colors:
    print(i)
    
    
# 7. Check if "blue" exists in the set.

colors = {"red", "green", "blue"}

print("yes!:" if "blue" in colors else "no!")

# 8. Count how many elements are in the set.
colors = {"red", "green", "blue"}
print(len(colors))

# 9. Loop through a set and print each item in uppercase.
colors = {"red", "green", "blue"}
color = {color.upper() for color in colors}
print(colors)


#10.10. Add user input into an existing set (example version without input).
colors = {"red", "green", "blue"}
user_input = input("enter color:").strip()
colors.add(user_input)
print(colors)

# 11. Find the union of two sets.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union =set1 | set2

print(union)


# 12. Find the intersection of two sets.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersection = set1 & set2
print(intersection)

## 13. Find the difference (set1 - set2)

difference = set1 -set2
print(difference)

# 14. Find the symmetric difference.
symmetric_difference = set1 ^ set2
print(symmetric_difference)

# 15. Use `|` operator to join two sets.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x | y
print(z)


# 16. Convert a list into a set (remove duplicates).
numbers = [1, 2, 2, 3, 4, 4, 5]
n=set(numbers)
print(n)

# 17. Convert a string into a set of characters.
text = "banana"
print(set(text))

# 18. Copy a set and modify the copy.
original = {"a", "b", "c"}
copy = {*original}
copy.add("d")
print(copy)

# 19. Convert a set back to a list.

animals = {"cat", "dog", "fish"}
print(list(animals))

# 20. Convert two lists to sets and find common elements.
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
print(set(a) & set(b))

## 21. Remove all even numbers from a set.
nums = {1, 2, 3, 4, 5, 6, 7, 8}
a = {n for n in nums if n %2 != 0}
print(a)

#22. Keep only items that start with "A".
names = {"ali", "Ahmed", "Sara", "Adeel"}
#names = {name for name in names if name.upper().startswith("A")}
names = {name for name in names if name.upper() .startswith("A")}
print(names)

# 23. Find unique characters in a sentence.
text = "Set is a unique collection"
print(set(text))

# 24. Get common vowels from two strings using sets.
str1 = "education"
str2 = "foundation"
vowels = {"a", "e", "i", "o", "u"}
print(set(str1) & set(str2) & vowels)

# 25. Find letters that appear only in one string but not both.
a = "python"
b = "typhoon"
print(set(a) ^ set(b))

# 26. Check if one set is a subset of another.
a = {1,2}
b = {1,2,3,4,6}
c = a.issubset(b)
print(c)

# 27. Check if two sets are disjoint.
a = {1, 2}
b = {3, 4}
print("disjoint" if a.isdisjoint(b) else "notdisjoint")

# 28. Check if one set is a superset of another.
a ={1,2,3,4}
b = {3,4}
print("superset" if a.issuperset(b) else "not disjoint")


# 29. Remove duplicates from a list using a set.
nums = [1, 2, 2, 3, 3, 4, 5]
print(set(nums))

# 30. Create a set from a sentence and count how many unique characters it contains.
sentence = "Practice makes perfect"
print(len(set(sentence)))














