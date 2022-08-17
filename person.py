class Person:
    def __init__(self):
        self.name=None

    def setName(self,name):
        self.name=name
    


class BusinessMan(Person):
    
    def __init__(self,name,income,numberOfPeople):
        super().setName(name)
        self.income=income
        self.numberOfPeople=numberOfPeople

class Employee(Person):
    def __init__(self,name,income):
        super().setName(name)
        self.income=income




B=BusinessMan("Mr.Jordan",850000,50)
#B.setName("Mr.Jordan")
E=Employee("Manan Mehra",100000)
#E.setName("Manan Mehra")

if B.income>E.income:
    print(B.income,B.name)

else:
    print(E.income,E.name)
