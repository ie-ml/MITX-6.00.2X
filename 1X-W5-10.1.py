# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 10:04:18 2020

@author: ieste

6.00.1X_Week 05_10 AnExtendedExample
Build a little system wich organize information about people
"""
import datetime

class Person(object):
    def __init__(self,name):
        self.name = name
        self.birthday = None
        self.lastname = name.split(' ')[-1]
        
    def __lt__(self, other):
        '''other es una instancia de esta clase'''
        if self.lastname == other.lastname:
            return self.name < other.name
        return self.lastname < other.lastname
    
    def setBirthday(self,month,day,year):
        self.birthday = datetime.date(year,month,day)
    
    def getAge(self):
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).date
    
    def getLastName(self):
        return self.lastname
    
    def __str__(self):
        return self.name
    
    # Construyo el data base
    
p1 = Person("Marck Zuckerberg")
p1.setBirthday(5,14,84)
p2 = Person("Drew Houston")
p2.setBirthday(3,4,83)
p3 = Person("Bill Gates")
p3.setBirthday(10,28,55)
p4 = Person("Andrew Gates")
p5 = Person("Steve Wozniak")

personList = [p1,p2,p3,p4,p5]

for e in personList:
    print(e)

personList.sort()

print("\n"+"Lista de nombres por orden alfabético: \n")

for e in personList:
    print(e)













        