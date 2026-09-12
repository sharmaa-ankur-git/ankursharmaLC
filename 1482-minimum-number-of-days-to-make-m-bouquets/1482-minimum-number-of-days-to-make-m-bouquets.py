class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        def can_make(day):
            bouquets = consecutive = 0
            for bloom in bloomDay:
                consecutive = consecutive + 1 if bloom <= day else 0
                if consecutive == k:
                    bouquets += 1
                    consecutive = 0
                    if bouquets == m:      # early exit — no need to scan rest
                        return True
            return False
        low, high = min(bloomDay), max(bloomDay)
        while low < high:
            mid = (low + high) // 2
            if can_make(mid):
                high = mid
            else:
                low = mid + 1
        return low