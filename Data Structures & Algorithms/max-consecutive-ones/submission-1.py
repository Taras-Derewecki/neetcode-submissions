class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOutput = 0
        output = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                output += 1
            else:
                output = 0
            maxOutput = max(output, maxOutput)
        return maxOutput
        