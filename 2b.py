#from unicodedata import digit

def st(string):
    
    digit,uper,lower,space,special,latter=0,0,0,0,0,0

    for i in string:
        if i.islower():
            lower+=1
        elif (i.isupper()):
            uper+=1
        elif i.isdigit():
            degite+=1  
        elif i.isspace():
            space+=1
        elif i.islatter():
            latter+=1
        else:
            special+=1

string=input("Enter string: ")
print("Digits:",digit)
print("Upper case:",uper)
print("Lower case:",lower)
print("space:",space)
print("Special characters:",special)
print("latters:",latters)
