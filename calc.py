x = input("What's x? ")
y = input("What's y? ")


z = int(x)+ int(y)

print(z)




# Another way of writting this that may be more efficient potentially

x = int(input("What's x? "))
y = int(input("What's y? "))

print(x + y) 



# To include commas

x = float(input("What's x? "))
y = float(input("What's y "))

z = round(x + y)

print(f"{z:,}")


# A way to round to a decimal place, in this case its to the 2nd decimal place, notice 
# 2 after x/y comma

x = float(input("What's x? "))
y = float(input("What's y "))

z = round(x / y, 2)

print(f"{z:,}")


# Another way of rounding to the 2 decimal place, notice .2f

x = float(input("What's x? "))
y = float(input("What's y "))

z = round(x / y,)

print(f"{z:.2f}")

















