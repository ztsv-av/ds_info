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
        
def find_median(nums1: list, nums2: list):

    m, n = len(nums1), len(nums2)
    if m > n:
        nums1, nums2 = nums2, nums1
    
    total = m + n
    half = (total + 1) // 2

    left, right = 0, m
    while True:
        i = (left + right) // 2
        j = half - i

        L1 = nums1[i] if i > 0 else float("-inf")
        R1 = nums1[i + 1] if i < m else float("inf")
        L2 = nums1[j] if j > 0 else float("-inf")
        R2 = nums1[j + 1] if j < n else float("inf")

        if L1 < R2 and R1 > L2:
            if total % 2 == 1:
                return max(L1, L2)
            else:
                return (max(L1, L2) + min(R1, R2)) / 2.0
        elif L1 < R2:
            left = i + 1
        else:
            right = i - 1
