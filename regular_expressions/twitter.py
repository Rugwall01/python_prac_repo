# Allow users to put in twitter url and infers the username
# Also should allow to reverse and get url from username entry


url = input("What is your twitter URL: ").strip()

# for url.replace the ORDER is, what you want to replace THEN what you want to replace that with
username =  url.replace("https://twitter.com/", "")
# So in the above I am replacing the first part of the url with nothing because I know the username 
# comes last in twitter url's, so I can extract it this way


print(f"username: {username}")


# needs added functionality to work in different senarios see twitter1.py









































