def partition(array, start_idx, end_idx):
    # select the middle value as the pivot
    midpoint = start_idx + (end_idx - start_idx) // 2
    pivot = array[midpoint]
   
    # "low" and "high" start at the ends of the list segment and move towards each other
    low = start_idx
    high = end_idx
   
    print(f"{array}, pivot: {pivot}, start_idx: {start_idx}, end_idx: {end_idx}")

    done = False
    while not done:
        while array[low] < pivot:
            low = low + 1
        while pivot < array[high]:
            high = high - 1
        print(f"    low: {low}, high: {high}")
      
        # if low and high have crossed each other, the loop is done
        if low >= high:
            print("    done")
            done = True
        # if not, the elements are swapped, low is incremented and high is decremented
        else:
            temp = array[low]
            array[low] = array[high]
            array[high] = temp

            low = low + 1
            high = high - 1
        print(f"    {array}, low: {low}, high: {high}")
   
    # "high" is the last index in the left segment
    return high

def quickSort(array, start_idx, end_idx):
    """
    Hoare version.

    Worst complexity: n^2
    Average complexity: n*log(n)
    Best complexity: n*log(n)
    Space complexity: 1
    """
    if end_idx <= start_idx:
        return
          
    # partition the list segment
    high = partition(array, start_idx, end_idx)
    # recursively sort the left segment
    quickSort(array, start_idx, high)
    # recursively sort the right segment
    quickSort(array, high + 1, end_idx)

quickSort([3, 2, 5, 0, 1, 8, 7, 6, 4], 0, 8)
