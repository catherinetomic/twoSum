class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        newNums = []
        for num in nums:
            a = num * num
            newNums.append(a)
        
        return newNums
    
s = Solution()
nums = [-4,-1,0,3,10]
print(s.sortedSquares(nums))