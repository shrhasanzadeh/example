a=input('color1:')
b=input('color2:')
c=input('color3:')
if a==b or a==c or b==c:
    print('2     colors same')
elif a==b and a==c and b==c:
    print('3 colors same')
else:
    print('color is difrent')
