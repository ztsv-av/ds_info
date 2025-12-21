def lengthOfLongestSubstring(s: str = "abcadebf") -> int:
    char_index = {}
    left = 0
    max_len = 0

    for right, char in enumerate(s):
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1
        char_index[char] = right
        max_len = max(max_len, right - left + 1)
    
    return max_len

def longest_increasing_subsequence(s: str = "abcadebf"):

    n = len(s)
    if n == 0:
        return ""
    
    sequence_lengths = [1] * n
    prev_char_idxs = [-1] * n

    best_len = 1
    best_end = 0

    for i in range(n):
        for j in range(i):
            if s[j] < s[i] and sequence_lengths[j] + 1 > sequence_lengths[i]:
                prev_char_idxs[i] = j
                sequence_lengths[i] = sequence_lengths[j] + 1
        if sequence_lengths[i] > best_len:
            best_len = sequence_lengths[i]
            best_end = i

    k = best_end
    out = [s[k]]
    while True:
        k = prev_char_idxs[k]
        if k == -1:
            break
        out.append(s[k])
    out = "".join(reversed(out))
    
    return best_len, out

def longestPalindrome(s: str) -> str:
    def isPalindrome(i: int, j: int):
        left = i
        right = j - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    if len(s) == 0 or len(s) == 1:
        return s

    for length in range(len(s), 0, -1):
        for start in range(len(s) - length + 1):
            if isPalindrome(start, start + length):
                return s[start : start + length]

    return ""
