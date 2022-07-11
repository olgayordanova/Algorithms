nums = [int(i) for i in input().split()]

def get_sum(inx, nums):
    if inx>=len(nums)-1:
        return nums[inx]
    return nums[inx]+get_sum(inx+1, nums)

print(get_sum(0, nums))