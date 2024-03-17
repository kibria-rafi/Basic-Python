lst =input().split()
if len(lst)> 2:
  del lst[0]
  del lst[len(lst)-1]
  print(lst)
else:
  print('Not Possible')