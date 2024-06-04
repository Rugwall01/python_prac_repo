
score = int(input("Score: "))

if score > 100:
    print("Grade A++")
elif score >= 96 and score <= 100:
    print("Grade: A+")
elif score == 95:
    print("Grade: A")
elif score >= 90 and score <= 94:
    print("Grade: A-")

elif score >= 86 and score < 90:
    print("Grade: B+")
elif score == 85:
    print("Grade: B")
elif score >= 80 and score <= 84:
    print("Grade: B-")

elif score >= 76 and score < 80:
    print("Grade: C+")
elif score == 75:
    print("Grade: C")
elif score >= 70 and score <= 74:
    print("Grade: C-")

elif score >= 66 and score < 70:
    print("Grade: D+")
elif score == 65:
    print("Grade: D")
elif score >= 60 and score <= 64:
    print("Grade: D-")
else:
    print("Grade: F")




# Here is the evolved efficient code
# Notice how the number and score are switched around at the begining and this allows score to be used
# on both sides in a single "equation"

if score > 100:
    print("Grade A++")
elif 96 <= score <= 100:
    print("Grade: A+")
elif score == 95:
    print("Grade: A")
elif 90 <= score <= 94:
    print("Grade: A-")

elif 86<= score < 90:
    print("Grade: B+")
elif score == 85:
    print("Grade: B")
elif 80 <= score <= 84:
    print("Grade: B-")

elif 76 <= score < 80:
    print("Grade: C+")
elif score == 75:
    print("Grade: C")
elif 70 <= score <= 74:
    print("Grade: C-")

elif 66 <= score < 70:
    print("Grade: D+")
elif score == 65:
    print("Grade: D")
elif 60 <= score <= 64:
    print("Grade: D-")
else:
    print("Grade: F")



# And here is yet an EVEN SIMPLER VERSION!!!!



if score > 100:
    print("Grade A++")
elif score >= 96:
    print("Grade: A+")
elif score == 95:
    print("Grade: A")
elif score >= 90:
    print("Grade: A-")

elif score >= 86:
    print("Grade: B+")
elif score == 85:
    print("Grade: B")
elif score >= 80:
    print("Grade: B-")

elif score >= 76:
    print("Grade: C+")
elif score == 75:
    print("Grade: C")
elif score >= 70:
    print("Grade: C-")

elif score >= 66:
    print("Grade: D+")
elif score == 65:
    print("Grade: D")
elif score >= 60:
    print("Grade: D-")
else:
    print("Grade: F")




























