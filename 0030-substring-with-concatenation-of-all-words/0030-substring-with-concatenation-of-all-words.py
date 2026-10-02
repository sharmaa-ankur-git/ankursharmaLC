from collections import Counter
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        num_words = len(words)
        required = Counter(words)
        n = len(s)
        result = []

        for offset in range(word_len):
            left = offset
            count = 0
            window = {}

            for right in range(offset, n - word_len + 1, word_len):
                word = s[right:right + word_len]

                if word in required:
                    window[word] = window.get(word, 0) + 1
                    count += 1

                    # Shrink window if word count exceeds required
                    while window[word] > required[word]:
                        left_word = s[left:left + word_len]
                        window[left_word] -= 1
                        count -= 1
                        left += word_len

                    if count == num_words:
                        result.append(left)
                else:
                    # Reset window if word is not in required
                    window.clear()
                    count = 0
                    left = right + word_len

        return result
        