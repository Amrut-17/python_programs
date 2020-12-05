def enter(m,n):
    print ('ENTER ELEMENTS OF 1\'st MATRIX ')
    for i in range (m):
        for j in range (n):
            a[i][j] = int(input())
    print('ELEMENTS OF 2\'nd MATRIX ')
    for i in range (m):
        for j in range (n):
            b[i][j] = int (input())
        
def addition (m,n):
    print ('ADDITION OF TWO MATRIX IS :')
    c = [[0 for i in range (m)] for j in range (n)]
    for i in range (m):
        for j in range (n):
            c[i][j] = a[i][j] + b[i][j]
    for i in range (m):
        for j in range (n):
            print (c[i][j] , end = ' ')
        print ()
        
def substraction(m,n):
    print ('SUBSTRACTION OF TWO MATRIX IS :')
    c = [[0 for i in range (m)]for j in range (n) ]
    for i in range (m):
        for j in range (n):
            c[i][j] = a[i][j] - b[i][j]
    for i in range (m):
        for j in range(n):
            print (c[i][j] , end = ' ')
        print ()
        
def multi(m,n):
    print ('MULTIPLICATION OF TWO MATRIX IS :')
    c = [[0 for i in range(m)] for j in range(n)]
    for i in range (m):
        for j in range (n):
            for k in range (n):
                c[i][j] = c[i][j] + a[i][k] * b[k][j]
    for i in range(m):
        for j in range (n):
            print (c[i][j] , end = ' ')
        print ()
        
def symmetric ():
    print ('ENTER ELEMENTS OF 1\'st MATRIX ')
    for i in range (m):
        for j in range (n):
            a[i][j] = int(input())
    for i in range (m):
        for j in range(n):
            if (a[i][j] == a[j][i]) :
                print ('MATRIX IS SYMMETRIC \n')
                break
    else :
        print ('MATRIX IS NOT SYMMETRIC \n')

import numpy
m = int(input ('ENTER NUMBER OF ROWS '))
n = int(input ('ENTER NUMBER OF COLUMNS '))
a = numpy.ndarray (shape = (m,n) , dtype = int )
b = numpy.ndarray (shape = (m,n) , dtype = int )                 

            
print ('SELECT CHOICE ')
choice = int (input ('\n\t1]ADDITION OF TWO MATRIX \n\t2]SUBSTRACTION OF TWO MATRIX \n\t3]MULTIPLICATION OF MATRIX \n\t4]CHECK MATRIX IS SYMMETRIC OR NOT \n  '))
if choice == 1 :
    enter(m,n)
    addition(m,n)
elif choice == 2 :
    enter(m,n)
    substraction(m,n)
else :
    if choice == 3 :
        enter(m,n)
        multi(m,n)
    elif choice == 4 :
        symmetric()
    else :
        print ('ENTER CORRECT CHOICE ')
    