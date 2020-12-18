def selection_sort(n):
    for i in range (n):
        min = i
        for j in range(i+1 , n):
            if (a[j] < a[min]):
                min = j
        temp = a[i]
        a[i] = a[min]
        a[min] = temp
    
    print('\nAFTER sorting')
    for i in range(n):
        print (a[i], end = " ")
        
import numpy 
n = int (input("ENTER SIZE OF ARRAY "))
a = numpy.ndarray(shape = (n) , dtype = int) 
print ('ENTER ARRAY ELEMENTS ONE BY ONE ')
for i in range (n):
    a[i] = int (input())
    
print ('BEFORE sorting')
for i in range(n):
    print (a[i], end = ' ')
selection_sort(n)