s=input('enter the number1: ')
c=0
for i in s:
    if i.isdigit():
        i=int(i)
        c=c+i
        if i==0:
            print(c)
            break
            
            