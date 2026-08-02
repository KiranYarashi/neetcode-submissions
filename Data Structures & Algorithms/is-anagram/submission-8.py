class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        myDict = defaultdict(int)

        if len(s) != len(t):
            return False
        for char in s:
            myDict[char] += 1
        for char in t:
            myDict[char] -= 1
        
        for key, value in myDict.items():
            if value !=  0 :
                return False
            
        return True