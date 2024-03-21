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

class shooping :
    def __init__(self, l1):
        self.items = l1

    def __len__(self):
        length = len(self.items)
        return length
s = shooping([1,2,3,4,5])
print(len(s))
  




























