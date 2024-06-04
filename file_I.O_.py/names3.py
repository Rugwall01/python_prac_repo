
name = input("What's your name? ")

file = open("names3.txt", "a")
file.write(name)
file.close()

# Changed the "w" to an "a" w stands for write a stands for append. Append will continuously add to the file insstead of rewritting it everytime it is opened

# there are no spaces though so the code needs to be refined again see names4.py
















