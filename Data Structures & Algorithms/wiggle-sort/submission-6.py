class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        n = len(nums)
        for i in range(n - 1):
            needSwap = nums[i] < nums[i + 1] if i % 2 else nums[i] > nums[i + 1]
            if needSwap:
                nums[i + 1], nums[i] = nums[i], nums[i + 1]
                continue
