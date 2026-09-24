a=input('enter: ')
l=a.split()
for i in ["hack","fraud" ,"scam" ,"password","atack"]:
    if i in l:
           print(a.count("hack"),a.count("fraud"),a.count("scam"),a.count("password"),a.count("atack"))