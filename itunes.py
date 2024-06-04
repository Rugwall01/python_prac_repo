# This is a program designed to "pretend" to be a browser so it can grab or 'request' data from an API, specifically apples API which is accessible in a browser via a formula anyone can follow


import requests
import sys


if len(sys.argv) != 2:
    sys.exit()


response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(response.json())


# In itunes1.py I will import the json library and format the information specifically to be json inreadable python format, in this iteration it comes out in json which is very similar but since python comes with its own json library we can convert it to  more readable format in python. see itunes1.py














