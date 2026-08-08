class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict = {}  #store value and index

        if len(nums) == 0:
            return []

        for i  in range(len(nums)):
            duplicate = target - nums[i]  
            if duplicate in myDict:
                return [ myDict[duplicate], i]
            myDict[nums[i]] = i

        return []