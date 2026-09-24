a=input('enter: ')
b=0
l=a.split()
for i in l:
    count=l.count(i)
    if count>b:
        b=count
print(b)