import numpy
n = int (input('ENTER NUMBER OF ELEMNETS \n'))
a = numpy.ndarray(shape = (n) , dtype = int)
print ('ENTER ARRAY ELEMNETS ONE BY ONE \n')
for i in range (n):
    a[i] = int (input())
   
print ('ARRAY ELEMENTS BEFORE SORTING : ' )   
for i in range (n):
    print (a[i],end = ' ')
    
for i in range (n):
    for j in range (n-1):
        if ( a[j]>a[j+1] ) :
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
            
print ('\nsorted list :')
for i in range (n):
    print (a[i], end = ' ')