L=input("یک رشته وارد کنید:")
a=len(L)
print(a)
b=a//2
if a%2==0:
    print(L[0:b])
else:
    print(L[b: ])
