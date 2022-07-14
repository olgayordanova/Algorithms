nums = [int(x) for x in input().split(' ')]


for idx in range(len(nums)):
    z = idx
    while z > 0 and nums[z] < nums[z-1]:
        nums[z-1], nums[z] = nums[z], nums[z-1]
        z-=1

print(*nums, sep = " ")