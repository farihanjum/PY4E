
largest = 0
smallest = None
a= None
while True :
    a= input('enter a number')
    if(a == "done") :
        break
    try :
        a= int(a)
        if a >largest :
            largest = a

        if smallest is None :
            smallest = a

        if a < smallest :
            smallest = a
    except :
        print('Invalid input')
print('Maximum is',largest)
print('Minimum is',smallest)
