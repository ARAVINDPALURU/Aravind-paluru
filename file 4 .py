#------> while loop
# -----> break using while loop

# eg : 1
# 1 ) iterate from 20 to 30 and break the loop in 27

'''
i = 20
while i<31:
    if i ==27:
        break
    print(i)
    i+=1

20
21
22
23
24
25
26

'''

#2 )

#i = 20
#while i<31:
#    print(i)
#    i+=1
#   if i ==27:
#        break


# 3. )

'''
i = 20
while i<31:
    print(i)
    if i==27:
        break
    i+=1
21
22
23
24
25
26
27

'''

# 4 .)
'''

i=20
while i<31:
    if i==27:
        print(i)
        break
    i+=1

27
'''

#-----> continue
#---> eg : 1
'''

i=20
while i<31:
    if i==27:
        continue
    print(i)
    i=i+1

    '''

'''
i=20
while i<31:
    if i==27:
        i=i+1
        continue
    print(i)

'''

# ! eg : 5


# while to iterate from 12 to 22
# find the sum of all numbers
#i = 12
#while i<22:
#    if i == 22:
#        break
#   print(i)
#    i+=1

'''

i = 12
sum = 0
while i<23:
    sum=sum+i
    i+=1
    print(sum)


12
25
39
54
70
87
105
124
144
165
187

'''
# find the average of value from 20 to 25

'''
i=20
sum=0
count=0
while i<=25:
    sum=sum+i
    count+=1
    i+=1
print(sum/count)


22.5

'''
#i=20
#sum=0
#count=0
#while i<=30:
#    sum=sum+i
#    count+=1
#    i+=1
#print(sum/count)



#25.0


#------> Nested for loop



#for i in range (1,3):
#   for j in range (1,4):
#        print(i,j)


#1 1
#1 2
#1 3
#2 1
#2 2
#2 3

'''


for i in range (1,3+1):
   for j in range (1,4+1):
        print(i,j)


1 1
1 2
1 3
1 4
2 1
2 2
2 3
2 4
3 1
3 2
3 3
3 4

'''
'''
for row in range (1,3+1):
    for col in range (1,4+1):
          print(row,col)

'''
# eg
# * * * *
# * * * *
# * * * *
# * * * * 
'''
for row in range (4):
    for col in range (4):
          print("*",end=" ")
    print()


* * * * 
* * * * 
* * * * 
* * * * 

'''
'''
rows = int(input("enter the rows"))
cols = int(input("enter the cols"))
for row in range (rows):
    for col in range (cols):
          print("*",end=" ")
    print()

* * * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * 

'''
'''

for i in range(0,6):
    for j in range(i,6):
        print("*",end=" ")
    print()



* * * * * * 
* * * * * 
* * * * 
* * * 
* * 
* 

'''
'''

for i in range(rows, 0, -1):
    for j in range(0, i):
        print("*", end=' ')
    print("\n")


#*****
#*   *
#*   *
#*   *
#*****

rows = 5
cols = 5

for i in range(rows):
    for j in range(cols):
        if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
            print("*", end='')
        else:
            print(" ", end='')
    print()


for row in range(5):
    for col in range(5):
        if col==0 or col==5-1 or row ==0 or row ==5-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


#      *
#    * * *
#   * * * *
#  * * * * *

rows = 9

for i in range(rows):
    print(" " * (rows - i - 1), end='')  
    print("*" * (2 * i + 1), end='')    
    print(" " * (rows - i - 1))
        
'''

'''


for row in range(6):
    for col in range(6):
            if(col==0 or (row==0 and col==0) or (row==1 and col==1))or (row==2 and col==2) or (row==3 and col==3) or (row==4 and col==4) or (row==5):
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print()

*           
* *         
*   *       
*     *     
*       *   
* * * * * *

'''





# ----> List
# primary

# Number ----> int, float complex
# String
# Boolean
# None

# collection
# List
# tuple
# set
# dictionary

# ? ---> List

# 1.) if the collection of elements are surrounded by Square brackets, it is considered to be list.
# ! ---> Eg:
# l1 = [4, 7, 9, 9.89, "hello", 7+9j, [8, 9, 0]]


# Characteristics of list
# 1.) List have to be surrounded []
# 2.) It is mutable (the elements in the list are changable)
# 3.) Every elements inside list is indexed
# 4.) The elements inside list will be ordered format
# 5.) It can hold duplicate values
# 6.) Its heterogenous

#--> Indexing
# In the collection datatypes like list, tuple, string, the elements will be alloted
# with predefined unique value called index value

# We have 2 types of indexing
# Positive indexing --> starts with @ from left hand side
# Negative indexing --> starts with -1 from right hand side

'''
# ?---> positive indexing
lst1 = [1,4,1,7,89,7,7.5,"p","i"]
print(lst1[0])
print(lst1[4])
print(lst1[20])

'''

# ------> negative indexing
'''
lst1 = [1 , 4 , 1 , 7 , 89.7 , 7.5 , "p" , "i" ]
print(lst1[-1])
print(lst1[-5])


 i
89   
 '''

# ------> slicing
#lst1 = [1, 4, 1, 7, 89, 7, 7.5, "p", "i" ]
#print(lst1[7:9])
      
#['p', 'i']
'''

lst1 = [1 , 4 , 1 , 7 , 89.7 , 7.5 , "p" , "i" ]
print(lst1[3:6])
print(lst1[0:7])


[7, 89.7, 7.5]
[1, 4, 1, 7, 89.7, 7.5, 'p']

'''
'''
lst1 = [1, 4, 1, 7, 89, 7, 7.5, "p", "i" ]
print(lst1[-4:-1])
print(lst1[-1:-4])
print(lst1[-7:-1])
print(lst1[-7:-1:2])


[7, 7.5, 'p']
[]
[1, 7, 89, 7, 7.5, 'p']
[1, 89, 7.5]

'''

#! to insert or add elemnt inside list

# append()----> used to add at last position of list
l1 = [9, 8, 0, 6]
l1.append("car")
print(l1)






    
