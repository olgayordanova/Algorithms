def reversed_nums(nums, k):
    if k+1 > len(nums)//2:
        return nums
    nums[k], nums[len(nums)-1-k] = nums[len(nums)-1-k], nums[k]
    reversed_nums(nums, k+1)
    return nums

nums=list(input().split(' '))
rev_nums = reversed_nums(nums, 0)
print(" ".join([str(el) for el in rev_nums]))


