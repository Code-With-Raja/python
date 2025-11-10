x = 4; # x is int
x= "Raja" # now x is str

print(x)

myVar = "prabhat"
print(myVar)



x,y,z = "Orange", "apple", "banana"

print(x)
print(y)
print(z)

x=y=z= "coconut";
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"];


x,y,z= fruits;

print(x)
print(y)
print(z)

a="Python ";
b="is ";
c="awesome"
print(a,b,c)
print(a+b+c)

x= "awesom"

def myfunc():
    print( "Python is a " + x)
myfunc()
x= "awesom"

def myfunc():
    x= "fantastic"
    print( "Python is a " + x)
myfunc()

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

fruits = ["apple", "mango", "orange"]

print (fruits.index("orange"))

print("raja".isalnum())
print("raja123".isalnum())
print("123".isalnum()) 

print("raja 123".isalnum())
print("raja!".isalnum())
print(" 123!".isalnum())

print("Python".isalpha()) 
print("Python3".isalpha())
print("Hello World".isalpha())
print("Hello!".isalpha())
print("²".isdigit())

print("Hello".isascii()) 
print("12345".isascii()) 
print("Hello123!".isascii())
print("नमस्ते".isascii())  

print("name".isidentifier())      # True (valid variable name)
print("first_name".isidentifier())# True
print("var123".isidentifier())    # True
print("_hidden".isidentifier())   # True
print("123var".isidentifier())    # False (cannot start with digit)
print("my var".isidentifier())    # False (contains space)
print("class".isidentifier())     # True (but it's a reserved keyword)

print("Hello World".istitle())       # True
print("This Is Python".istitle())    # True
print("Hello world".istitle())       # False (second word not capitalized)
print("HELLO WORLD".istitle())       # False (all letters uppercase)
print("Python3 Programming".istitle()) # True (numbers don't affect title case)
print("123 Python".istitle())        # True (numbers ignored, next word capitalized)

words = ["Python", "is", "fun"]
result = " ".join(words)   # space as separator
print(result)              # Output: Python is fun

items = ["apple", "banana", "cherry"]
result = ", ".join(items)
print(result)              # Output: apple, banana, cherry

text = "Python"
result = text.ljust(10)
print(result)          # Output: 'Python    '
print(len(result))     # Output: 10

text = "Python"
result = text.ljust(10, "-")
print(result)          # Output: 'Python----'

text = "###Python###"
result = text.lstrip("#")
print(result)        # Output: 'Python###'


table = str.maketrans("abc", "123");
text = "abcghabc";
trans_text = text.translate(table)
print(trans_text)

table = str.maketrans({'a':'1', 'b':'2', 'c':'3'});
text = "abcghabc";
trans_text = text.translate(table)
print(trans_text)


text = "python is awesome"
result = text.partition("is")
print(result)

text = "I like Python. Python is powerful."
result = text.replace("Python", "Java")
print(result)
text = "apple apple apple"
result = text.replace("apple", "orange", 2)
print(result)

text = "Python is easy, Python is powerful"
pos = text.rfind("Python")
print(pos)

text = "Hello World"
pos = text.rfind("Python")
print(pos)

text = "hello"
result = text.rjust(10)
print(result)

text = "Python is easy and Python is powerful"
result = text.rpartition("and")
print(result)

text = "Python is fun to learn"
result = text.rsplit()
print(result)

text = "apple,banana,orange,grape"
result = text.rsplit(",", 2)
print(result);

# Python Booleans 
print(10>9);
print(1>2)

a=200
b=33

if b>a:
   print("b is greater than a")
else:
   print("b is not greater than a")

print(bool("Hello"))
print(bool(15))
x = "Hello"
y = 15

print(bool(x))
print(bool(y))



bool("abc")
bool(123)
bool(["apple", "cherry", "banana"]);

class myclass():
  def __len__(self):
    return 0

myobj = myclass() 
print(bool(myobj));  

def myFunction() :
  return True

print(myFunction())


if myFunction():
   print("YES!")
else:
   print("NO!")

x = 200
print(isinstance(x,int))

print(10+5)

# Arithmetic operators

a=15;
b=4;

print("Addition:", a+b);
print("Subtraction:", a - b);
print("Multiplication:", a * b);
print("Division:", a / b) ; 
print("Floor Division:", a // b);
print("Modulus:", a % b);
print("Exponentiation:", a ** b)

#Operator Precedence 

print((6+3)- (6+3))
print(100 + 5 * 3)
print(5 + 4 - 7 + 3)

# List - ordered, changeable, allows duplicates
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1,list2,list3)

list1 = ["abc", 34, True, 40, "male"]
print(list1)

mylist = ["apple", "banana", "cherry"]
print(type(mylist))

thisList = list(("a","b", "c"));
print(thisList)

# Tuple - ordered , unchangeable, allows duplicates.

numbers = (10,20,30,10)
print(numbers)
#numbers[1] = 25;
#print(numbers)


# Set - unorderd, no duplicates

colors = {"red", "green", "blue", "red"};
print(colors) 

#Dictionary — Key-value pairs
person = {
    "name": "Prabhat",
    "age": 34,
    "city": "Bankura"
}

print(person["name"])       # Prabhat
person["age"] = 35          # Update value
person["country"] = "India" # Add new key-value pair
print(person)


# Access items 

thislist = ["apple", "banana", "cherry", "Orange", "kiwi", "melon", "mango"];
print(thislist[1])

#Nagative Indexing 
print(thislist[-2])

# Range of Indexes
print(thislist[2:5])
print(thislist[:4])

# Range of Negative indexes

print(thislist[-4:-1])

# Check if Item Exists

if "apple" in thislist:
   print("Yes, 'apple' is in the fruits list")

# Python - Change List Items

# Change Item Value

fruits = ["Apple", "Banana", "Cherry"]
fruits[1] = "Blackberry"
print(fruits)

# Change a Range of Item Values
fruits = ["Apple", "Banana", "Cherry"]
fruits[1:3] = ["Blackberry", "Watermelon"]
print(fruits)

# Insert Items 

fruits = ["apple","banana", "cherry"]
fruits.insert(0,"watermelon")
print(fruits)

# Append Items
fruits.append("orange")
print(fruits)

# Extend List
fruits1 = ["mango", "pineapple", "papaya"]
fruits.extend(fruits1)
print(fruits)

# Add Any Iterable
fruits2 = ("kiwi", "dragon")
fruits.extend(fruits2)
print(fruits)

# Remove Items
fruits.remove("banana")
print(fruits)

fruits.pop(0)
print(fruits)

# remove last item
fruits.pop()
print(fruits)

# delete item
del fruits[0]
print(fruits)

#del fruits
#print(fruits)

# Clear the List 
#fruits.clear()
#print(fruits)

# Python - Loop Lists
# Loop Through list

for x in fruits:
   print(x)

# Loop Through the index numbers
for i in range(len(fruits)):
   print(fruits[i])

# Using a while loop

i = 0
while i< len(fruits):
   print(fruits[i])
   i = i+1

# Loop using list comprehension

[print(x) for x in fruits]


# List Comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
   if "a" in x:
      newlist.append(x)

print(newlist)

# In one line code
newlist1 = [x for x in fruits if "a" in x];
print(newlist1)

newlist2 = [x for x in fruits if x != "apple"]
print(newlist2)

newlist = [x.upper() for x in fruits]
newlist = ['hello' for x in fruits]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

# Python- Sort Lists

# Sort List Alphanumerically
list = ["orange", "mango", "kiwi", "banana"]
list.sort()
print(list)

# Sort the list numerically:

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# Sort Descending
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

# Customize Sort Function

def myfunc(n):
   return abs(n-65)

list = [100,50,65,82,23]
list.sort(key= myfunc)
print(list)

# Reverse Order

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

# Python copy Lists

# use copy() method

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# use slice() method
thislist1 = ["a", "b", "c", "d"]
list1 = thislist1[:]
print(list1) 

# Python - Join Lists
#join two lists

list1 =["a", "b", "c"]
list2 = [1,2,3,4]
list3 = list1 + list2
print(list3)

for x in list2:
   list1.append(x)
print(list1)

# extend()
list1.extend(list2)
print(list1)






