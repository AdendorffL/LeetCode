#Two sum

class Solution:
    def twoSum():
        nums = [3, 1, 4, 2]
        dupe = nums.copy()
        target = 7

        for i in nums:
            first_num = nums[0]
            second_num = target - first_num
            nums.pop(0)
            
            if second_num in nums:
                print([dupe.index(int(first_num)), dupe.index(int(second_num))])


Solution.twoSum()