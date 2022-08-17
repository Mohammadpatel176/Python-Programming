l1=[]
n=int(input("enter how many data you want to insert into list: "))

for i in range(n):
    i=input("enter data:")
    l1.append(i)
    
print(l1)
print("After removing duplicat data from list:")
l2=set(l1)
#l1=list(l2)
print(l2)
