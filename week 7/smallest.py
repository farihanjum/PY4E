smallest = None
for i in [9,41,12,3,74,15] :
  if smallest is None :
    smallest = i
  elif smallest > i :
    smallest = i
    print(smallest)

print(smallest)
