# ----------- TOP K Frequent Elements -----------

# Given an integer array nums and an integer k,
# return the k most frequent elements.
# You must solve it in better than O(n log n) time complexity.

# input
nums = [1, 1, 1, 1, 1, 1]
k = 2


# solution dictionary
def topKFrequent(nums, k):
    # step 1: Count frequencies
    freqs = {}
    for num in nums:
        freqs[num] = freqs.get(num, 0) + 1
    if len(freqs) < k:
        raise Exception("len(set(nums)) < k")
    elif len(freqs) == k:
        return list(freqs.keys())
    print(freqs)

    # step 2: Bucket sort based on frequency
    buckets = [[] for _ in range(len(nums) + 1)]
    for num, freq in freqs.items():
        buckets[freq].append(num)
    print(buckets)

    # step 3: Collect top k frequent elements
    output = []
    for freq in range(len(buckets) - 1, 0, -1):
        for num in buckets[freq]:
            output.append(num)
            if len(output) == k:
                return output


import heapq
from collections import Counter


# O(nlogk), O(n)


# solution heap
def topKFrequent(nums, k):
    # Step 1: Count frequencies
    freqs = Counter(nums)  # O(n)

    # Step 2: Build heap of k elements
    heap = []
    for num, freq in freqs.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)

    # Step 3: Extract elements from heap
    return [num for freq, num in heap]


# ----------- Two Sum -----------
# Given an array of integers nums and an integer target,
# return the indices of the two numbers such that they add up to target.
# Assume exactly one solution
# You cannot use the same element twice
# O(n), O(n)


def twoSum(nums, target):
    seen = {}  # num -> index
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i


# ----------- Three Sum (Medium) -----------
# Given an array nums,
# return all unique triplets [a, b, c] such that:
# a + b + c == 0
# O(n^2), O(n^2) worst case


def threeSum(nums):
    nums.sort()  # O(nlogn)
    result = []

    for i in range(len(nums)):  # O(n)
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # skip duplicates

        left, right = i + 1, len(nums) - 1
        while left < right:  # O(n)
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                # Skip duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1

    return result


# ----------- Longest Substring Without Repeating Characters -----------
# Given a string s,
# find the length of the longest substring without repeating characters
# O(n), O(k), where k is the character set


def lengthOfLongestSubstring(s):
    char_index = {}
    left = 0
    max_len = 0

    for right, char in enumerate(s):
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1  # move left to skip duplicate

        char_index[char] = right
        max_len = max(max_len, right - left + 1)

    return max_len


# ----------- Hash Array -----------
# Given an array param of size n,
# you need to create an array secretKey of size n,
# where each element is any integer
# You compute a hash array where:
# hash[i] = secretKey[i] % param[i]
# Your goal is to choose the secretKey values in such a way
# that the hash array has as many distinct elements as possible
# The goal is to maximize the number of distinct values in hash[i] = secretKey[i] % param[i]
# O(nlogn), O(1)


def computeMaxDistinctHash(param):
    param.sort()  # O(n log n)
    unique = 0  # how many distinct remainders we’ve “reserved” so far
    for p in param:  # try each slot, smallest mod first
        # can this slot still give us a new remainder?
        if unique < p:
            unique += 1
        # otherwise p <= unique, so its entire range 0..p-1 is already “used up”
    return unique


# ----------- Remove character, is string a polyndrome? -----------
# Compute prefix hashes of the original string (so you can get any substring’s hash in O(1)).
# Compute prefix hashes of the reversed string for the same reason.
# For each index i in the string:
#   Use your forward prefix hashes to “cut out” character i by splicing together the hash of s[0:i] and s[i+1:].
#   Do the same on the reversed string at its mirrored index n−1−i.
#   If those two combined hashes match, then removing s[i] yields a palindrome.
#   Count how many i pass that test.
# That's it—no per-index O(n) scans, just O(1) hash operations per i, for an O(n) overall check.
# O(n), O(n)


def countRemovableIndices(s: str) -> int:
    n = len(s)
    B = 131
    M = 10**9 + 7  # Single large prime

    # Precompute powers of B
    p = [1] * (n + 1)
    for i in range(n):
        p[i + 1] = (p[i] * B) % M

    # Compute prefix hashes for s and reversed s
    h = [0] * (n + 1)
    rh = [0] * (n + 1)
    rev = s[::-1]

    for i in range(n):
        v = ord(s[i]) - ord("a") + 1
        h[i + 1] = (h[i] * B + v) % M

    for i in range(n):
        v = ord(rev[i]) - ord("a") + 1
        rh[i + 1] = (rh[i] * B + v) % M

    # Helper to get hash of s[l:r]
    def get_hash(h, l, r):
        x = (h[r] - h[l] * p[r - l]) % M
        return x + M if x < 0 else x

    cnt = 0
    for i in range(n):
        # Remove s[i] → s[:i] + s[i+1:]
        pre = get_hash(h, 0, i)
        suf = get_hash(h, i + 1, n)
        len_suffix = n - 1 - i
        # splice hashes together:
        #   multiply the prefix‐hash by B^Lf (which shifts it 'left' by Lf characters)
        #   then add the suffix‐hash
        #   finally take modulo M
        H = (pre * p[len_suffix] + suf) % M

        # Remove mirrored index from reversed string
        j = n - 1 - i
        rpre = get_hash(rh, 0, j)
        rsuf = get_hash(rh, j + 1, n)
        len_rsuffix = i
        R = (rpre * p[len_rsuffix] + rsuf) % M

        if H == R:
            cnt += 1

    return cnt


# ----------- Count anagramic pairs -----------
# Let’s take: s = "abba"
# All substrings:
#   a, b, b, a, ab, bb, ba, abb, bba, abba
# Valid anagram pairs:
#   "a" ↔ "a"
#   "b" ↔ "b"
#   "ab" ↔ "ba"
#   "abb" ↔ "bba"
# → 4 pairs total.
# O(n^2), O(n^2)

from collections import defaultdict


def count_anagrammatic_pairs(s):
    n = len(s)
    freq_map = defaultdict(int)

    # Generate all substrings
    for i in range(n):  # O(n)
        freq = [0] * 26
        for j in range(i, n):  # O(n(n+1)/2)
            ch = s[j]
            freq[ord(ch) - ord("a")] += 1
            # Use tuple(freq) as the hashable signature
            freq_map[tuple(freq)] += 1

    # Count all valid anagram pairs
    count = 0
    for group_size in freq_map.values():
        if group_size > 1:
            count += group_size * (group_size - 1) // 2

    return count


# ----------- Longest Subarray with Equal Number of 0s and 1s -----------
# Given a binary array (only 0s and 1s),
# find the length of the longest contiguous subarray with equal number of 0s and 1s.
# Example:
#   Input: [0, 1, 0, 1, 1, 0]
#   Output: 6
# O(n), O(n)


def findMaxLength(nums):
    sum_to_index = {0: -1}
    max_len = 0
    current_sum = 0

    for i, num in enumerate(nums):
        current_sum += 1 if num == 1 else -1

        if current_sum in sum_to_index:
            max_len = max(max_len, i - sum_to_index[current_sum])
        else:
            sum_to_index[current_sum] = i

    return max_len
