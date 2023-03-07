nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

for k in range(len(nums1)):
    if len(nums2) != 0:
        if nums1[k] <= nums2[0] and k < m:
            print(nums1)
            continue
        if nums1[k] > nums2[0] or k > m:
            del nums1[-1]
            nums1.insert(k,nums2[0])
            del nums2[0]
            print(nums1)