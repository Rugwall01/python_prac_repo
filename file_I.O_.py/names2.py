#names = [] 

#for _ in range(3):
#    names.append(input("What's your name? "))

#for name in sorted(names):
#    print(f"hello, {name}")


name = input("What's your name? ")

file = open("names2.txt", "w")
file.write(name)
file.close()


# In this version the file is created and written to however every time you open the program and write to the file again it overwrites the old data. in names3.py we will see this corrected

# This is mainly due to the "w" that is the first change next




