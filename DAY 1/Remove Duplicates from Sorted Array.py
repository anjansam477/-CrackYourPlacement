#as per question the list given is sorted by default
def removeDuplicates(nums):
    i = 1
    for j in range(1, len(nums)):
        if nums[j] != nums[j-1]:
            nums[i] = nums[j]
            i += 1
    print("unique values : ", i)
    return nums

numslist = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    numslist.append(ele)
print("after removing duplicates :", removeDuplicates(numslist))
#as per question the elements after "i" unique values doesn't matter 