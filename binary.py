def Binary_search (array , element):
        first = 0 
        last = n-1
        found = False
        while first<=last and not found:
                mid = (first+last)//2
                if element > array[mid] :
                    first = mid + 1 
                elif array[mid] == element :
                    found = True
                else :
                    last = mid - 1
        if found == True:
            print ('ELEMENT IS FOUND At LOCATION : ' ,mid)
        else:
            print ('ELEMENT IS NOT FOUND ')

import numpy 
n = int (input ('ENTER ARRAY SIZE \n'))
array = numpy.ndarray(shape = (n) , dtype = int)
print ('ENTER ARRAY ELEMENTS IN INCREASING ORDER |_ONLY_| ')
for i in range (n):
	array[i] = int (input ())
    
print ('ARRAY ELEMENTS ARE :\n\t=',array)
element = int (input ('ENTER ELEMENT TO SEARCH IN ARRAY \n'))
Binary_search(array,element)