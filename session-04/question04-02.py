import random

while True:
    a=random.choice(['sang','kaghaz','gheichi'])
    print(a)
    b=input('enter sang or kaghaz or gheichi:')
    if b==('exit'):
        break
    if a==b:
        print('success')
        
    elif a!=b:
        print('mojadad talash kon')

    

