class Solution(object):
    def pivotIndex(self, nums):
        
        total = sum(nums)
        left = 0

        for i in range(len(nums)):
            right = total-left-nums[i]

            if left == right:
                return i

            left +=nums[i]

        return -1    

        # brute force

        # for i in range(len(nums)):
        #     left = sum(nums[:i])
        #     right = sum(nums[i+1:])

        #     if left == right:
        #         return i

        # return -1    