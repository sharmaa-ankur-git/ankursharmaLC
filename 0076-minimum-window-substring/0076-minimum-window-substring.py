class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""

        # Step 1: Frequency map of target string t
        t_dict = {}
        for char in t:
            t_dict[char] = t_dict.get(char, 0) + 1

        required = len(t_dict)  # Number of unique characters to satisfy
        formed = 0              # Number of unique characters currently satisfied

        # Window state tracking
        s_map = {}
        low = 0
        min_len = float("inf")
        best_window = (0, 0)    # Stores (start, end) indices

        # Step 2: Expand window with the high pointer
        for high in range(len(s)):
            char = s[high]
            s_map[char] = s_map.get(char, 0) + 1

            # Check if this character has satisfied its target frequency
            if char in t_dict and s_map[char] == t_dict[char]:
                formed += 1

            # Step 3: Contract window while it contains all target characters
            while formed == required:
                # Update smallest window found so far
                current_len = high - low + 1
                if current_len < min_len:
                    min_len = current_len
                    best_window = (low, high)

                # Remove the leftmost character from the window
                left_char = s[low]
                s_map[left_char] -= 1

                # If dropping left_char breaks the required count, lose the milestone
                if left_char in t_dict and s_map[left_char] < t_dict[left_char]:
                    formed -= 1

                low += 1

        # If min_len never updated, no valid substring exists
        return "" if min_len == float("inf") else s[best_window[0] : best_window[1] + 1]