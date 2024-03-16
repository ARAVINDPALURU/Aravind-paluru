# 1.) Python program to capitalize the first and last character of each 
# word in a string
# 2.) Input : 128
# Output : Yes
# 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# 3.)l1=[1,2,3,4], l2=[5,6,7,8]
# Add both l1 and l2, ans=[6, 8, 10, 12]


# 1.)
#s1 = "hello world"
#fst = s1[0].upper()
#lst = s1[-1].upper()
#print(fst+s1[1:len(s1)-1]+lst)

#Hello worlD

# 2.)
#n=128
#while n!=0:
#   rem = n%10
#    print("the value of reminder :",rem)
#   print("the value of n :",n)
#    n = n/10

'''   
the value of reminder : 8
the value of n : 128
the value of reminder : 2.8000000000000007
the value of n : 12.8
the value of reminder : 1.28
the value of n : 1.28
the value of reminder : 0.128
the value of n : 0.128
the value of reminder : 0.0128
the value of n : 0.0128
the value of reminder : 0.00128
the value of n : 0.00128

'''

'''
n = 128
temp = n
f1 = 0
while n! = 0:
    rem = n%10
    check = temp % rem
    if check ! = 0:
        f1 = 1
    n = n//10
if f1==0:
    print("yes")
else:
    print("n0")

'''



# 3.)
#l1 = [8, 9, 0, 7]
#l2 = [7, 6, 5, 4]
#l3 = [ ]
#for val in range(len(l1)):
#   ans = l1[val]+l2[val]
#   l3.append(ans)
#print(l3)

#[15, 15, 5, 11]


# ! -----> set
# characteristics of set
'''
1.) set can be created using{}
2.) The element inside set are not indexed
3.) Does not allow duplicate values
4.) it unordered
5.) heterogenous
6.) mutable or changable

'''



# Eg:1
'''
s1 = {9, 9, 89, 7.76, 8+7j, (8, 7, 5), "truck", 'e'}
print(s1)

{89, (8, 7, 5), 'e', 7.76, 9, (8+7j), 'truck'}
'''

#eg:2
'''
s2={5,8,9,[9,0]}
print(s2) #-----------> error
'''

#eg:3
#min(),max(),len()

#eg
# to add element inside list
'''
s1={8,78,67,'u'}
#add()
s1.add(43)
print(s1)

{67, 8, 43, 'u', 78}
'''

#update
'''
s1={8,78,67,'u'}
s1.update([9,0])
print(s1)

{0, 67, 8, 9, 78, 'u'}
'''

# to delete element iside list
'''
s1={8,78,67,'u'}

# pop()
s1.pop()
print(s1)

{67, 'u', 78}
'''

#remove
'''
s1.remove(78)
print(s1)

{8, 67, 'u'}
'''

#discard
'''
s1={8,78,67,'u'}
s1.discard(67)
print(s1)

{8, 'u', 78}
'''

# clear()
#l1 = {}
#print(type(l1)) #---> datatype is dict

#s1 = set() # to create empty set
#print(type(s1))


'''
s1 = {8,9,0}
s1.clear()
print(s1)
'''

'''
s1 = {8,9,0}
del s1
print(s1)
'''
# del s1
# print(s1)


# * join the sets
'''
s1 = {9,0,8}
s1 = {9.90,"card",'t',56}
#union()
s3 = s1.union(s2)
print(s3)
'''
# * intersection() --> to get common elements inside set
'''
s1 = {4,5,6}
s2 = {5,6,7,8}
print(s1.intersection(s2))

{5, 6}
'''
# * difference()
'''
s1 = {4,5,6}
s2 = {5,6,7,8}
print(s1.difference(s2))
print(s2.difference(s1))
print(s1.symmetric_difference(s2))

{4}
{8, 7}
{4, 7, 8}
'''

# isdsjoit(), issubset(), issuperset()
'''

s1 = {8,9,0}
s2 = {6,7,5,8,9,0}
print(s1.issubset(s2))
print(s2.issuperset(s1))

True
True
'''

#s1 = {1,2,3,4,5}
#s2 = {3,2,7,8,9}
#n1 = {1,2,3}
#for val in s1 :
#   if val in s2 :
#        print("its joint set")


#its joint set
#its joint set

# ? o/p ---->its a joint set
#  ! --------> dictionary

# ! -----> problem : 1

'''

s1 = {1,2,3,4,5}
s2 = {3,2,7,8,9}
for val in s1 :
    if val in s2 :
        str1 = "its joint set"
print(str1)

its joint set

'''

# ! ------> dictionary
# eg : 1

'''
d1 = {1:100, 'a':200, 4.5:"hello"}
print(d1)
print(len(d1))

{1: 100, 'a': 200, 4.5: 'hello'}
3
'''

'''

d1 = {1:100, 'a':200, 4.5:"hello"}
marks_stud1 = {"English": 79, "maths":20, "physics": 60}
print(d1)
print(len(d1))

d1 = {1:100, 'a':200, 4.5:"hello"}

'''

# ? Char of dictionary
# 1.) Have to be surrounded by{}
# 2.) It have to be in the form of key, value pair
# 3.) It is mutable
# 4.) Duplicate keys are not allowed, duplicate value are allowed
# 5.) It is unindexed
# 6.) It is ordered
# 7.) key does not allow mutable dat types , values allow mutable data type

'''
d1 = {1:100, 2:200, 3:300, 4:400}
# to access element in dictionary

print(d1)
#or
# To access the values
print(d1[1]) #o/p --->100
'''
'''
# ? some common functions
#len(),min(),max()
print(min(d1))
print(max(d1))
'''
'''
# ? To find min, max based on values
print(min(d1.values()))
print(max(d1.values()))
'''
'''
# ? dictionary based functions
# to add elements(key and value pair) in dict
d1 = {1:100, 2:200, 3:300, 4:400}
d1[5] = 500
print(d1)
'''
'''
# ? To replace a value in dictionary
d1 = {1:100, 2:200, 3:300, 4:400}
d1[2]="mango"
print(d1)
'''
'''
# ? delete element from dictionary
d1 = {1:100, 2:200, 3:300, 4:400}
#popitem ---> to delete last key value pair in dict
d1.popitem()
print(d1)
print(d1.popitem())
'''
'''
pop()
d1.pop(2) # 2 is the key in dictionary
print(d1)

clear(),del
update()
join 2 dictionary
d1 = {1:100, 2:200, 3:300, 4:400}
d2 = {"a":"apple","b":"boy","g":"game"}
d1.update(d2)
print(d1)
'''

'''
#get() ---> used to get the value from a key
d1 = {1:100, 2:200, 3:300, 4:400}
#print(d1[3])
#print(d1[90])
print(d1.get(90))


#to print all the keys
print(d1.keys())
print(type(d1.keys()))
'''

# ! problem: 1

'''
n = int(input("enter num of times : "))
integer=[]
float_value =[]
string=[]
for val in range(n):
    value = eval(input("enter the num of values: "))
    if type (value)==int :
        integer.append(value)
    elif type (value) ==float :
        float_value.append(value)
    elif type (value) == str :
        string.append(value)
    else:
        print("pls provide data in int, float, string")
print(integer)
print(float_value)

enter num of times : 6
enter the num of values: 5462
enter the num of values: 65262
enter the num of values: 6263
enter the num of values: 223
enter the num of values: 2323
enter the num of values: 21562
[5462, 65262, 6263, 223, 2323, 21562]
[]

'''

'''

n = int(input("enter num of times : "))
integer=[]
float_value =[]
string=[]
for val in range(n):
    value = eval(input("enter the num of values: "))
    if type (value)==int :
        integer.append(value)
    elif type (value) ==float :
        float_value.append(value)
    elif type (value) == str :
        string.append(value)
    else:
        print("pls provide data in int, float, string")
print(integer)
print(float_value)
print(string)

enter num of times : 3
enter the num of values: "hello"
enter the num of values: 2.3
enter the num of values: 5695
[5695]
[2.3]
['hello']

'''

# return a set of elements prsent in set A or B but not both
'''

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60 ,70}
set3 = set()
for val in set1:
    if val not in set2:
        set3.add(val)
for val in set2:
    if val not in set1:
        set3.add(val)
print(set3)

{10, 20, 70, 60}

'''

# ! ------> problem 3
'''
l1 = [1,2,3,4]
l2 = ["a" , "b" , "c" , "d"]

d1 = {}
for val in range(len(l1)):
    d1[l1[val]] = l2[val]
    print(d1)

{1: 'a'}
{1: 'a', 2: 'b'}
{1: 'a', 2: 'b', 3: 'c'}
{1: 'a', 2: 'b', 3: 'c', 4: 'd'}  

'''

l1 = [1,2,3,4]
l2 = ["a" , "b" , "c" , "d"]

d1 = {}
for val in range(len(l1)):
    d1[l1[val]] = l2[val]
print(d1)


#1.)swap elements in string list 
# the original list is : ['Gfg' , 'is' , 'best' ,'for' , 'geeks']
# list after performing charcahter swaps : [ 'efg' , 'is' , 'bGst' , 'for' , eGGKs' ]














































