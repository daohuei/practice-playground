def median_sorted(nums1, nums2):
    m = len(nums1)
    n = len(nums2)
    total_len = m + n
    begin1, begin2 = 0, 0
    left, right = 0, 0
    for i in range(int(total_len / 2) + 1):
        left = right
        if begin1 < m and (begin2 >= n or nums1[begin1] < nums2[begin2]):
            right = nums1[begin1]
            begin1 += 1
        else:
            right = nums2[begin2]
            begin2 += 1
    if total_len % 2 != 0:
        print(right)
    else:
        print((left + right) / 2)


if __name__ == "__main__":
    n1 = [1, 3]
    n2 = [3, 4, 5, 6]
    nums1 = [1, 3]
    nums2 = [2]
    median_sorted(nums1, nums2)
    nums1 = [1, 2]
    nums2 = [3, 4]
    median_sorted(nums1, nums2)
