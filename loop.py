# Loop real world example

# Calculating total price from a shopping list

prices = [120,250,89,150]
total = 0

for price in prices:
    total += price

print("Total Price:-" , total)    

# Reading All Files in a Folder

import os
folder_path = "/home/coding-with-raja/Documents"
for file in os.listdir(folder_path):
    if file.endswith(".pdf"):
        print("Found pdf file:", file)

# Counting Words in Sentences
sentences = ["I love Python", "Loops are powerful", "Practice daily"]
word_count = 0

for sentence in sentences:
    word_count += len(sentence.split())

print("Total words:", word_count)






# Automating Repeated Tasks (e.g., Sending Emails)
emails = ["raja@gmail.com", "prabhat@gmail.com", "pd@gmail.com"];

for email in emails:
    print(f"Sending email to {email}..... ") 


# Filtering Even Numbers
numbers = [1,2,3,4,5,6]
even = [n for n in numbers if n % 2 ==0 ]
print("Even numbers:", even)

#Processing API Data
data = [
    {"name": "Raja", "age": 32},
    {"name": "Prabhat", "age": 35},
    {"name": "Santosh", "age": 42}
]
for user in data:
    print(f"{user['name']} is {user['age']} years old  ") 