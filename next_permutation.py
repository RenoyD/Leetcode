nums = [3,2,1]
n = len(nums)

def ascending(nums):
    nums.sort()
    return nums

def next_permutation(nums, peak, index):

    #swapping of peak with LHS of it
    x = nums[index-1]
    nums[index-1] = peak
    nums[index] = x

    #sorting the next values in ascending order
    asc = ascending(nums[index+1::])
    nums[index+1::] = asc[::]

#iterating backwards and finding 1st peak from RHS
for i in range(n-1, -1, -1):
    #Right most element set to peak
    if i == n-1:
        peak = nums[i]
        continue

    # if no peak found till i=0
    if i == 0 and nums[i] >= peak:
        #arrange in ascending order
        print(ascending(nums))
        break

    if nums[i] >= peak:
        #set the peak as current val
        peak = nums[i]
        continue

    if nums[i] < peak:
        #peak found :)
        next_permutation(nums, peak, i+1)
        break





