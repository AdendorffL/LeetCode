class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        complete_list = list(range(0, len(nums) + 1))
        for i in complete_list:
            if i not in nums:
                return(i)
            
Solution.missingNumber([3, 0, 1])