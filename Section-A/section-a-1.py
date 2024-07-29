''' SECTION A: QUESTION 1
Median of Two Sorted Arrays
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
'''
def arrays_median(nums1, nums2):
    
    # Lets make sure nums1 is the smaller array. This ensures that the binary search is performed on the smaller array
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    # Lets calculate the total length and half length of the combined arrays
    total_len = len(nums1) + len(nums2)
    half_len = total_len // 2

    # Lets initialize our binary search range
    left, right = 0, len(nums1) - 1
    while True:
        # Let us partition nums1 and nums2 array
        i = (left + right) // 2
        j = half_len - i - 2

        # Get the left and right elements around the partition for nums1 array
        nums1_left = nums1[i] if i >= 0 else float('-infinity')
        nums1_right = nums1[i + 1] if (i + 1) < len(nums1) else float('infinity')

        # Get the left and right elements around the partition for nums2 array
        nums2_left = nums2[j] if j >= 0 else float('-infinity')
        nums2_right = nums2[j + 1] if (j + 1) < len(nums2) else float('infinity')

        # We perform a check to see if we have found the correct partitions
        if nums1_left <= nums2_right and nums2_left <= nums1_right:

            # If the total length is odd, we return the minimum of the right elements
            if total_len % 2 == 1:
                return f"{min(nums1_right, nums2_right):.5f}"

            # If the total length is even, we return the average of the middle two elements
            return f"{(max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2:.5f}"

        # If the value of the left element in around the partition of the nums1 array is greater than the value of the right element of the nums2 array, we move the partition in nums1 to the left, else, we move the partition in nums1 to the right
        elif nums1_left > nums2_right:
            right = i - 1
        else:
            left = i + 1

# Example usage:
# nums1 = [1, 3]
# nums2 = [2]
# print(arrays_median(nums1, nums2))

# nums1 = [1, 2]
# nums2 = [3, 4]
# print(arrays_median(nums1, nums2))

# Fuzz data
# nums1 = [76, 57, 19, 87, 62, 23, 87]
# nums2 = [57, 10, 2, 40, 40, 35, 36, 59, 43, 7, 98, 90, 33, 11]
# nums3 = [67, 47, 63, 40, 29, 65, 100, 7, 69, 57, 59, 36, 68, 33, 16]
# nums4 = [7, 10, 45, 21, 71, 27, 97, 73, 25]

# print(arrays_median(nums1, nums2))
# print(arrays_median(nums3, nums4))