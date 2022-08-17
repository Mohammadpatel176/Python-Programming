D1={'First Name': 'Mohammad', 'Middle Name': 'Mehmudbhai', 'Last Name': 'Patel'}
print("initial Dectonary:",D1)

#lambda Function
D1={v:k for k,v in D1.items()}
print("After inverting:",D1)

#using dict,keys() and dict.values()
D2={'Animal':'Dog','colour':'red','fruite':'Mango'}
print("Befor inverting:",D2)
D2=dict(zip(D2.values(),D2.keys()))
print("After inverting:",D2)

#using inverse map method
D3={201: 'ball', 101: 'akshat'}
print("Befor inverting:",D3)
D3=dict(map(reversed,D3.items()))
print("After inverting:",D3)