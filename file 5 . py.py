#------->  common functions for list

#l1 = [6, 7, 8, 9, 0]
#print(len(l1))
#print(max(l1))
#print(min(l1))
#5
#9
#0

#l1 = [6,7,8,9, "p", "u"]
#print(max(l1)) #error coz its a combination of list and string
#print(min(l1))  #error coz its a combination of list and string

#l1 = [6,7,8,9,0,8.89,-5,0.78]
#print(min(l1))

#l1 = [6,7,8,9,0,8.89,-5,0.78]
#index() ---> to get index value of specific element
#print(l1.index(9))

#l1 = [6,7,8,9,0,8.89,-5,0.78]
#count() ---> how many num of times an element is repeated
#print(l1.count(6))


# ! some functions which is specifically used for list

# To add element inside list
# ? insert () ---> to add element at specific index positions
#l1 = [6,6,6,7,8,9,0,8.89,-5,0.78]
#l1.insert(2, "cars")
#print(l1)


#to delete an element from list
#l1 = [6,6,6,7,8,9,0,8.89,-5,0.78]

# pop() ----> last element will be deleted
# 11.pop()
# print(11)

#pop(index_value) --> used to delete element at specific index
#l1.pop(4) # 4 is index value
# print(l1)

# *remove(element) --> used to delete element directly
# l1.remove(8.89)
# print(l1)

# *clear() ---> to complete delete all element in list
#l1.clear()
#print(l1)

# clear() --> to complete delete all element in list
'''
l1 = [2,3,2,3,4,32,6.76,98.5,-94]
l1.clear()
print(l1)

()
'''

#del ---> to delete the list
'''
l1 = [2,3,2,3,4,32,6.76,98.5,-94]
del(l1)
print(l1)
'''
# ----> jion 2 lists
'''
l1=[9,0,8]
l2=["p","o","t",34]
print(l1+l2)

[9, 0, 8, 'p', 'o', 't', 34]
'''
# extend() ---> to combine 2 lists
'''
l1=[9,0,8]
l2=["p","o","t",34]
l1.extend(l2)
print(l1)

[9, 0, 8, 'p', 'o', 't', 34]
'''

# ? ---> copy()
# l1 = [6, 7, 8,9, 3]
# l2 = l1.copy()
# print(l2)
# print(l1)

# print(id(l1))
# print(id(l2))

# ! -----> diff between shallow copy and deep copy
# shallow copy
'''
import copy
l1 = [8, 9, 0,[5, 6], [3, 2, 1] ]
l2 = copy.copy(l1)
l1.append(890)
print(l1)
print(l2)

[8, 9, 0, [5, 6], [3, 2, 1], 890]
[8, 9, 0, [5, 6], [3, 2, 1]]

'''

# * deep copy
''' 
import copy
l1 = [8, 9, 0,[5, 6], [3, 2, 1] ]
print(l1[-1][1])
l2 = copy . copy (l1)
l1[-1].append('cars')
print(l1)
print(l2)

2
[8, 9, 0, [5, 6], [3, 2, 1, 'cars']]
[8, 9, 0, [5, 6], [3, 2, 1, 'cars']]
'''

'''
import copy
l1 = [8, 9, 0,[5, 6], [3, 2, 1] ]
#print(l1[-1][1])
l2 = copy . deepcopy (l1)
l1[-1].append('cars')
print(l1)
print(l2)


[8, 9, 0, [5, 6], [3, 2, 1, 'cars']]
[8, 9, 0, [5, 6], [3, 2, 1]]

'''

# ? sort ------> arrange elements in list in ascending or descending order

#l1 = [9, 7, 45, 0, -6, 5, 12]
#l1.sort()  -----> to arrange in ascending order 
#print(l1)

#[-6, 0, 5, 7, 9, 12, 45]

#l1 = [9, 7, 45, 0, -6, 5, 12]
#l1.sort(reverse=True) ------. to arrange in descending order
#print(l1)


# l1 = ['z','i', 'o', 'p', 9]
# l1.sort()
# print(l1) # ---> error

# list constructor
# list() --> to conver other collection datatype to list
# l3 = ((8, 9, 0))
# print(list(l3))

# l4 = (8, 9)
# print(list(l4))

# ! ---> nested list
l1=[8,9,[0,8,7],["p","a","y"],[7,"v"]]
# ! ----> nested list
# M:-1
'''
l1=[8,9,[0,8,7],["p","a","y"],[7,"v"]]
print(l1[3][1])
'''
# M:-2
'''
l1=[8,9,[0,8,7],["p","a","y"],[7,"v"]]
print(l1[1:5])
'''
# M:-3
'''
l1=[8,9,[0,8,7],["p","a","y"],[7,"v"]]
print(l1[1:-1])


'''

# to delete "t" from l1
'''
l1 = [8,9,[0,8,7],["p","o","y"],[8,'t']]
l1[-1].remove('t')
print(l1)

[8, 9, [0, 8, 7], ['p', 'o', 'y'], [8]]
'''

# combine these ["p","o",'y'],[8,'t']
'''
l1=["p","o",'y']
l2=[8,'t']
l1.extend(l2)
print(l1)

['p', 'o', 'y', 8, 't']
'''

# -------> Tupule
# char of tuple

#1.) tuple have to be surrounded by ()
#2.) The element inside tuple are not changable
#3.) The element inside tuple are indexed
#4.) The element will excuted in order
#5.) It is heterogenous
#6.) It allow duplicate element

# eg :
#t1 = (8, 8, 9, 6, 5.78, [9, 0], (6, 8), "hey", 9+6j)
#print(type(t1))

#(8, 8, 9, 6, 5.78, [9, 0], (6, 8), 'hey', (9+6j))
#<class 'tuple'>

# ? indexing,slicing are all same as list
'''
l1 = (8)
print(type(l1))
 
<class 'int'>
'''

'''
l1 =(8,)
print (type( l1))


<class 'tuple'>

'''

'''
t2 = 8,
print(type(t2))

<class 'tuple'>
'''

# len(), min(), max(), index(),count() ----> all the same as list
# to add element inside touple ---->cannot add
# cannot delete any element from tuple


# * join two tuples
'''
t1 = (8, 9, 0)
t2 = (6, 7, 8)
print (t1+t2)

(8, 9, 0, 6, 7, 8)
'''

# To add all element inside list and tuple
'''
sum( )
l1 = (8, 9, 7, 6)
print(sum(l1))
'''



# * sort tuple
'''
t1 =  (8, 9, 0, 89, 12)
print(tuple(sorted(t1)))
print(tuple(sorted(t1,reverse=True)))


(0, 8, 9, 12, 89)
(89, 12, 9, 8, 0)
'''

# ? iterate list and tuples

# * iterate list and tuples

'''
l1 = [9, 8, 0, 6, 5]
for i in l1 :
    print(i)

9
8
0
6
5

'''

# * iterate based on index value

'''
l1 = [9, 8, 0, 6, 5, 8, 56]
for i in range (0, len(l1)):
    print(l1[i])


9
8
0
6
5
8
56

'''

#  ------> strings
#s1 = '0'
#print(type(s1))

#s1 = 'u'
#print(type(s1))

'''
s1 = "hello world"
# * to access string
print(s1)

hello world
'''


#####
'''
s1 = "hello world"
print(s1)
# indexing and slicing -----> same as list and tuple
print(s1[0:5])

hello world
hello
'''
# len( ) , min ( ) ,max( ), index( ) , count( )

'''
s1 = "hello world"
print(max(s1))
print(len(s1))
print(min(s1))


w
11
 
'''

# functions of string
'''
s1="hello world"
# to convert all charecteres tyo upper case
print(s1.upper())

HELLO WORLD
'''
'''
s1="HELLO WORLD"
# to convert all cases in lower case
print(s1.lower())

hello world
'''

# strip()
'''
s1=" where are you?"
print(s1)

 where are you?
'''
# strip() ---> to eliminate the space in begining and end of string
'''
s1=" where are you?"
print(s1.lstrip())   ---> to eliminate the space in begining
print(s1.rstrip())   ---> to eliminate the space in ending
print(s1.strip())

where are you?
'''

# spilit() ---------> to split the words in string basesd on a charecter
'''
s1=" where are you?"
print(s1.split())
print(s1.split("r"))
print(s1.split("e"))

['where', 'are', 'you?']
[' whe', 'e a', 'e you?']
'''
# replace()---->
'''
s1=" where are you?"
print(s1.replace('r','&&'))

 whe&&e a&&e you?
'''
# swapcase()---> to convert captital to small and small to capital at a time
'''
s1="HEY there"
print(s1.swapcase())

hey THERE
'''

# title() --> to erite the string in format of title
'''
s1='never give up'
print(s1.title())

Never Give Up
'''
# jion the strings
'''
s1='hello'
s2='world'
print(s1+s2)

helloworld
'''

#splitlines() ---> used to split the string based on lines
print(s1.splitlines())

# find() ---> used to find the index based on a character
#s1 = "hello world"
#print(s1.find('z'))
#print(s1.index('z'))

# join() ---> 
l1 = ["hey", "there"]
print(" ".join(l1))
print("$".join(l1))

s1 = "Welcome to all"
print(s1.endswith('l'))
print(s1.startswith('W'))


s1 = "67"
print(type(s1))
print(s1.isdigit())

# Print the string in reverse manner
s1 = "Welcome to all"
print(s1[::])

'''

# ! ---> Strings
s1 = "0"
print(type(s1))

s1 = "u"
print(type(s1))

s1 = "hello world"
# to access string
print(s1)
# indexing and slicing ---> same as list and tuple 
print(s1[0:5])

# ---> common function

# len(), min(), max(), index(), count()
s1 = "hello world"
print(len(s1))
print(max(s1))
print(min(s1))

#ord() ---> used to find the ASCII value of a character
s1 = 'u'
print(ord(s1))

# Functions of string
s1 = "hello world"
#to convert all characters to upper case
print(s1.upper())

#to convert all characters to lower case
print(s1.lower())

# strip() ---> to eliminate the space in beginning and end of string
s1 = "where are you?"
print(s1.lstrip())
print(s1.rstrip())
print(s1.strip())


#split() --> to split the words in string based on a character
s1 = "where are you?"
print(s1.split())
print(s1.split("r"))
print(s1.split("w"))
print(s1.count('e'))

# replace() --->  to replace a specific char in the string
s1 = "where are you?"
print(s1.replace('r', '&&'))

# swapcase() ---> to convert capital to small and small to capital at a time
s1 = "HEY there"
print(s1.swapcase())

# title() ---> to write the string in format of title
s1 = 'never give up'
print(s1.title())

# capitalize()
s1 = 'never giveUP'
print(s1.capitalize())

# join the strings
s1 = "hello"
s2 = 'world'
print(s1+s2)

s1 = how are you
i am fine
hey there
'''

#splitlines() ---> used to split the string based on lines
print(s1.splitlines())

# find() ---> used to find the index based on a character
#s1 = "hello world"
#print(s1.find('z'))
#print(s1.index('z'))

# join() ---> 
l1 = ["hey", "there"]
print(" ".join(l1))
print("$".join(l1))

s1 = "Welcome to all"
print(s1.endswith('l'))
print(s1.startswith('W'))


s1 = "67"
print(type(s1))
print(s1.isdigit())

# Print the string in reverse manner
s1 = "Welcome to all"
print(s1[::])
'''
'''
'''
#!----> Eg:1
# wap to find the number of lower case letters
'''

s1 = "hey there you aRE"
count = 0
for i in s1:
    if i in lower():
        count +=1
 print("the total num lower case letters:",count)
















  


