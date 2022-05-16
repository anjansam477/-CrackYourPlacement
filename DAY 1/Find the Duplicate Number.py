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