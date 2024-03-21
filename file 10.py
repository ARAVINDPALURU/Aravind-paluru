# tasks

# write the code for the below tasjs using function
# 1.)d1 = {"shirt": 1000, "pant": 1500, "Shoes": 900, "handkey": 30}
# a.) Find the min ans max priced product
# b.) Find the product starts with "s" and "S"

# 2.) Find the n = 67, is strong number or not

# 3.) l1 = [1,2,3,4,5,6]
# n=2 --> [5,6, 1,2,3,4]
# n=3 --> [4,5,6, 1,2,3]
#------------------------------------------------
# ! Method over-riding
# * ploymorphism in classes

'''
class bank :
      def ratio(self):
          print("All banks has repo rate")

class SBI(bank):
    def ratio(self):
        print("SBI rate is 9%")

class IOB(bank):
    def ratio(self):
        print("IOB rate is 7.5%")


i = IOB()
i.ratio()

s = SBI()
s.ratio()


IOB rate is 7.5%
SBI rate is 9%

'''

# ? eg : 2


'''
class USA:
    def language(self):
        print("english")

    def capital(self):
        print("washington DC")

class India:
    def language(self):
        print("hindi")

    def capital(self):
        print("New delhi")

I = India()
I.language()
I.capital()

hindi
New delhi

'''

# eg : 3

# polymorphism using objects

#c1, c2 ---> c1 = print(c1), print(c2)
# f1, f2


'''
class c1:
    def f1(self):
        print("class 1")


class c2(c1):
    def f1(self):
        super().f1()
        print("class2")


obj1 = c2()
obj1.f1()

class 1
class2
'''
# Eg:4

'''
class c1:
    def f1(self):
        print("class 1")

class c2(c1):
    def f1(self):
        print("class 2")

obj1 = c2()
obj2 = c1()

def display(a):
    a.f1()
display(obj1)
display(obj2)
'''

# * changing the functionality of builitin functions
'''
class shooping :
    def __init__(self, l1):
        self.items = l1

    def __len__(self):
        length = len(self.items)
        return length
s = shooping([1,2,3,4,5])
print(len(s))
  
5

'''

# ! ---> Method overloading

# ! Eg:1

'''
class suming:
    def add(self,a,b):
        print(a+b)

    def add(self, a, b, c):
        print(a+b+c)

s = suming()
# s.add(4,3) # ! ---> error
s.add(455,575,441)

'''
# * changing the functionally of builtin functions

'''
class shopping:
   def __init__(self,l1):
       self.items = l1
       
   def __len__(self):
       length = len(self.items)
       return length
s = shopping([1,2,3,4,5])

print(len(s))

'''

# ! --------> Abstraction
# The procss of hiding the implimentation details is abstraction

# ? Eg:1
'''
class shapes(ABC):
    def sides(self):
        print('All shapes have sides except circle')

class triangle:
    def triangle_sides(self):
        print("3 sides")

class square:
    def square(self):
        print("4 sides")

'''

'''
from abc import ABC,abstractmethod
class shapes(ABC):
    @abstractmethod
    def sides(self):
        print("All shapes have sides except circle")

class triangle(shapes):
    def triangle_sides(self):
        print("3 sides")

class square(shapes):
    def square(self):
        print("4 sides")

tr = triangle()
tr.triangle_sides()
'''
# To write the capital letters
'''
def decor(func):
    def inner():
        str1 = func()
        return str1.upper()
    return inner()

@decor
def greet():
    return 'good morning'

'''

# ! Rules to define abstract class 1

# 1 .) Abstract class cannot be instatained
# 2.) From abc impport ABC , abstractmethod
# 3.)subclass the normal class with ABC
# 4.) covert the normal method inside the abstract class to abstract method
# 5.) All the child classes have to be subclassed with abstract class
# 6.) the abstract method should be present in the

# child classes


# ! Eg:2
# super()

'''
from abc import ABC, Abstractmethod 
class c1(ABC):
    @Abstractmethod
    def m1(self):
        print("this is abstract class")

class c2(c1):
    def m2(self):
        super().m1()
        print("Iam child 1")

    def m1(self):
        pass
    
class2 = c2()
class2.m2()

'''

'''

from abc import ABC, abstractmethod
class password(ABC):
    @abstractmethod
    def pwd(self):
        pswd = "aravind7369"
        return pswd

class login(password):
    def validate(self,name,passwrd):
        if super().pwd() == passwrd:
            print("welcome", name, "!!")
            print(" Login succesfull")
        else:
            print("Please check the password")

    def pwd(self):
        pass


login = login()
name = input("Enter the name: ")
pwd = input("Enter the password: ")
login.validate(name, pwd)
'''


# ! Encapsulation


'''
class car:
    name = "BMW"

c1 = car()
print(c1.name)
c1.name = "Audi"
print(c1.name)


'''

# * ---> eg : 2

# ? Accessing private date outside the class


'''
class c1:
    __phone = '9632587410'

    def display(self):
        print(self.__phone)
c = c1()
c.display()


'''

# * ---->eg :3
# ? declare private method

'''
class class1:
    def __m1(self):
        print("Iam private method")

        def __init__(self):
            self.__m1()
c = class1()
c.m1()

'''

# ? nested class

'''
class class1:
    class class2:
        name = "aravind"

        def display(self):
            print(self.name)
    obj1 = class2()

obj = class1()
obj.obj1.display()

aravind
'''
























