n = int (input ('ENTER NUMBER TO CHECK WETHER ITS PALLINDROME NUMBER OR NOT\n'))
num = n
reverse = 0
while n > 0 :
    digit = n%10
    reverse = (reverse*10) + digit
    n = n // 10
if (num == reverse):
    print ('NUMBER IS PALLINDROME ')
else :
    print(' ITS NOT PALLINDROME NUMBER ') 