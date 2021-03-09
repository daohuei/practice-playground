def strStr(haystack: str, needle: str) -> int:
    if len(needle) == 0:
        return 0
    j = 0
    index = 0
    count = 0
    while index < len(haystack):
        if haystack[index] == needle[j]:
            count += 1
            if len(needle) == count:
                return index - count + 1
            j += 1
        else:
            index = index - count
            j = 0
            count = 0
        index += 1

    return -1


def strStr2(haystack: str, needle: str) -> int:
    if needle:
        if haystack:
            if haystack == needle:
                return 0
            len_n = len(needle)
            len_h = len(haystack)
            diff = len_h - len_n
            for i in range(diff + 1):
                if haystack[i : i + len_n] == needle:
                    return i
        return -1

    else:
        return 0


print(strStr2(haystack="hello", needle="ll"))
print(strStr2(haystack="aaaaa", needle="bba"))
print(strStr2("mississippi", "issip"))
print(strStr2("mississippi", "issi"))
