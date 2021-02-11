def searchInsert(nums: list(), target: int) -> int:
	start, end = 0, len(nums)
	if len(nums) == 0:
		return 0
	while start < end:
		mid = (start + end) // 2
		if target == nums[mid]:
			return mid
		elif target < nums[mid]:
			end = mid
		else:
			start = mid + 1	
	return start

print(searchInsert([1,3,5,6], 7))
print(searchInsert([1,3,5,6], 0))