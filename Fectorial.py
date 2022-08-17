n=int(input("Enter Number which you want factorial:"))
fectorial=1

if n<0:
    print("Enter right input")

elif n==0:
    print("Fectorial is 1")

else:
    for i in range(1,n+1):
        fectorial*=i
    print("Fectorial of given number is:",fectorial)
