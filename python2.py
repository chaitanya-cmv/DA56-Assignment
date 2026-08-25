# 1. LIST CREATION

# Create age_list with five integer elements
age_list = [24, 25, 26, 27, 28]

print("Age List:", age_list)


# Create name_list with five string elements
name_list = ["Anu", "Riya", "Meera", "Diya", "Kavya"]

print("Name List:", name_list)


# 2. LIST OPERATIONS / MODIFICATIONS

# a. Append "Yazhini" to name_list
name_list.append("Yazhini")
print("After append:", name_list)


# b. Insert 30 at index 2 in age_list
age_list.insert(2, 30)
print("After inserting 30:", age_list)


# c. Remove "Yazhini" from name_list
name_list.remove("Yazhini")
print("After removing Yazhini:", name_list)


# d. Pop the last element from age_list
age_list.pop()
print("After popping last element:", age_list)


# e. Extend age_list with [29, 30, 26]
age_list.extend([29, 30, 26])
print("After extending:", age_list)


# f. Sort age_list in descending order
age_list.sort(reverse=True)
print("Sorted in descending order:", age_list)


# g. Find maximum, minimum and sum of ages
print("Maximum age:", max(age_list))
print("Minimum age:", min(age_list))
print("Sum of all ages:", sum(age_list))


# 3. ACCESSING LIST ELEMENTS

# a. Print the first element of name_list
print("First element:", name_list[0])


# b. Print the last element of name_list
print("Last element:", name_list[-1])


# c. Print elements from index 2 to index 4
print("Elements from index 2 to index 4:", name_list[2:5])


# d. Print name_list in reverse order
print("Reverse order:", name_list[::-1])


# 4. DICTIONARY

# a. Create student_marks dictionary
student_marks = {
    "Anu": 75,
    "Riya": 88,
    "Meera": 92,
    "Diya": 68,
    "Kavya": 79
}

print("Student Marks:", student_marks)


# b. Access and print the mark of a specific student
print("Marks of Riya:", student_marks["Riya"])


# c. Add Janani with a mark of 80
student_marks["Janani"] = 80

print("After adding Janani:", student_marks)


# d. Update the mark of an existing student to 82
student_marks["Anu"] = 82

print("After updating Anu's mark:", student_marks)


# e. Print keys, values and key-value pairs
print("Keys:", student_marks.keys())
print("Values:", student_marks.values())
print("Key-Value pairs:", student_marks.items())


# 5. SETS

# a. Create my_set
my_set = {'a', 'e', 'i', 'o', 'u', 'a', 'a', 'i'}

print("My set:", my_set)

# Explanation:
# Sets do not allow duplicate values.
# Therefore, duplicate 'a' and 'i' are removed.


# b. Attempt to change my_set[4]
# This will give an error because sets do not support indexing.
#
# my_set[4] = 's'

# Instead, to add 's' to the set, use:
my_set.add('s')

print("Set after adding 's':", my_set)


# 6. UNION AND INTERSECTION

# c. Create two sets
set1 = {1, 3, 5, 7, 9}

set2 = {2, 3, 5, 8, 10}


# d. Union
union_set = set1.union(set2)

print("Union:", union_set)


# Intersection
intersection_set = set1.intersection(set2)

print("Intersection:", intersection_set)


# 7. CONDITIONAL STATEMENTS

# Performance Category Program

score = int(input("Enter your score (0 to 10): "))

if score < 0 or score > 10:
    print("Invalid score. Please enter a score between 0 and 10.")

elif score > 7:
    print("Above Average: Excellent performance!")

elif score >= 4:
    print("Average: Good effort!")

else:
    print("Below Average: Need to improve your performance. Consistent practice will lead to better results.")