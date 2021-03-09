def longestCommonPrefix(strs: list) -> str:
    l_str = len(strs)
    if not strs or l_str == 0:
        return ""
    return recur_common_prefix(strs, 0, l_str - 1)


def recur_common_prefix(strs, left, right):
    if left == right:
        return strs[left]
    else:
        mid = int((left + right) / 2)
        lcpLeft = recur_common_prefix(strs, left, mid)
        lcpRight = recur_common_prefix(strs, mid + 1, right)
        return commonPrefix(lcpLeft, lcpRight)


def commonPrefix(left_str, right_str):
    min_len = min(len(left_str), len(right_str))
    for i in range(min_len):
        if left_str[i] != right_str[i]:
            return left_str[:i]

    return left_str[:min_len]


if __name__ == "__main__":
    print(longestCommonPrefix(["flower", "flow", "flight"]))
