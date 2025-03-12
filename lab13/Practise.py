#The re Module: Basic Functions
#1 re.search()
import re

text = "My phone number is 5555555 and my office number is 123456789"
pattern = r"\d+"
replacement = "NUMBER"

print(text)
print(re.sub(pattern, replacement, text))

#2. re.match()
import re

text = "My name is Adilet"
patter = r"Adilet"

match = re.search(patter, text)
if match:
    print("Found:", match.group())
else:
    print("No match")


#3 re.findall()
import re

text = "John's number is 555-12345, and Mia's number is 555-56789"
pattern = r"\d{3}-\d{5}"

result = re.findall(pattern, text)
print(result)