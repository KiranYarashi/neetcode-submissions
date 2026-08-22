class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        hash = {}

        for i in range(len(numbers)):
            remaning = target - numbers[i]
            if remaning in hash:
                return [hash[remaning], i  + 1]
            else:
                hash[numbers[i]] = i +1 
        return []