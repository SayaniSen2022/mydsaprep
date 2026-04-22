# practice regex

import re

# Extract all digits from 'a1b22c333'
text = "a1b22c333"
result = re.findall(r"\d+", text)
# print(result)

# Extract all words from 'Hello world 123'
text = "Hello world 123"
result = re.sub(r"\d+", "",text)
# print(result)

# Remove all special characters from 'Hello@# World!!'
text = "Hello@# World!!"
res = re.sub(r"[^a-zA-Z0-9]", "", text)
# print(res)

# Count number of vowels in 'programming'
text = "programming"
res = re.findall(r"[aeiou]", text)
# print(len(res)) 
# res is a list

# Check if string contains only digits
test = "123"
# print(bool(re.fullmatch(r"\d+", test))) 
#true

# Validate email address
def isValidEmail(email):
  pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
  return re.fullmatch(pattern, email) is not None
# print(isValidEmail("aB123@fmail.com")) 

# Extract all emails from text
text = "Contact me at a@gmail.com and b@yahoo.com"
res = re.findall(r'[a-zA-Z0-9+-_%.]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
print(res)

# Extract all URLs
