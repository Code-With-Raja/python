# append()
fruits =["apple", "banana", "cherry"]
print(fruits)
fruits.append("mango")
print(fruits)

# clear()
#fruits.clear()
#print(fruits)

# copy()
fruits.copy()
print(fruits)

#count()
count = fruits.count("banana")
print(count)

# extend()
fruits.extend(["orange", "coconut"])
print(fruits)

# index()
possition = fruits.index("orange", 2,5);
print(possition)
print(fruits.index("banana", 0,4))

# insert()
fruits.insert(2, "papaya")
print(fruits)

# pop()
fruits.pop(0)
print(fruits)

# remove()
fruits.remove("mango")
print(fruits)

# reverse()

fruits.reverse()
print(fruits)

# sort()
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)

# Python tuples
thisTuple = ("apple", "orange", "banana");
print(thisTuple)
print(len(thisTuple))

# Create Tuple with One Item

oneTuple = ("papaya",)
print(oneTuple)

# Tuple Items - Data Types

tuple1 = ("apple", "banana", "orange");
tuple2 = (1,2,3,4,5);
tuple3 = (True,False, True)

tiple1 = ("abc", 34, True, 40, "male") 

# type()
mytuple = ("a","b","c")
print(type(mytuple))

# The tuple() Constructor
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

# Python - Access Tuple Items
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# Change Tuple Values
x= ("apple", "banana", "cherry")
y = list(x);
y[1]= "orange";
x = tuple(y)

print(x)

# Add Items
y= list(x);
y.append("coconut")
x = tuple(y)

print(x)

# Remove Items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

print(thistuple)

# Python - Unpack Tuples

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
 
# Using Asterisk

fruits = ("apple", "banana", "cherry", "strawberry", "rasberry")
(green, *yellow, red) = fruits

print(green)
print(yellow)
print(red)

# python- Loop Tuples

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)
# Loop through the Index Numbers

for i in range(len(thistuple)):
    print(thistuple[i])

# Using a while Loop

i = 0;
while i < len(thistuple):
    print(thistuple[i])
    i= i+1

