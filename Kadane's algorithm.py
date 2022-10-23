nums = [5, 4, -1, 7, 8]
# BRUTE FORCE APPROACH
# # setting final sum to 1st value
# final_sum = nums[0]
#
# for i in range(len(nums)):
#     # resetting sum to current number
#     sum = nums[i]
#     if final_sum < sum:
#         final_sum = sum
#     for j in range(i+1, len(nums)):
#         sum = sum + nums[j]
#         if final_sum < sum:
#             final_sum = sum

curr_sum = 0
final_sum = 0


for i in range(len(nums)):
    curr_sum = curr_sum + nums[i]
    if final_sum < curr_sum:
        final_sum = curr_sum
    if curr_sum <= 0:
        curr_sum = 0

# checking if all elements are negative
max_nums = max(nums)
if max_nums < 0:
    final_sum = max_nums

