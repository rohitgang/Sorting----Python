class Sort:

    def __init__(self):
        self.__author__= ['Rohit Gangurde']


    """
    ----------------------------------------BUBBLE SORT--------------------------------------------------
    Steps through the array and looks at i element and i-1 element, checks if they are in ascending order.
    If they are not, it swaps them, otherwise it goes on to next element. As it steps through the unsorted
    part of the list, it has the worst time complexity of O(n**2). It has the best time complexity of Ω(n).
    It has the average time complexity of Θ(n**2). It has space complexity of O(1).
    ------------------------------------------------------------------------------------------------------
    """
    def bubble(self, arr):

        def swap(i, j):
            arr[i], arr[j] = arr[j], arr[i]

        n = len(arr)
        swapped = True

        x = -1
        while swapped:
            swapped = False
            x = x + 1
            for i in range(1, n - x):
                if arr[i - 1] > arr[i]:
                    swap(i - 1, i)
                    swapped = True

        return arr

    """
    -----------------------------------------SELECTION SORT----------------------------------------------------
    Divides the array into a sorted and an unsorted sub-array. The element in the sorted array is the minimum 
    from the unsorted subarray. So we keep on placing the minimum element from the unsorted array into the 
    sorted array and removing it from the unsorted array till we have no elements in the unsorted array. It has 
    the worst time complexity of O(n**2). It has the best time complexity of Ω(n**2). It has the average time 
    complexity of Θ(n**2). It has space complexity of O(1).
    ------------------------------------------------------------------------------------------------------------
    """
    def selection(self, arr):

        for i in range(len(arr)):
            minimum= i
            for j in range(i+1,len(arr)):
                if arr[j] < arr[minimum]:
                    minimum=j
            #place it at the end of the sorted array
            arr[minimum], arr[i]= arr[i], arr[minimum]

        return arr

    """
    ---------------------------------------------INSERTION SORT-------------------------------------------------
    Iterates through the array looking at one element at a time. It checks if the element is in the right place. 
    If it is not, it finds the best place for the element and inserts it there; otherwise it moves on to the 
    next element. It ahs the worst time complexity of O(n**2). It has the best time complexity of Ω(n). It has 
    the average time complexity of Θ(n**2). It has space complexity of O(1).
    ------------------------------------------------------------------------------------------------------------
    """
    def insertion(self, arr):

        for i in range(len(arr)):
            cursor= arr[i]
            pos= i

            while pos > 0 and arr[pos-1] > cursor :
                #swap number down the list
                arr[pos]= arr[pos-1]
                pos-=1
            arr[pos]= cursor

        return arr


    """
    --------------------------------------------MERGE SORT-------------------------------------------------------
    It recursively calls mergeSort() on the array till we have sub arrays of length 1. Then it works on merging 
    the sublists in ascending order till we have no sub arrays. It has the worst time complexity of O(nLog(n)). 
    It has the best time complexity of Ω(nLog(n)). It has the average time complexity of Θ(nLog(n)). It has 
    space complexity of O(n). 
    -------------------------------------------------------------------------------------------------------------
    """
    def mergeSort(self, arr):
        #base case
        if len(arr) <= 1:
            return arr

        mid= len(arr)//2

        left,right= mergeSort(self,arr[:mid]), mergeSort(self, arr[mid:])

        return merge(self, left, right, arr.copy())

    def merge(self, left, right, merged):
        left_cursor, right_cursor= 0,0
        while left_cursor < len(left) and right_cursor < len(right):
            if left[left_cursor] <= right[right_cursor]:
                merged[left_cursor+right_cursor]= left[left_cursor]
                left_cursor+=1
            else:
                merged[left_cursor+right_cursor]= right[right_cursor]
                right_cursor+=1
        for left_cursor in range(left_cursor, len(left)):
            merged[left_cursor+right_cursor]= left[left_cursor]

        for right_cursor in range(right_cursor, len(right)):
            merged[right_cursor+left_cursor]= right[right_cursor]

        return merged

