def removeDuplicates(nums: list) -> int:
	if len(nums) == 0:
		return 0
	elif nums[len(nums)-1] == nums[0]:
		return 1
	count = 1
	for i in range(len(nums)-1):
		if nums[i] != nums[i+1]:
			nums[count] = nums[i+1]
			count += 1
	return count

print(removeDuplicates([1,1,2]))
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))