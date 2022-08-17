def sli(starting,ending,string):
    return int(string[starting:ending])



#class decleration
class Clock:
    def __init__(self,hour,minute,second):   #constructor in python with three arguments hour minuite and second
        self.hour=hour
        self.minute=minute
        self.second=second
        
            

    def setClock(self):  #setClock method
        if(self.second>59):
            temp=self.second
            self.second%=60
            self.minute+=temp//60

        if(self.minute>59):
            temp=self.minute
            self.minute%=60
            self.hour=self.hour+temp//60

        if(self.hour>23):
            self.hour=0
     

    def setTick(self):  #setTick Method 
        self.second+=1

        if(self.second>59):
            self.minute+=1
            self.second=0

            if(self.minute>59):
                self.hour+=1
                self.minute=0

                if(self.hour>23):
                    self.hour=0

    def __add__(self,other):
        temp=Clock(0,0,0)
        temp.hour=self.hour+other.hour
        temp.minute=self.minute+other.minute
        temp.second=self.second+other.second

        return temp


    def displayTime(self):  #Display method
        print(self.hour,":",self.minute,":",self.second)

 


#main part

st=input("Enter time in hh:mm:ss formet: ")
hour=sli(0,2,st)
minute=sli(3,5,st)
second=sli(6,8,st)

c1=Clock(hour,minute,second)  #objcet c1 is created
c1.displayTime()
print("...............................")
c1.setClock()
c1.displayTime()
print("...............................")
c1.setTick()
c1.displayTime()

st=input("Enter time in hh:mm:ss formet: ")
hour=sli(0,2,st)
minute=sli(3,5,st)
second=sli(6,8,st)

c2=Clock(hour,minute,second)  #objcet c1 is created
c2.displayTime()

print("After Addition of two objects:")
c3=c1+c2
c3.setClock()
c3.displayTime()











