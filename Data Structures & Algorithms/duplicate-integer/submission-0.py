class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result = []
        duplicates = 0
        for i in nums:
            if i not in result:
                result.append(i)
            else:
                duplicates+=1
        return duplicates!=0