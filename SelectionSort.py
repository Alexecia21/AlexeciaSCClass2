# make an array for sorting the selection

array = [13, 4, 9, 5, 3, 16, 12]

def selectionSort(array):

    n = len(array)

    for i in range(n): #<-- whatever the length of the array is how many times you will run the loop

        minimum = i 

        for j in range(i+1, n):

            if (array[j] < array[minimum]):

                minimum = j 

        temp = array[i]
        array[i] = array[minimum]
        array[minimum] = temp 

    return array

print (selectionSort(array))
