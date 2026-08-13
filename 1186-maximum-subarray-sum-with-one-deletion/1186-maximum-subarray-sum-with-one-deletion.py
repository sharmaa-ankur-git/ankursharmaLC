class Solution(object):
    def maximumSum(self, arr):
        no_del = arr[0]
        one_del = float('-inf')
        max_sum = arr[0]
        
        for i in range(1, len(arr)):
            x = arr[i]                     
            prev_no_del=no_del
            prev_one_del=one_del                    
            one_del=max(prev_no_del,prev_one_del+x)                
            no_del=max(x,prev_no_del+x)                  
            max_sum=max(max_sum,no_del,one_del)
            
        return max_sum
        
        
        