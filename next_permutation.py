# does not give the correct output, because I misunderstood the logic of this algo.
# but, The code written below was exactly how I wanted to implement it using the peak concept

nums = [1,2,3]
n = len(nums)

# iterating backwards and finding 1st peak from RHS
for i in range(n - 1, -1, -1):
    print(i, "I")
    # Right most element set to peak initially
    if i == n - 1:
        peak = nums[i]
        continue

    # if no peak found till i=0
    if i == 0 and nums[i] >= peak:

        # arrange in ascending order. That is your next permutation
        nums.sort()
        break

    if nums[i] >= peak:
        # set the peak as current val
        peak = nums[i]
        continue

    if nums[i] < peak:
        # peak found :)
        # here nums[i] is the next number after the peak
        # we need to find the next greatest number to nums[i] and swap them
        print("I am here")
        print(peak)
        bigger = peak
        i_bigger = i + 1
        for j in range(i, n):

            if j == i or j == i + 1:
                continue

            if bigger > nums[j + i] > nums[i]:
                bigger = nums[j + i]
                i_bigger = j + i

        print("bigger",bigger)
        print("ib",i_bigger)
        # swapping num[i] with the next greater number to it on RHS
        nums[i], nums[i_bigger] = nums[i_bigger], nums[i]
        print("nums",nums)
        rev = nums[n:i:-1]

        nums[i+1:] = rev[:]

        break
