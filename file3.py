'''
# ! eg : 3
# ? take values of length and breadth of a
# ? from user and check if it square or not .

'''
'''
length = int ( input ( " enter the value " ) )
breadth = int ( input ( " enter the value " ) )
if length == breadth :
    print("its a square")
else :
    print("its not square")
    
 enter the value 30
 enter the value 25
its not square

'''
'''
eg  : 4
 pythan program to check weather the given integer the multiple of 5 and ?

 '''
'''

n = int ( input ( " enter the number " ))
if n%5==0 and n%7==0 :
    print ( "yes ")
else :
    print (" no ")
    
 enter the number 35
yes 

'''
'''

eg : 5
write a program to accept the cost price of bike aand display the road tax to be paid according to the following criteria :

cost price ( in Rs )
 > 100000
 > 50000 and <= 100000
 <= 50000
 '''
'''
price = int ( input ( " enter the price : " ) )
amount = 0
if price>=100000:
    discount=100000*( 6/100)
    value=price - discount
    tax=value*(15/100)
    total=value+tax
else :
    tax = price*(5/100)
    total = price+tax
print ( " the onroad cost of bike is : " ,total )
    
  enter the price : 500000
 the onroad cost of bike is :  568100.0

 '''
'''
 # ------>if ,elif ,else

  eg : 1
   '''

'''
a=7
b=9
c=3

if a > b and a > c :
    print ( " a is greater " )
elif b > a and b > c :
    print ( " b is greater " )
elif c > a and c > b :
    print ( " c is greater " )

 b is greater


 '''
'''

# A school has following rules for grading system :
# a. Below  25 - F
# b. 25  to  45 - E
# c. 45   to 50  - D
# d. 50  to 60  - C
# e. 60  to  80  - B
# f. Above  80 -  A
# Ask user to enter marks and print the corresponding grade .
'''
'''
mark = int ( input ( "  Enter mark " ))
if mark >=80 and mark <= 100 :
    print ( "A " )
elif mark >= 60 and mark < 80 :
    print ( " B " )
elif mark >= 50 and mark < 60 :
    print ( " C " )
elif mark >= 45 and mark < 50 :
    print ( " D ")
elif mark >= 25 and mark < 45 :
    print ( " E " )
else :
    print ( " Fail " ) 


  Enter mark 22
 Fail

'''
'''

* rules
1.)statement inside the if condition have to be present at first
2.)elif cannot be used in short hand if else
3.)always it have to end with else
* rules
'''
'''

a=9
b=60
if a>b :
     print(" A ")
else:
    print (" B " )

 B 

'''

'''
# ! Code to check the given char is vowel or consonent
'''


#char = input("enter the char :" )
#if char == " a " or char ==' e ' or char == 'i ' or char== ' o ' or char =='u' :
#            print ( " is a vowel ")
#else :
#   print ("its consonent " ) 
      
#enter the char :g
#its consonent 



#char = input ( " enter the char ")
#str1 = " aeiouAEIOU "
#if char in str1 :
#    print (" vowel " )
#else :
#    print ( " consonent")


#a=8
#b=5
#c=9
#print("A is greater ") if a>b and a>c else print ("B is greater ") if b>a and b>c else print (" C is greater " )

# C is greater


# -----> looping
# looping can be implimented using
# for loop
# while loop

 # ---> for loop
 # for loop is used for iteration, if we know the no of times the loop have to run
 # it is used to itrrate the iterables eg ( string , list , tuple , etc ....)

 # todo -----> syntax for loop

# for syntax in c
#for (i=0;i<10;i++){
#     printf("hello");
#     }


#for syntax in python
'''
for i in range (0,10):
    
    print (i)
    print ("hello")

 0
hello
1
hello
2
hello
3
hello
4
hello
5
hello
6
hello
7
hello
8
hello
9
hello
'''

#for  val in range (1,10+1,):
 #   print('7' , 'x' , val , '=' , val*7) # method : 1

#7 x 1 = 7
#7 x 2 = 14
#7 x 3 = 21
#7 x 4 = 28
#7 x 5 = 35
#7 x 6 = 42
#7 x 7 = 49
#7 x 8 = 56
#7 x 9 = 63
#7 x 10 = 70


 # Eg:6---> method 2
'''
for val in range(1,10+1):
    ans="7 x {}= {}"
    print(ans.format(val,val*7))
    
7 x 1= 7
7 x 2= 14
7 x 3= 21
7 x 4= 28
7 x 5= 35
7 x 6= 42
7 x 7= 49
7 x 8= 56
7 x 9= 63
7 x 10= 70
'''

# Eg:6---> method 3
'''
for val in range(1,10+1):
    print(f"7 x {val}={val*7}")

7 x 1=7
7 x 2=14
7 x 3=21
7 x 4=28
7 x 5=35
7 x 6=42
7 x 7=49
7 x 8=56
7 x 9=63
7 x 10=70
'''
# Eg:7
#breack ---> used to terminate the loop
'''
for val in range (1,10):
    if val ==6:
        break
    print(val)

1
2
3
4
5
'''
'''
for value in range (20,41,1):
    print(value)
    


20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
'''

# ! ------> while loop
#while is used when we do not kbnoe the number of times the loop have to run
#to iterate the non iterable elements while loop is used

# to do syntax
# initialisation
# while condition
#     statement
#     incre or decre

#Eg:1

#to iterate number from 1 to 10

#i=0
#while i<11:
#    print(i)

n=int(input("enter number: "))
sum=0
for val in range(1, n+1):
    sq=val*val
    if val %2==0:
        sum=sum+val
    else:
        sum=sum-sq
print(sum)

# for loop practice
# write a program to display sum of odd numbers and even
# numbers that fall between
# 12 abd 37c(including both numbers)

# ---> Assesment
# 1.) cats and mouse:Hacker rank
# 2.) Print the factorla of 8 using for loop
# 3.) Write a program to display sum of odd numbers and even 
# numbers that fall between
# 12 and 37(including both numbers)
# 4.) Write code to print the sum of number using while loop
# n1 = 123 --> 1+2+3 = 6
# 5.) Prine th reverse of given number --> n1= 234 o/p --> 432




    
























































































































   







































































