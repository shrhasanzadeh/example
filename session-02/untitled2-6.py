i=int(input('enter number:'))
price1=i-(i*0.15)
price2=i-(i*0.1)
if i>=1000000:
    print(price1)
elif 500000<i<1000000:
    print(price2)
else:
    print(i)
    