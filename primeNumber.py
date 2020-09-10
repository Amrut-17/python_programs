import time
from math import ceil
n = int(input('enter number\n'))

half = n//2
if n == 1:
    print("not prime number")
elif n == 2 or n == 3:
    print('PRIME NUMBER !!!!')
elif n>2 :
    start_time = time.time()
    for i in range (2, half+1):
        if n%i == 0:
            print('not prime number')
            break
        
    else :
        print('PRIME NUMBER !!!!')
            #break
    end_time = time.time()
    print(end_time - start_time)
else :
    print('not prime number')
    
    
# This code is about to check given number is prime or not
# Time required to execute this code is for number 15485863 is 8.853506 second's
