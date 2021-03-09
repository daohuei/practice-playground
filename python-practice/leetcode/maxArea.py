def maxArea(height) -> int:
    max_val = 0
    for i in range(len(height)):
        for j in range(i + 1, len(height)):
            max_val = max(max_val, min(height[i], height[j]) * (j - i))
    return max_val


def maxArea2(height) -> int:
    max_val, count = 0, 0
    r = len(height) - 1
    while count < r:
        max_val = max(max_val, min(height[count], height[r]) * (r - count))
        if height[count] < height[r]:
            count += 1
        else:
            r -= 1
    return max_val


if __name__ == "__main__":
    print(maxArea2([1, 8, 6, 2, 5, 4, 8, 3, 7]))
