i=str(input('شماره کازت:'))
a=str(input('پیش شماره کارت بانکی:'))
s=i[0:4]
print(s)
if a==s:
    print('نام بانکی')
    
else:
    print('معتبر نیست')
