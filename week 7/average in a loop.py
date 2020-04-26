count = 0
total = 0
print('Before',count,total)
for i in [9,41,12,3,74,15] :
    count+=1
    total+=i
    print(count,total, i)
print('After',count,total,total/count)
