class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        n = len(nums)
        if n == 1:
            return
        for i in range(n):
            if i + 1 >= n:
                return
            needSwap = nums[i] < nums[i + 1] if i % 2 else nums[i] > nums[i + 1]
            if needSwap:
                nums[i + 1], nums[i] = nums[i], nums[i + 1]
                continue
