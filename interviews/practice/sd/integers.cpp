bool isPalindrome(int x, const std::string& solution_type) {
    if (x < 0 || (x % 10 == 0 && x != 0)) {
        return false;
    }

    if (solution_type == "str") {
        std::string s = std::to_string(x);
        int left = 0;
        int right = s.size() - 1;

        while (left < right) {
            if (s[left] == s[right]) {
                left++;
                right--;
            } else {
                return false;
            }
        }
        return true;
    }

    else if (solution_type == "int") {
        int reversed_half = 0;
        int original = x;

        while (original > reversed_half) {
            reversed_half = reversed_half * 10 + original % 10;
            original /= 10;
        }

        return (original == reversed_half || original == reversed_half / 10);
    }

    return false; // invalid type
}
