# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 10:47:21 2023

@author: Web 123
"""

# x=1
# help(x)
# dir(x)

# y=[1,2,3]
# help(y)
# dir(y)

# z={'a':1}
# help(z)
# dir(z)

# class patient(object):
#     status = 'patient'
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         self.conditions=[]
#     def get_details(self):
#         print(f'Patient Record : {self.name} and {self.age} years Old'\
#             f' Current Information : {self.conditions}')

#     def add_info(self,information):
        # self.conditions.append(information)



# yasir=patient('Anees', 25)
# asim=patient('Noor', 25)


# class Infant(patient):
#     # patien under 2 years
    
#     def __init__(self,name,age):
#         self.vaccinations=[]
#         super().__init__(name,age)
#     def add_vac(self,vaccine):
#         self.vaccinations.append(vaccine)
#     def get_details(self):
#         print(f'patient Record : {self.name} and {self.age} years old '\
#               f'patient has had {self.vaccinations} vaccine'\
#               f'current Information : {self.conditions}.'\
#               f'\n {self.name} is an infant, has he had all his checks ?')
# archie=Infant('archie fitleworth',0)
# archie.add_vac('MMR')

# class Infant(patient):
#     ''' Patient under 2 years'''
    
#     def __init__(self,name,age):
#         self.vaccinations = []
#         super().__init__(name,age)
        # 
#     def add_vac(self,vaccine):
#         self.vaccinations.append(vaccine)
        # 
#     def get_details(self):
#           print(f'Patient record: {self.name}, {self.age} years.' \
#                 f' Patient has had {self.vaccinations} vaccines.' \
#                 f' Current information: {self.conditions}.' \
#                 f'\n{self.name} IS AN INFANT, HAS HE HAD ALL HIS CHECKS?')
        
# archie = Infant('Archie Fittleworth',0)        
# archie.add_vac('MMR') 



# Question 1

# Create a class to represent a bank account. It will need to have a balance,
# a method of withdrawing money, depositing money and displaying the balance to
# the screen. Create an instance of the bank account and check that the methods 
# work as expected.

# class Bank_Account(object):
#     def __init__(self,balance=0.00):
#         self.balance=balance
#     def Display_Balance(self):
#         print(f'Your Balance is {self.balance}')
#     def Make_Deposit(self):
#         amount=float(input('How Much Would yo like to deposit : >>'))
#         self.balance +=amount
#         print(f'Balance is Now {self.balance}')
#     def with_Draw(self):
#         amount = float(input(f'How Much Payment WithDraw{self.balance} :>>'))
#         if amount > self.balance:
#             print(f'you don\'t hae sufficient funds, your Balance is {self.balance} >> ')
#         else :
#             self.balance -= amount
#             print(f'Withdrwawal Successfully : Balance is Now {self.balance} >>')
        


'''
Question 2
 Create a circle class that will take the value of a radius and 
 return the area of the circle
'''

# import math

# class Circle(object):
#     def __init__(self,radius):
#         self.radius= radius
#     def clac_area(self):
#         area=math.pi*(self.radius)**2
#         return area

































































































