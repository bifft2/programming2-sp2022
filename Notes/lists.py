class_list = ["Alberto", "Jonah", "Ryder", "Malcolm"]
print(class_list)

# get elements at specific indices
print(class_list[0])
print(class_list[3])
print(class_list[-1])
# print(class_list[-5])

# get the length of the list
print(len(class_list))

# append to a list
class_list.append("Ms. Ifft")
print(class_list)

# loop through a list
for i in range(len(class_list)):
    print(class_list[i])

# Jonah

# index function
list_1 = ["stats", "mobile app development", "graphic novels"]
list_1.insert(-10, "free period") # what happens when the index is too large?
print(list_1)

list_1.remove("stats")  # error if the item doesn't exist in the list

# len counts the items in a list or the characters in a string


# Malcolm

nums = [3, 6, 1, 3, 8, 9, 2, 3]

print(min(nums))
print(max(nums))

# also works on strings


print(sum(nums))


# Alberto

greetings = ["Hi", "Hello", "What's up", "Howdy"]
print(greetings[-1])
print(greetings[3])

print(greetings.index("Hello"))

print(nums.count(3))

# Ryder
test = [2, 3, 4, 5, 6]
print(test[1:5])

test.sort()
test.reverse()

# .extend()
# concatenation


#               0           1         2        3
our_class = ["Malcolm", "Alberto", "Jonah", "Ryder"]

# use list slicing to grab ["Alberto", "Jonah"]
print(our_class[1:3])

# 3 ways to insert Ms. Ifft at the end
our_class.insert(4, "Ms. Ifft")
our_class.append("Ms. Ifft")
our_class.insert(-1, "Ms. Ifft")
print(our_class)

# print the length of the element at the 0th index of the list
print(len(our_class[0]))

# print the lowest character in the name at the 2nd index
print(min(our_class[2].lower()))
# or sort and then grab