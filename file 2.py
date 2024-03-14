'''
a, b=c=7,8
print(a)
print(b)
print(c)

a=b,c, = 4,2
print(a,b,c)

#--->swapping of variables
a=7
b=5
print(a,b)

# Eg:1
# temp=a #temp=7
#a=b   #a=5
#b=temp#b=7

##a=5,b=7
#print(a,b)

#Eg:2
#a=a+b #a=12
#b=a-b #b=12-7=5
#a=a-b #a=12-5=7

#print(a,b)

# a, b=b, a # only in python
# print(a,b)

a=a*b #a=35
b=a/b #b=35/7=5.0
a=a/b #a=35/5=7.0
print(int(a),int(b))

'''
'''
a = 7
b = 5
a= a*b
b=a/b
a=a/b
print(int(a) ,int(b))
'''
'''
--->keywords
keywords are preserved words which provides special meaning to compiler or interchanger
'''
'''
import keyword
print (keyword.kwlist)


['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
'''
'''
import keyword
print( keyword.kwlist)
print(len(keyword.kwlist))
print(type(keyword.kwlist))

['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

<class 'list'>
'''
'''
#----->literal is the constant value assigned to a variable
a variable is considers to be constant when it defines  in caps
'''
'''
a=78 # nis variable
a=78 # uis constant
'''
'''
11= [9,8,0]
11= [6, 7 ,8 ,0]
11=89
'''
'''
hash( )-----> it creates a hack value for constant data type and provides error for vnon constant datatypes

n1=89=7j
print(hash(n1))

7000110

f1= [7 , 8 , 9]
print(hash(f1))

'''
'''
#!---> operators
#operaters are symbols which are used to perform various operations between 2 or more operations 

#Arthimetic
#Assignment
#Logical
#Relational or Comparison
#bitwise
#identity
#membership
'''
'''
#-----> Arthimetic --->+, -, * , / ,% , // ,**

eg : 1
a=8
b=6
c=5
print (a+b+c)

'''
'''
# input ( )----> used to get routine  input
n1=input("enter the value:")
print (n1)

'''
'''
https://medium.com/@a.tavallaie/python-programming-libraries-for-mechanical-engineer-409cf994efdd

'''
'''
a=4
b
print(a/b)
print(a%b)

'''
'''
# a= 765433
# b =19
# print (a//b) # ---> the output wiil be in integer and the output will be based on the floor value

'''
'''
print ( 2**4) 

 '''
'''
# ! comparison ----> ==, > , < , != , <= , >=
# a = 8
# b = 9
# print ( a> b ) # true
'''
'''
a=8
b=8
print (a is b)
 '''
'''
a= (1, 2 , 3 )
b= ( 1, 2 , 3 )
print (a is b )
'''
'''
# member ship operator
L1 = [ 7 , 8 , 9 , 0 , 6 , 5 ]
num = 55
print(num in L1)
print (num not in L1)
'''
'''
if ( condition ){
    statement;
    statement;
    statement;
    statement;
    }
'''
'''
a = 6
if a>3:
    print ("yes")
else:
     print("no")
  '''
'''
a = 0
a = none
a = false
a = ""
if a :
    print("yes")
else :
    print("no")
'''
'''
n = int ( input("enter the number: "))
if n %2==0 :
    print ( n , " is even " )
else :
    print (n , " is odd ")

'''
'''

n = int (input (" nationality :" ))
print ( " n " )
'''

name = input (" enter the name: ")
age = int ( input ( " entyer the age: " ))
nationality = input ( " enter the nation: ")

enter the name: aravind
 entyer the age: 20
 enter the nation: indian

























    
