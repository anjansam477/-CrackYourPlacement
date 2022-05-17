#Find the Duplicate Number, there's only one repeat
def findDuplicate(nums) -> int:
    duplist = []
    dup = 0
    for element in nums:
        if element not in duplist:
            duplist.append(element)
        else:
            dup = element
    return dup

nums = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    nums.append(ele)
print("Duplicate number : ")
print(findDuplicate(nums))

#Floyd's Cycle Detection method (shorter faster and efficient)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
