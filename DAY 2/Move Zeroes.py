#move all 0's to the end of it while maintaining the relative order of the non-zero elements
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i, j = 0, 0
        def swap(m,n):
            temp = nums[m]
            nums[m] = nums[n]
            nums[n] = temp
        while j < len(nums):
            if nums[j] != 0:
                swap(i, j)
                i+=1
            j+=1