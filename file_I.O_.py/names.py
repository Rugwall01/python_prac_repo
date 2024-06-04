
name = input("What's your name? ")
print(f"hello, {name}")

#This idea above made to be coducive to multiple names below then refined furthur

names = []


for _ in range(3):
    name = input("What's your name? ")
    names.append(name)


# "Refined"


for _ in range(3):
    names.append(input("What's your name? "))

# Go to names1.py

