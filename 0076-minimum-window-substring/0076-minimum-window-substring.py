from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        # Frequency map for string t
        target_counts = Counter(t)
        window_counts = {}

        have, need = 0, len(target_counts)
        res, res_len = [-1, -1], float("inf")
        left = 0

        for right, char in enumerate(s):
            window_counts[char] = window_counts.get(char, 0) + 1

            # Check if current character satisfies required count
            if char in target_counts and window_counts[char] == target_counts[char]:
                have += 1

            # Shrink window from the left while it remains valid
            while have == need:
                # Update best result
                window_size = right - left + 1
                if window_size < res_len:
                    res = [left, right]
                    res_len = window_size

                # Remove the left character
                left_char = s[left]
                window_counts[left_char] -= 1
                if left_char in target_counts and window_counts[left_char] < target_counts[left_char]:
                    have -= 1
                left += 1

        l, r = res
        return s[l : r + 1] if res_len != float("inf") else ""
                
            
            
            


        

        