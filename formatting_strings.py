name = input("What's your name? ")

name = name.strip()

#f  for format before "" will format the variable inside the curly braces (i.ethese things{}), 
#in this case the variable is 'name' and is a string    
#the name = name.strip() takes away the white space that exists when a variable inside curly braces is
#printed next to a set string value such as the text 'hello,' the 'name' is a defined string and the 
#'.' allows/opens up the ability for functions to be assigned to the string. Arguments can modify the funtion if desired ny putting the arg into the function's parenthesis'


name = name.capitalize()
#another function of a string that formats the string 'name' ... in this case it will capitalize

name = name.title()
#this capitalizes all words separated by spaces in the string intead of just the first
#can be written like below

name = name.strip().title()

#or in the original defenition of name like this:
# name = input("What's your name? ").strip().title() <-- This is arguably the most efficient and safe



#now we willl print the string
print(f"hello, {name}")



















