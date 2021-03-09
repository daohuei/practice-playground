def searchRange(nums: list(), target: int) -> list():
    start, end = 0, len(nums) - 1
    ans = [-1, -1]
    if end + 1 == 0:
        return ans
    while start <= end:
        mid = (start + end) // 2
        if target == nums[mid]:
            if mid > 0:
                if target > nums[mid - 1]:
                    ans[0] = mid
                    break
                else:
                    end = mid - 1
            elif mid == 0:
                ans[0] = mid
                break
            else:
                end = mid - 1
        elif target < nums[mid]:
            end = mid - 1
        else:
            start = mid + 1
    start, end = 0, len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        if target == nums[mid]:
            if mid < len(nums) - 1:
                if target < nums[mid + 1]:
                    ans[1] = mid
                    break
                else:
                    start = mid + 1
            elif mid == len(nums) - 1:
                ans[1] = mid
                break
            else:
                start = mid + 1
        elif target < nums[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return ans


print(searchRange([5, 7, 7, 8, 8, 10], 8))
print(searchRange([5, 7, 7, 8, 8, 10], 6))
