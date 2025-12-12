# for testing
array = [1, 5, -13, -5, 0, 99, 85, 17, 25, -66, 5, 6, 9, 101, 55, 13, 17, 99, 56, 76, 4, -101, 1000, -1000]

def bubbleSort(array):

    """
    Bubble Sort is the simplest sorting algorithm 
    that works by repeatedly swapping the adjacent elements 
    if they are in wrong order. 

    Worst time complexity: n^2
    Average time complexity: n^2
    Best time complexity: n
    Space complexity: 1

    parameters
    ----------
    array : unsorted array
    """

    for i in range(len(array) - 1):
 
        for j in range(0, len(array) - i - 1):
 
            if array[j] > array[j + 1] :

                array[j], array[j + 1] = array[j + 1], array[j]


def insertionSort(array):

    for i in range(1, len(array)):

        up = array[i]
        j = i - 1

        while j >= 0 and array[j] > up:

            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = up    

    return array    


def selectionSort(array):

    """
    Selection sort algorithm sorts an array 
    by repeatedly finding the minimum element 
    (considering ascending order) from unsorted part 
    and putting it at the beginning.

    Worst time complexity: n^2
    Average time complexity: n^2
    Best time complexity: n^2
    Space complexity: 1

    parameters
    ----------
    array : unsorted array
    """

    for i in range(len(array) - 1):
        smallestIdx = i

        for j in range(i + 1, len(array)):
            if array[j] < array[smallestIdx]:
                smallestIdx = j
            
        temp = array[i]
        array[i] = array[smallestIdx]
        array[smallestIdx] = temp

    return array

def insertionSort(array):

    """
    Insertion sort is a simple sorting algorithm 
    that builds the final sorted array (or list) 
    one item at a time.

    Worst time complexity: n^2
    Average time complexity: n^2
    Best time complexity: n
    Space complexity: 1

    parameters
    ----------
    array : unsorted array
    """

    for i in range(1, len(array)):
        j = i

        while j > 0 and array[j] < array[j - 1]:
            temp = array[j]
            array[j] = array[j - 1]
            array[j - 1] = temp
            j -= 1
        
    return array

def insertionSortInterleaved(array, startIdx, gap):

    """
    Helper function for Shell sort algorithm

    parameters
    ----------
    array : array
        unsorted array
    startIdx : integer
        index of a value from which to start
        sorting algorithm
    gap : integer
        gap between compairing values
    """

    for i in range(startIdx + gap, len(array), gap):
        j = i

        while (j - gap >= startIdx) and (array[j] < array[j - gap]):
            temp = array[j]
            array[j] = array[j - gap]
            array[j - gap] = temp
            j = j - gap

def shellSort(array, gapValues):

    """
    Shell sort method starts by sorting pairs of elements 
    far apart from each other, then progressively reducing
    the gap between elements to be compared.

    Worst complexity: Depends on gap sequence
    Average complexity: n*log(n)^2 or n^(3/2)
    Best complexity: n
    Space complexity: 1

    parameters
    ----------
    array : array
        unsorted array
    gapValues : array
        Number of indexes between compairing values in
        an array.
        Gap values are often chosen in decreasing order. 
        A gap value of 1 is equivalent to the regular 
        insertion sort algorithm.
        Usual gap values: 
            powers of 2 minus 1 is a common choice, 
            in decreasing order. 1 should be the last value.
        The sum of gapValues is the number of times
        insertionSortInterleaved is called.
    """

    for gapValue in gapValues:

        for startIdx in range(gapValue):

            insertionSortInterleaved(array, startIdx, gapValue)

def partition(array, startIdx, endIdx):

    """
    Helper function for Quick sort algorithm

    parameters
    ----------
    array : array
        unsorted array
    startIdx : integer
        index of a value from which to start
        sorting algorithm
    endIdx : integer
        index of a value after which not to use
        sorting algorithm

    returns
    ----------
    high : integer
        last index in left partition segment 
    """
    # Select the middle value as the pivot.
    midpoint = startIdx + (endIdx - startIdx) // 2
    pivot = array[midpoint]
   
    # "low" and "high" start at the ends of the list segment
    # and move towards each other.
    low = startIdx
    high = endIdx
   
    done = False
    while not done:
        # Increment low while array[low] < pivot
        while array[low] < pivot:
            low = low + 1
      
        # Decrement high while pivot < array[high]
        while pivot < array[high]:
            high = high - 1
      
        # If low and high have crossed each other, the loop
        # is done. If not, the elements are swapped, low is
        # incremented and high is decremented.
        if low >= high:
            done = True

        else:
            temp = array[low]
            array[low] = array[high]
            array[high] = temp

            low = low + 1
            high = high - 1
   
    # "high" is the last index in the left segment.
    return high

def quickSort(array, startIdx, endIdx):
    
    """
    Quick sort picks an element as pivot and partitions 
    the given array around the picked pivot. The key process 
    in quickSort is partition(). Target of partitions is, 
    given an array and an element x of array as pivot, 
    put x at its correct position in sorted array and 
    put all smaller elements (smaller than x) before x, 
    and put all greater elements (greater than x) after x.
    Once partitioned, each partition needs to be sorted. 
    Quicksort is typically implemented as a recursive algorithm 
    using calls to quicksort to sort the low and high partitions. 
    This recursive sorting process continues until a partition has 
    one or zero elements, and thus is already sorted.

    Worst complexity: n^2
    Average complexity: n*log(n)
    Best complexity: n*log(n)
    Space complexity: 1

    parameters
    ----------
    array : array
        unsorted array
    startIdx : integer
        index from which to start sorting algorithm
    endIdx : integer
        index where to end sorting algorithm
    """

    # Only attempt to sort the list segment if there are
    # at least 2 elements
    if endIdx <= startIdx:
        return
          
    # Partition the list segment
    high = partition(array, startIdx, endIdx)

    # Recursively sort the left segment
    quickSort(array, startIdx, high)

    # Recursively sort the right segment
    quickSort(array, high + 1, endIdx)

def merge(array, startIdx, midIdx, endIdx):

    """
    Helper function for Merge sort algorithm

    parameters
    ----------
    array : array
        unsorted array
    startIdx : integer
        the start index of the first sorted partition
    midIdx : integer
        the end index of the first sorted partition
    endIdx : integer
        the end index of the second sorted partition
    """

    merged_size = endIdx - startIdx + 1     # Size of merged partition
    merged_array = [0] * merged_size        # Dynamically allocates temporary array
                                            # for merged array
    merge_pos = 0                           # Position to insert merged number
    left_pos = startIdx                     # Initialize left partition start position
    right_pos = midIdx + 1                  # Initialize right partition start position
   
    # Add smallest element from left or right partition to merged array
    while left_pos <= midIdx and right_pos <= endIdx:
        if array[left_pos] <= array[right_pos]:
            merged_array[merge_pos] = array[left_pos]
            left_pos += 1
        else:
            merged_array[merge_pos] = array[right_pos]
            right_pos += 1
        merge_pos += 1
   
    # If left partition is not empty, add remaining elements to merged array
    while left_pos <= midIdx:
        merged_array[merge_pos] = array[left_pos]
        left_pos += 1
        merge_pos += 1
   
    # If right partition is not empty, add remaining elements to merged array
    while right_pos <= endIdx:
        merged_array[merge_pos] = array[right_pos]
        right_pos = right_pos + 1
        merge_pos = merge_pos + 1
   
    # Copy merge number back to array
    for merge_pos in range(merged_size):
        array[startIdx + merge_pos] = merged_array[merge_pos]

def mergeSort(array, startIdx, endIdx):
        
    """
    Merge sort is a sorting algorithm that divides 
    a list into two halves, recursively sorts each half, 
    and then merges the sorted halves to produce a sorted list.

    Worst complexity: n*log(n)
    Average complexity: n*log(n)
    Best complexity: n*log(n)
    Space complexity: n

    parameters
    ----------
    array : array
        unsorted array
    startIdx : integer
        index from which to start sorting algorithm
    endIdx : integer
        index where to end sorting algorithm
    """

    if startIdx < endIdx:
        midIdx = (startIdx + endIdx) // 2  # Find the midpoint in the partition

        # Recursively sort left and right partitions
        mergeSort(array, startIdx, midIdx)
        mergeSort(array, midIdx + 1, endIdx)
            
        # Merge left and right partition in sorted order
        merge(array, startIdx, midIdx, endIdx)

# Returns the maximum length, in number of digits, out of all list elements 
def radixGetMaxLength(array):

    """
    Helper function for radixSort.
    Finds the longest digit in an array.

    parameters
    ----------
    array : array
        unsorted array
    
    returns
    -------
    max_digits : =/=
        maximum lenght of a digit 
        in an array
    """

    max_digits = 0

    for value in array:
        digit_count = len(str(value))

        if digit_count > max_digits:
            max_digits = digit_count
        
    return max_digits

def radixSort(array):
        
    """
    The radix sort algorithm sorts a list of integers 
    by grouping elements based on the element's digits, 
    starting with the least significant digit and ending with 
    the most significant. Two steps are needed for each digit. 
    First, all list elements are placed into buckets based 
    on the current digit's value. Then, the list is rebuilt 
    by removing all elements from buckets, in order from lowest 
    bucket to highest.

    Worst complexity: n*k/d
    Average complexity: n*k/d
    Space complexity: n+2^d

    parameters
    ----------
    array : array
        unsorted array
    """

    buckets = [[] for i in range(10)]

    # Find the max length, in number of digits
    max_digits = radixGetMaxLength(array)
        
    pow_10 = 1
    for digitIdx in range(max_digits):

        for num in array:
            bucket_index = (num // pow_10) % 10
            buckets[bucket_index].append(num)

        array.clear()

        for bucket in buckets:
            array.extend(bucket)
            bucket.clear()
      
        pow_10 = pow_10 * 10
   
    negatives = []
    positives = []

    for num in array:

        if num < 0:
            negatives.append(num)
        else:
            positives.append(num)

    array.clear()
    array.extend(negatives + positives)


# The parameter dir indicates the sorting direction, ASCENDING
# or DESCENDING; if (a[i] > a[j]) agrees with the direction,
# then a[i] and a[j] are interchanged.*/
def compAndSwap(a, i, j, dire):
    if (dire==1 and a[i] > a[j]) or (dire==0 and a[i] < a[j]):
        a[i],a[j] = a[j],a[i]
 
# It recursively sorts a bitonic sequence in ascending order,
# if dir = 1, and in descending order otherwise (means dir=0).
# The sequence to be sorted starts at index position low,
# the parameter cnt is the number of elements to be sorted.
def bitonicMerge(a, low, cnt, dire):
    if cnt > 1:
        k = cnt//2
        for i in range(low , low+k):
            compAndSwap(a, i, i+k, dire)
        bitonicMerge(a, low, k, dire)
        bitonicMerge(a, low+k, k, dire)
 
# This function first produces a bitonic sequence by recursively
# sorting its two halves in opposite sorting orders, and then
# calls bitonicMerge to make them in the same order
def bitonicSort(a, low, cnt,dire):
    if cnt > 1:
          k = cnt//2
          bitonicSort(a, low, k, 1)
          bitonicSort(a, low+k, k, 0)
          bitonicMerge(a, low, cnt, dire)

# Caller of bitonicSort for sorting the entire array of length N
# in ASCENDING order
# Note that this program works only when size of input is a power of 2.
def bitonicCall(a,N, up):
    bitonicSort(a,0, N, up)

             
def bucketSort(array):

    arr = []
    slot_num = 10 # 10 means 10 slots, each
                  # slot's size is 0.1

    for i in range(slot_num):
        arr.append([])
         
    # Put array elements in different buckets
    for j in array:
        index_b = int(slot_num * j)
        arr[index_b].append(j)
     
    # Sort individual buckets
    for i in range(slot_num):
        arr[i] = insertionSort(arr[i])
         
    # concatenate the result
    k = 0
    
    for i in range(slot_num):

        for j in range(len(arr[i])):

            array[k] = arr[i][j]
            k += 1

    return array
