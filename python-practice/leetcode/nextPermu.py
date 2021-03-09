def nextPermutation(nums: list()) -> None:
    i = len(nums) - 2
    while i >= 0 and nums[i + 1] <= nums[i]:
        i -= 1
    if i < 0:
        reverse(nums, 0)
        print(nums)
        return
    j = len(nums) - 1
    while j >= 0 and nums[j] <= nums[i]:
        j -= 1
    swap(nums, i, j)
    reverse(nums, i + 1)
    print(nums)


def swap(nums, i, j):
    tmp = nums[i]
    nums[i] = nums[j]
    nums[j] = tmp


def reverse(nums, start):
    i = start
    j = len(nums) - 1
    while i < j:
        swap(nums, i, j)
        i += 1
        j -= 1


print(nextPermutation([1, 2, 3]))
print(nextPermutation([3, 2, 1]))
print(nextPermutation([1, 1, 5]))
print(nextPermutation([1, 3, 2]))
