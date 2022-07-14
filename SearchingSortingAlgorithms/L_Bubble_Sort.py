nums = [int(x) for x in input().split(' ')]
z=len(nums)-1
while z >0:
    for idx in range(z):
        if nums[idx] > nums[idx+1]:
            nums[idx], nums[idx+1] = nums[idx+1], nums[idx]
    z-=1
print(*nums, sep = " ")