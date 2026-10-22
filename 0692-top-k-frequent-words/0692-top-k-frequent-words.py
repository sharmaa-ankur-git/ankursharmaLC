import heapq
from collections import Counter
class WordFreq:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq
    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word  
        return self.freq < other.freq      
class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        count = Counter(words)
        heap = []       
        for word, freq in count.items():
            heapq.heappush(heap, WordFreq(word, freq))
            if len(heap) > k:
                heapq.heappop(heap)  
        result = []
        while heap:
            result.append(heapq.heappop(heap).word)
        return result[::-1]