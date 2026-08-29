class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        low=0
        longest=0
        n=len(fruits)
        picked={}
        for high in range(n):
            fruit=fruits[high]
            picked[fruit]=picked.get(fruit,0)+1

            while len(picked)>2:
                picked[fruits[low]]-=1
                if picked[fruits[low]]==0:
                    del picked[fruits[low]]
                low+=1
            longest=max(longest,high-low+1)
        return longest
            

        