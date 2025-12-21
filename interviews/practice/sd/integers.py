from typing import List

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

    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    m, n = len(nums1), len(nums2)

    total = m + n
    half = (total + 1) // 2

    left, right = 0, m
    while True:
        i = (left + right) // 2
        j = half - i

        L1 = nums1[i - 1] if i > 0 else float("-inf")
        R1 = nums1[i] if i < m else float("inf")
        L2 = nums2[j - 1] if j > 0 else float("-inf")
        R2 = nums2[j] if j < n else float("inf")

        if L1 <= R2 and R1 >= L2:
            if total % 2 == 1:
                return max(L1, L2)
            else:
                return (max(L1, L2) + min(R1, R2)) / 2.0
        elif L1 < R2:
            left = i + 1
        else:
            right = i - 1

def isPalindrome(x: int, solution_type: str) -> bool:
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    if solution_type == "str":
        x = str(x)
        left = 0
        right = len(x) - 1
        while left < right:
            if x[left] == x[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
    elif solution_type == "int":
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x = x // 10
        return (x == reversed_half or x == reversed_half // 10)

def romanToInt(s: str) -> int:
    values = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1,
    }

    out = 0
    prev_value = 0

    for c in reversed(s):
        curr_value = values[c]
        if curr_value < prev_value:
            out -= curr_value
        else:
            out += curr_value
        prev_value = curr_value

    return out

def longestCommonPrefix(strs: List[str]) -> str:
    if not strs:
        return ""
    
    def helper(str1: str, str2: str) -> str:
        if len(str1) > len(str2):
            str1, str2 = str2, str1
        i = 0
        while i < len(str1) and str1[i] == str2[i]:
            i += 1
        return str1[:i]

    prefix = strs[0]
    for s in strs[1:]:
        prefix = helper(prefix, s)
        if not prefix:
            break
    return prefix

def longestCommonPrefixV2(strs: List[str]) -> str:
    if not strs:
        return ""
    
    # use the shortest string as the base; no prefix can be longer than this
    shortest = min(strs, key=len)
    prefix_len = len(shortest)
    
    for s in strs:
        i = 0
        # compare up to current prefix_len
        while i < prefix_len and s[i] == shortest[i]:
            i += 1
        prefix_len = i
        if prefix_len == 0:
            return ""
    
    return shortest[:prefix_len]
