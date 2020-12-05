def fact_recursively(n):
	if n == 0 :
		return 1
	else :
		return n*fact_recursively(n-1)
		

n = int (input ('ENTER NUMBER. \n\t TO FIND ITS FACTORIAL _ '))
result = fact_recursively(n)
print ('FACTORIAL OF GIVEN NUMBER IS = ' , result)