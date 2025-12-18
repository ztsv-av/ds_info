def sum_equals_k(values: list = [3, 7, 15, -5, 0, 3, 2, 8, 5, 2, 1, 6, 4, -2, -3, -5, 17, 2], k: int = 8):
    """
    Given an array of integers and an integer k, find the total number of continuous subarrays whose sum equals k. 
    The solution should have  O(N) runtime.
    """
    count = 0
    curr = 0
    sum_freqs = {0: 1}
    for i, val in enumerate(values):
        curr += val
        need = curr - k
        if need in sum_freqs:
            print(curr)
            print(need)
            print(sum_freqs)
            print(values[:i+1])
            count += sum_freqs[need]
        sum_freqs[curr] = sum_freqs.get(curr, 0) + 1
    return count
        
