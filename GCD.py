def GCD(x,y):
   if y==0:
       return x
   else:
       return GCD(y,x%y)
   
   
   
x=int(input("Enter first number:"))
y=int(input("Enter second number:"))

result=GCD(x,y)
print("Gratest division number of given two number is:",result)
