def linear(array):
    print('ENTER ARRAY ELEMENT ONE BY ONE\t ')
    for i in range (n):
        array[i] = int (input())

    print ('ARRAY ELEMENTS ARE :\n\t= ',array)
    elem = [int (input('ENTER ELEMENT TO SEARCH\n\t'))]
    found = False
    while i<=n:
        for i in range (n):
            if array[i]==elem:
                found=True
                print ('ELEMENT IS FOUND AT LOCATION ',i)
        break
    if not found :
        print('ELEMENT IS NOT FOUND ')

import numpy
n = int (input ('ENTER ARRAY SIZE \n'))
array = numpy.ndarray(shape = (n) , dtype = int)
linear(array)
            
		
# This code is RUN on Numpy library function 
# So its prerequirment that the Numpy library should be installed
