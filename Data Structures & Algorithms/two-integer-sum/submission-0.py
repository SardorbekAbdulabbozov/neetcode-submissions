class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = None
        j = None
        map = {v : k for k, v in enumerate(nums)}
        for n in range(len(nums)):
            diff = target - nums[n]
            if diff in map and map[diff] != n:
                i = n
                j = map[diff]
                break

        return [i,j] if i<j else [j,i]
                



            