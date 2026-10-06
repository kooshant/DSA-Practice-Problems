class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        hashset = set()

        for num in nums:
            if num in hashset:
                return num
            else:
                 hashset.add(num)

        return -1
        