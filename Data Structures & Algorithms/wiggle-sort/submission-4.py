class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        if len(nums) == 1:
            return
        for i in range(len(nums)):
            if i + 1 >= len(nums):
                return
            if i % 2 and nums[i] < nums[i + 1]:
                nums[i + 1], nums[i] = nums[i], nums[i + 1]
                continue
            if not i % 2 and nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                continue
