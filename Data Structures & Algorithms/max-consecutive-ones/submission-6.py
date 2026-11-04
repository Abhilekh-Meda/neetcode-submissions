class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counts = []
        ones_count = 0
        for num in nums:
            if num == 1:
                ones_count += 1
                counts.append(ones_count)
            else:
                counts.append(ones_count)
                ones_count = 0
        return max(counts)
            
            
                
            
