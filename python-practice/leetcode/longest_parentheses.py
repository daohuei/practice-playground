def longestValidParentheses(s: str) -> int:
    left, right, max_len = 0, 0, 0
    left1, right1 = 0, 0
    s_len = len(s)
    for i in range(s_len):
        if s[i] == "(":
            left += 1
        else:
            right += 1
        if left == right:
            max_len = max(max_len, right * 2)
        elif right >= left:
            right, left = 0, 0

        if s[s_len - 1 - i] == "(":
            left1 += 1
        else:
            right1 += 1
        if left1 == right1:
            max_len = max(max_len, left1 * 2)
        elif left1 >= right1:
            left1, right1 = 0, 0
    return max_len


print(longestValidParentheses("(()"))
print(longestValidParentheses(")()())"))
