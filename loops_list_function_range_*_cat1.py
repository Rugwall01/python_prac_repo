# Python is indexed from 0, meaning if you have a variable defined as a list of seperate string valueslike below they will be indexed from left to right starting at 0. You can target/select a specific strvalue using square bracket '[]'  and referencing its index inside, then passing this into the argument of your function

students = ["Heromine", "Harry", "Ron"]

#print(students[0])
#print(students[1])
#print(students[2])

# The above hard codes the printing of this list, below opens up functionality

for student in students:
    print(student)

# This is basically saying for every i in list "students" print i. And i is immediately initiallized seperately to each entry in the list, which are already indexed, so its more like [0], [1], [3], ... ; 

# IN PLACE OF 'i' OR '_' WE USE 'student' IN ORDER TO MAKE THINGS MORE UNDERSTANDABLE/READABLE AND LESS CRYPTIC 



# Above is iteration using strings, if we want to iterate these strings using numbers like weve done in the past iterating with numbers we can do that. Look Below where we use 'len' or 'length'


for i in range(len(students)):
    print(students[i])


# 'students' passed to 'len', 'len' then checks for the "length" of 'students', its length is the number of separate string entries it has, it then applies/passes this number to range and the range is set to that number for the loop. i is already initiallized to go in order and assign itself to each string entry by its index; so when we pass i into the index value that is then passed along with its reference list 'students' into the argument for print, the print function will output the string value of the corresponding index value, which is i, which is first initiallized to [0] and then everytime the loop repeats, is re-initiallized to the next index value automatically [1], [2], [3], ... 



# The code below prints the string value, as before, along with its corresponding index value 'i'

for i in range(len(students)):
    print(i, students[i])



# In the code below we list the index value shifted by +1 in order to make it look like a list made by a person, which would normally start at 1


for i in range(len(students)):
    print(i + 1, students[i])









