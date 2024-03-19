# 1.) Write a Python script to generate and print a dictionary that 
# contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 2.)Find the uncommon words from 2 strings

# # s1 = "Hello how are you"
# s2 = "Hello how is"

# 3.)Wrire a code print the 8th fibanochi number


# ! Eg:3
'''
def profile(name,age,place):
    txt="my name is {}.Iam {}. years old.Iam from {}."
    print(txt.format(name,age,place))
profile("kousik",20,"Banglur")

my name is kousik.Iam 20. years old.Iam from Banglur.
'''

# Eg:4
# functions with return statement
# return
#1.) A variable declared inside function can be accessed outside the function using return
#2.) return does not print anything
#3.) we cannot write any code below return statement


'''
def f1():
    z = 8
f1()
print(z) # error---------> cannot use outside function
'''
'''
def f1(a,b):
    c = a*b
    return c
#print(f1(6, 8))
obj = f1(6, 8)
obj1 = f1(4, 6)


def gracemark(object):
    print(object+4)
gracemark(obj)
gracemark(obj1)

52
28
'''
'''
def palindrome(n):
       print(n)


a = int(input("Enter the value:"))
palindrome(a)

# ? Problem:1
def palindrome(n)
string = srt(n)
    rev = str(n)
    if string==rev:
         print(n, "palindrome")
    else:
         print("not palindrome")
         a  =  int(input("Enter the vslue:"))
         palindrome(a)
'''
# ? based on the declaration of parameter and args
# ? function are divide in to 5 catagories

#posible args
#key words args
# default args
#varible lenth args
#key words avriable lenth args

# * Positional args
#? The position of parameter ahve to be same as position as arguments
#! Eg:1
'''
def profile (name,phone,mark):
    txt = "My name is {}.My phone number is{}.I got {} marks."
    print(txt.format(name,phone,mark))

    profile(9573558615,"aravind",95)# unexpected output
'''
'''
# * Keyword args
#!Eg:1
To overcome the disadvantage of position args ,we keyboard args
It is the process of intialising the paremeter with the args while calling the
Functon
def profile (name,phone,mark):
    txt = "My name is{}.my phone number is{}.I got{} marks."
    print(txt.format(name ,phone,mark))

    profile (name"aravind",123456789,marks=95) # error
    profile(123456789,name="aravind",mark95)
  profile (name"aravind",123456789,marks=95) # error--> positional args follow keyboard   
   profile(123456789,name="aravind",mark95) #! error--> name has multiple values
   profile("aravind",mark=95,phone 123456789)

(*>#): positive integer
(#>*): negative integer
(#=*): 0
Example 1:
Input 1:

###***   -> Value of S
Output :

0   → number of * and # are equal
'''
'''


# ! Exception
def profile(name, phone, place="Kadapa"): # error --> because default args should not follow positional param
   if place == "kadapa" or place=="kADAPA" or place=="Kadapa":
     txt="My name is{}. My phone number{}. I got{} marks{}."
     print(txt.format(name,phone,place))
   else:
        print("You are not eligible to Signup")
profile("aravind",9876543210)
'''
'''
# * variable length params
# ! Eg:1
#To pass more then 1 arg to a paremeter means we use variable length args
# To convert normal paremeter to variable length param, add to ther prefix of param

#name="aravind", " hareesh ", " sadugudu "
#print(name)


def profile(*name):
    for val in name:
        print(" My name is",val)
profile("aravind", 'hareesh', 'basha')


# ! Eg:2
def profile (*name, age):
    for val in name:
        print("My name is ",val,"my age is ",age)
profile(", 'name2', 'name3', 26) # error --> age has no args

        
# * keyword variable length args
# ! Eg:1
def price(**price_list):
    print(price_list)

price(shirt=1000, iphone=80000)

d1 = ("a":100,"b":200, "c":300)
d1 = dict(a=100,b=200, c=300)
print(d1)
(*>#): positive integer
(#>*): negative integer
(#=*): 0
Example 1:
Input 1:

###***   -> Value of S
Output :

0   → number of * and # are equal




# ! Exception
def profile(name, phone, place="Kadapa"): # error --> because default args should not follow positional param
   if place == "kadapa" or place=="kADAPA" or place=="Kadapa":
     txt="My name is{}. My phone number{}. I got{} marks{}."
     print(txt.format(name,phone,place))
   else:
        print("You are not eligible to Signup")
profile("aravind",9876543210)

'''
'''
# * variable length params
# ! Eg:1
#To pass more then 1 arg to a paremeter means we use variable length args
# To convert normal paremeter to variable length param, add to ther prefix of param

#name="aravind", " hareesh ", " sadugudu "
#print(name)


def profile(*name):
    for val in name:
        print(" My name is",val)
profile("aravind", 'hareesh', 'basha')


# ! Eg:2
def profile (*name, age):
    for val in name:
        print("My name is ",val,"my age is ",age)
profile("aravind", 'name2', 'name3', 26) # error --> age has no args

        
# * keyword variable length args
# ! Eg:1
def price(**price_list):
    print(price_list)
'''

#n=5
#{1:1,2:4,3;9,4:16,5:25}

'''
n=int(input("Enter the number:"))
d1 = {}
for val in range(1, n+1):
    d1[val]= val**2
print(d1)

Enter the number:5
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
'''
'''
def dict1(n):
    d1 = {}
    for val in range(1, n+1):
        d1[val]= val**2
    print(d1)
dict1(5)

{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
'''

'''
d1={"a":100,"b":200,"c":300}
d1 = dict(a=100,b=200,c=300)
print(d1)

{'a': 100, 'b': 200, 'c': 300}
'''

# ! ---------> object oriented programming
# The panadigms of objects oriented progarmming are


# class
# objects
# inheritance
# polymorphism
# abstraction
# encapsulation

# ! Class is a blue print of an object

#l1=[1,2,3,4,5,6]


# Eg:1
'''
class c1:
    name1 = "aravind"
    print(name1)

aravind
'''
# Eg:2
'''
class person:
    name = "aravind"

c = person()
print(c.name)

aravind
'''

# c = person() # c as object
# The process of creation of an object is called as Instantiation
# print(c.name)


#Eg:3
# create a method
# when function is creating with a class is called as method

'''
class person:
    def display(person): # it is a method
        print("Hello welcome to classes")

p = person()
p.display()

Hello welcome to classes
'''

# eg:4
# method with parameter
'''
class person:
    def display(person,name,age):
        print(name,age)

p = person()
p.display("aravind",20)

aravind 20
'''
'''
# Eg:5

class person:
    fname = "aravind" # attribute or static variable
    lname = "paluru"
    
    def display(person):
        print(person.fname)

    def full_name(person):
        print(person.fname+" "+person.lname)
        

p = person()
p.first_name()
p.full_name()

'''



# eg 6.)

class profile :
       def_init_(self) :
              print("hey")




































 
