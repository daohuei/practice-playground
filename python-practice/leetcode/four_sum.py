def fourSum(nums: list(), target: int) -> list():
    nums.sort()
    result = list()
    for i in range(len(nums) - 3):
        if nums[i] > target:
            break
        if i == 0 or (i > 0 and nums[i] != nums[i-1]):
            for j in range(i+1, len(nums) - 2):
                if nums[j] > target:
                    break
                if j == i + 1 or (nums[j] != nums[j-1]):
                    low, high = j+1, len(nums) - 1
                    total = target - nums[i] - nums[j]
                    while low < high:
                        if nums[low] + nums[high] > total:
                            high -= 1
                        elif nums[low] + nums[high] < total:
                            low += 1
                        else:
                            result.append([nums[i], nums[j], nums[low], nums[high]])
                            while low+1 < high and nums[low] == nums[low+1]:
                                low += 1
                            while low < high-1 and nums[high] == nums[high-1]:
                                high -= 1
                            low += 1
                            high -= 1
    return result


if __name__ == '__main__':
    print(fourSum([0, 0, 0, 0, 0, 0, 0, 0], 0))
