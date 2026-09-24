a=input('enter: ')
count=0
for i in a:
    if i.isalpha():
        count+=1
print(count)
  
count1=0
for i in a:
    if i.isupper():
        count1+=1
print(count1)

count2=0
for i in a:
    if i.islower():
        count2+=1
print(count2)

count3=0
for i in a:
    if i.isdigit():
        count3+=1
print(count3)

count4=0
for i in a:
    if i.isspace():
        count4+=1
print(count4)

count5=0
for i in a:
    if not i.isalnum():
        count5+=1
print(count5)