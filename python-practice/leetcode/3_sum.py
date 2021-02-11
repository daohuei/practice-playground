def threeSum(nums: list()) -> list():
    nums.sort()
    result = []
    for i in range(len(nums)-2):
        if i == 0 or (i > 0 and nums[i] != nums[i-1]):
            if nums[i] > 0:
                break
            low, high = i+1, len(nums) - 1
            total = 0 - nums[i]
            while low < high:
                if nums[low] + nums[high] > total:
                    high -= 1
                elif nums[low] + nums[high] < total:
                    low += 1
                else:
                    result.append([nums[i], nums[low], nums[high]])
                    while low+1 < high and nums[low] == nums[low+1]:
                        low += 1
                    while low < high-1 and nums[high] == nums[high-1]:
                        high -= 1
                    low += 1
                    high -= 1

    return result


if __name__ == '__main__':
    print(threeSum([-1, 0, 1, 2, -1, -4]))
