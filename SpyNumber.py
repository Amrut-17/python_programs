import os
a = int (input('ENTER NUMBER \n ... '))
num = a
sum = 0
prod = 1
while a != 0:
    x = a%10
    sum = sum + x
    prod = prod * x
    a = a//10
if sum == prod:
    os.system('color 0c')
    print ('YES, ITS AN SPY NUMBER')
    #os.system('color 0a')
else :
    print('ITS NOT An SPY NUMBER')
    os.system('color 0a')