def InsertionSort(n):
    for i in range (1,n):
        key = a[i]
        j = i-1
        while (j>=0 and a[j]>key):
            a[j+1] = a[j]
            j = j-1
        a[j+1] = key
    print ('\n SORTED LIST : \t')
    for i in range (n):
        print (a[i],end = ' ')
 
import numpy 
n = int (input("ENTER NUMBER OF ELEMENTS  "))
a = numpy.ndarray(shape = (n) , dtype = int)
print("ENTER ARRAY ELEMNETS ONE BY ONE ")
for i in range(n):
    a[i] = int (input())
print("unsorted array is :\t")
for i in range(n):
    print (a[i],end = ' ')
InsertionSort(n)
