a=input('enter: ')
if len(a)<8:
    print('Password must contain at least 8 characters')
c=0
for i in a:
    if i.isupper():
        c=1
        break
if c==0:
    print('password must contain at least capital characters')

b=0
for i in a:
    if i.islower():
        b=1
        break
if b==0:
    print('password must contain at least small characters')

d=0
for i in a:
    if i.isdigit():
        d=1
        break
if d==0:
    print('password must contain at least digit characters')

e=0
for i in a:
    if not i.isalnum():
        e=1
        break
if e==0:
    print('Password must contain a spec')

else:
    print('Password is invalid')        