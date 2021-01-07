n = int(input("Enter Number of elements : "))
reverse = 0
for i in range(n):
    number = int(input("Enter Number"))
    while(number > 0):
        digit = number % 10
        reverse = (reverse * 10) + digit
        number = number // 10
    print(reverse)
    reverse = 0
    
