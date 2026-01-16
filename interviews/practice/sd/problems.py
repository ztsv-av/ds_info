def maxWaterArea(height) -> int:

    def compute_area(i, j):
        min_height = min(height[i], height[j])
        width = j - i
        area = min_height * width
        return area
    
    if len(height) < 2:
        return 0

    i, j = 0, len(height) - 1
    max_area = 0
    while i < j:
        max_area = max(compute_area(i, j), max_area)
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return max_area

def closedBrackets(s: str) -> bool:

    pairs = {"{": "}", "[": "]", "(": ")"}
    stack = []

    for ch in s:
        if ch in pairs:  # opening bracket
            stack.append(ch)
        elif ch in pairs.values():  # closing bracket
            if not stack:
                return False
            if pairs[stack.pop()] != ch:
                return False
        else:
            return False

    return not stack
