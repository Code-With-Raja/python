# Sets

myset = {"apple", "banana", "cherry"}
print(myset)

# unchangable
thisset = {"apple", "banana", "cherry", "apple",1,2,0}
print(thisset);

# get length of a set
print(len(thisset))

# set items - data types
# string, int, boolean
set1 = {"apple", "banana", "cherry"};
set2 = {1,5,7,9,3};
set3 = {True, False, False}
set = {"abc", 34, True, 40, "male"}

# type()
print(type(set1))
print(type(set2))


#Access Items
for x in thisset:
    print(x)

print("banana" in thisset)

print("banana" not in thisset)

# Add Item

thisset = {"a","b","c"}

thisset.add("o")
print(thisset)

# Add sets
tropical = {"m","j","h"}

thisset.update(tropical)

print(thisset)

# Remove Item 
thisset.remove("a")
print(thisset)

# pop()
x = thisset.pop()
print(x)
print(thisset)

# clear()
thisset.clear()
print(thisset)

# Python - Loop sets
# Loop items
thisset = {"potato", "Dal", "rice"}
for x in thisset:
    print(x)

# Join sets
set1 = {"a","b","c"};
set2 = {1,2,3};

set3 = set1.union(set2);
print(set3)

# |
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)

# Intersection
set1 = {"apple", "banana", "cherry"};
set2 = {"google", "microsoft", "apple"};
set3 = set1.intersection(set2);
print(set3) # print- apple

set3 = set1 & set2
print(set3) # print- apple

# intersection_update
set1.intersection_update(set2)
print(set1)

# difference
set1 = {"apple", "banana", "cherry"};
set2 = {"google", "microsoft", "apple"};
set3 = set1.difference(set2);
print(set3)
set3 = set1-set2
print(set3)
# differnence_update
set1.difference_update(set2)
print(set1)
#Symmetric Differences
set3 = set1.symmetric_difference(set2)
print(set3)
set3 = set1 ^ set2;
print(set3)
#Symmetric Differences_update
set1.symmetric_difference_update(set2);
print(set1)

# Python frozenset
# create a frozenset
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))