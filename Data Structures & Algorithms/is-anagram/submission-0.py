class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        for i in s:
            if i in count:
                count[i] = count[i] + 1
            else:
                count[i] = 1
        for i in t:
            if i in count:
                count[i] = count[i] - 1
            else:
                count[i] = -1
        
        for i in count:
           if count[i] != 0:
            return False

        return True 

            