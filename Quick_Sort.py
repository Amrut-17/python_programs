def sort_for_pivot(list , first , last):
    pivot = list[first]
    left = first + 1
    right = last
    
    while True :
        while left <= right and list[left] <= pivot :
            left+= 1
        while left <= right and list[right] >= pivot :
            right-= 1
        if right < left :
            break 
        else :
            list[left] , list[right] = list[right] , list[left]
    list[first] , list[right] = list[right] , list[first]
    return right 
    
    
def quick_sort(list , first , last):
    if first < last :
        p = sort_for_pivot(list , first , last)
        quick_sort(list , first , p-1)
        quick_sort(list , p+1 , last)
        
n = int (input ('enter size of list\n'))
print('enter elements ')
list = [int(input ())for i in range (n)]
quick_sort(list , 0 , n-1)
print(list)  