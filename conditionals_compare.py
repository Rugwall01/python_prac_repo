
x = int(input("What's x? "))
y = int(input("What's y? "))


if x < y:
    print("x is less than y")

if x > y:
    print("x is greater than y")
if x == y:
    print("x is equal to y")





# To make this more concise and efficient




x = int(input("What's x? "))
y = int(input("What's y? "))


if x < y:
    print("x is less than y")

elif x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal to y")


# See how the above elif stops the process if the Boolean condition is True, and only proceeds to 
# check the next Boolean condition if the prevous Boolean condition has rendered an answer of False





# "Last" progression of this code simplifies it more and circumvents the need to ask the third
# question/conditional shoult the previous conditionals render False





x = int(input("What's x? "))
y = int(input("What's y? "))


if x < y:
    print("x is less than y")

elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")




























