# Part 1
import re

text = "Our office number is 555-1234 and direct phone number is 555-5678. For emergencies, dial 555-9999"
pattern = r"\d{3}-\d{4}"

phone_numbers = re.findall(pattern, text)

print("Phone Numbers Found:", phone_numbers)


# Part 2
text = "Hello, my name is Adilet!"
pattern = r"Hello"

print("Using re.match()...")
match = re.match(pattern, text)
if match:
    print("Match Found:", match.group())
else:
    print("No Match Found!")

print("Using re.search()...")
text = "Why you did not wave me a Hello???"
search = re.search(pattern, text)
if search:
    print("Search Found:", search.group())
else:
    print("No Search Found!")

print() # separate each lab exercise

# Part 3
text = "There are 3 apples, 15 oranges, and 256 bananas in the basket."
pattern = r"\d+"

print(text)

text = re.sub(pattern, "NUMBER", text)
print(text)