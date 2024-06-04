

import json
import requests
import sys


if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity+song&limit=1&term=" + sys.argv[1])

o = response.json()
for result in 0["results"]:
    print(result["trackName"])

# grabbing the json object from the server response from url, this url is a txt file of all the info for weezer limited to 1, inside is an key named 'results' this key is a list and it contains only 1 value because we limited it to 1, trackName is the specific 'value' we are targeting 

# Go to itunes3.py where we will grab the first fifty trackName(s) or in otherwords songs















