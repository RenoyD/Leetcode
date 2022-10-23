nums = [2,0,2,1,1,0]

index = 0
for i in range(len(nums)):
    if nums[i] == 0:
        nums[i], nums[index] = nums[index], nums[i]
        index += 1
for i in range(index, len(nums)):
    if nums[i] == 1:
        nums[i], nums[index] = nums[index], nums[i]
        index += 1

print(nums)