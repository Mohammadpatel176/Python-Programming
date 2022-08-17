l1=[(1,2),(92,3),(4,7),(8,11),(3,6)]
print("The original list is: ",l1)
res1=list(map(max,zip(*l1)))
res2=list(map(min,zip(*l1)))

print("The miximum number in given list is: ",res1)
print("The minimum number in the list is: ",res2)

m0=min(l1)[0],max(l1)[0]
m1=max(l1)[1],max(l1)[1]

print("The minimum and miximum number in first position ",tuple(m1))
print("The minimum and miximum number in second postion: ",tuple(m0))
