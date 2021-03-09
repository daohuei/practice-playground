def threeSumClosest(nums: list, target: int) -> int:
    nums.sort()
    sub = float("inf")
    for i in range(len(nums) - 2):
        lo = i + 1
        hi = len(nums) - 1
        while lo < hi:
            current_sum = nums[lo] + nums[i] + nums[hi]
            current_sub = current_sum - target
            if abs(current_sub) < abs(sub):
                sub = current_sub
            if current_sum > target:
                hi -= 1
            elif current_sum < target:
                lo += 1
            else:
                sub = 0
                break
        if sub == 0:
            break
    return sub + target


# nums = [-1,2,1,-4], target = 1
if __name__ == "__main__":
    print(threeSumClosest([-1, 2, 1, -4], 1))
