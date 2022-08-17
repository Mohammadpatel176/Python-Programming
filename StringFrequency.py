l1="MyNameIsMohammad"

l2={}


for i in l1:

    if i in l2:

        l2[i]+=1

    else:

        l2[i]=1
        

print("Count of all the element in the given string is:\n",l2)


