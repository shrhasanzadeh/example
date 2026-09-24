a=input('enter: ')
b=0
output=" "
for i in range(len(a)-1):
    if a[i]==a[i+1]:
        b+=1
    else:
      output=output+a[i]+str(b) 
      
print(output+a[-1]+str(b))