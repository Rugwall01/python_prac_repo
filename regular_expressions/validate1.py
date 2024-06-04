
#re.search(pattern, string, flags=0) 


import re


email = input("What's your email? ").strip()


if re.search("@", email):
    print("Valid")
else:
    print("Invalid")


    
# Operators in re library are '.' '*' '+' '?' '{m}' '{m,n}'
# . any character except a newline
# * 0 or more repetitions
# + 1 or more repetitions
# ? 0 or 1 repetition
# {m} m repetitions
# {m,n} m-n repetitions

# Adding .* to each side of the @ bekow will allow the user to put anycharacters 0 or more to the left and the right using a .+ instead will require at least one entry on each side
email = input("What's your email? ").strip()


if re.search(".*@.*", email):
    print("Valid")
else:
    print("Invalid")



# Here it is
email = input("What's your email? ").strip()


if re.search(".+@.+", email):
    print("Valid")
else:
    print("Invalid")



# Doing ..* is the same thing as .+ because once you move on from the first . and add another the first . is defined as requiring 1 then tou define the second. as 0 or more effectively creating 1 or more which is what .+ is. Look above at the + symbol and * symbol in the legend



email = input("What's your email? ").strip()


if re.search("..*@..*", email):
    print("Valid")
else:
    print("Invalid")



# re.search uses a finite state machine aka a non-deterministic finite automaton which is implimented in software
# see:
    #https://stackoverflow.com/questions/60843126/non-deterministic-finite-automata
    #https://www.google.com/imgres?q=non-deterministic%20finite%20automata&imgurl=https%3A%2F%2Fwww.tutorialspoint.com%2Fautomata_theory%2Fimages%2Fndfa_graphical_representation.jpg&imgrefurl=https%3A%2F%2Fwww.tutorialspoint.com%2Fautomata_theory%2Fnon_deterministic_finite_automaton.htm&docid=-JRopf3EbaUBUM&tbnid=PRKVpRzSQ8H2pM&vet=12ahUKEwjRysH376eGAxWYGDQIHTTrA9EQM3oECHsQAA..i&w=502&h=149&hcb=2&ved=2ahUKEwjRysH376eGAxWYGDQIHTTrA9EQM3oECHsQAA

    #https://www.google.com/imgres?q=non-deterministic%20finite%20automata&imgurl=https%3A%2F%2Fuserpages.umbc.edu%2F~squire%2Fimages%2F451-f2.jpg&imgrefurl=https%3A%2F%2Fuserpages.umbc.edu%2F~squire%2Fcs451_l4.html&docid=aSzhj7VAwjH-0M&tbnid=V2i2OHLKAkuQ0M&vet=12ahUKEwjRysH376eGAxWYGDQIHTTrA9EQM3oECB0QAA..i&w=554&h=344&hcb=2&ved=2ahUKEwjRysH376eGAxWYGDQIHTTrA9EQM3oECB0QAA

    #https://www.google.com/imgres?q=non-deterministic%20finite%20automata&imgurl=https%3A%2F%2Fstatic.javatpoint.com%2Ftutorial%2Fautomata%2Fimages%2Fnfa.png&imgrefurl=https%3A%2F%2Fwww.javatpoint.com%2Fnon-deterministic-finite-automata&docid=1MdF-Cfm6sZdHM&tbnid=UiZFzqaYOe2JnM&vet=12ahUKEwjRysH376eGAxWYGDQIHTTrA9EQM3oECC8QAA..i&w=238&h=169&hcb=2&ved=2ahUKEwjRysH376eGAxWYGDQIHTTrA9EQM3oECC8QAA

    #https://www.google.com/imgres?q=non-deterministic%20finite%20automata&imgurl=https%3A%2F%2Fwww.csd.uwo.ca%2F~mmorenom%2FCS447%2FLectures%2FLexical.html%2Fimg17.png&imgrefurl=https%3A%2F%2Fwww.csd.uwo.ca%2F~mmorenom%2FCS447%2FLectures%2FLexical.html%2Fnode3.html&docid=QTDHkBTLy9hYsM&tbnid=lQDcvfJgNRaPyM&vet=12ahUKEwjMvdSi8KeGAxVEJDQIHcQNCM0QM3oECB8QAA..i&w=1031&h=691&hcb=2&ved=2ahUKEwjMvdSi8KeGAxVEJDQIHcQNCM0QM3oECB8QAA

    #https://stackoverflow.com/questions/60843126/non-deterministic-finite-automata

# Go to validate2.py
