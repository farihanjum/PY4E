
total = 0
count = 0
a= None
while True :
    a= input('enter a number')
    if(a == "Done") :
        break
    try :
        a= int(a)
        total+=a
        count+=1
    except :
        print('bad data')
print(total,count,total/count)
