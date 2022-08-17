n = int (input ("Enter the number for which the factorial needs to be calculated:"))

def rec_fact (n):
    if n == 1:
        return n

    elif n < 1:
        return ("Wrong input")

    else:
        return n*rec_fact (n-1)

print (rec_fact (n))
