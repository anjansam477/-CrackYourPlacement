#list consists of only 0, 1 & 2
def sortColors(nums):
    left, right = 0, len(nums) - 1
    m = 0

    def swap(m,n):
        temp= nums[m]
        nums[m] = nums[n]
        nums[n] = temp

    while m <= right:
        if nums[m] == 0:
            swap(left, m)
            left+=1
        elif nums[m] == 2:
            swap(m, right)
            right-=1
            m-=1
        m+=1
    return(nums)

nums = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    nums.append(ele)
print("After Sort : ")
print(sortColors(nums))