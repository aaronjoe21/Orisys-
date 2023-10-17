import re
hashtag=input("Enter a message with hashtags:")
pattern = "#\w+"
n=re.findall(pattern,hashtag)
print(n)

