def countAndSay(n: int) -> str:
    res = "1"
    while n > 1:
        temp = ""
        i = 0
        while i < len(res):
            print(n, temp, res, i)
            num = getRepeatNum(res[i:])
            temp = temp + str(num) + "" + str(res[i])
            i = i + num
        n -= 1
        res = temp
    return res


def getRepeatNum(s):
    count = 1
    same = s[0]
    for i in range(1, len(s)):
        if same == s[i]:
            count += 1
        else:
            break
    return count


print(countAndSay(6))
