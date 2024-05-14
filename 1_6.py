def compoundinterest(amount,rate,time):
    Amount = amount * (pow((1 + rate / 100), time))
    return Amount - amount

print(compoundinterest(10000, 10.25, 5))