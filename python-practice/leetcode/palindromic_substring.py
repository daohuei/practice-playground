def pali_substr(s):
    pal = {}
    max_result = [0, 0]
    processed_s = "$"
    for ca in s:
        processed_s += ca + "$"

    m = len(processed_s)  # 5
    for i in range(m):  # 0~4
        for j in range((m) // 2):  # 0~1
            if i - (j + 1) >= 0 and i + j + 1 < m:
                print(processed_s[i], processed_s[i + j + 1], processed_s[i - (j + 1)])
                if processed_s[i + j + 1] != processed_s[i - (j + 1)]:
                    pal[i] = (j + 1 - 1) * 2 + 1
                    if pal[i] > max_result[1]:
                        max_result = [i, pal[i]]
                    break
                else:
                    pal[i] = (j + 1) * 2 + 1
                    if pal[i] > max_result[1]:
                        max_result = [i, pal[i]]
            else:
                pal[i] = (j + 1 - 1) * 2 + 1
                if pal[i] > max_result[1]:
                    max_result = [i, pal[i]]
                break
    a = max_result[0]
    b = max_result[1]
    c = (b - 1) // 2
    result = ""
    for n in range(a - c, a + c + 1):
        result += processed_s[n]
    print(result)
    print(result.replace("$", ""))


def pali_substr2(s):
    if not s:
        return ""
    max_len = 1  # the length of longest substring
    st = 0  # start point
    print(s[1:2])
    for i in range(1, len(s)):
        print(i)
        print(s[i - max_len - 1 : i + 1], s[i - max_len - 1 : i + 1][::-1])
        if (
            i - max_len > 0
            and s[i - max_len - 1 : i + 1] == s[i - max_len - 1 : i + 1][::-1]
        ):
            st = i - max_len - 1
            max_len += 2
            continue
        print(s[i - max_len : i + 1], s[i - max_len : i + 1][::-1])
        if i - max_len >= 0 and s[i - max_len : i + 1] == s[i - max_len : i + 1][::-1]:
            st = i - max_len
            max_len += 1
    return s[st : st + max_len]


if __name__ == "__main__":
    input_str = "abcdaade"
    pali_substr(input_str)
    print(pali_substr2(input_str))
