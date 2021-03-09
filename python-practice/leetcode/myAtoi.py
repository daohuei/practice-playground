def myAtoi(str: str) -> int:
    if len(str) == 0:
        return 0
    sign_bool = False
    neg = False
    result = ""
    for s in str:
        if s == " ":
            if len(result) > 0 or sign_bool:
                break
            continue
        elif s == "-" and not sign_bool and len(result) == 0:
            sign_bool = True
            neg = True
        elif s == "+" and not sign_bool and len(result) == 0:
            sign_bool = True
        elif s >= "0" and s <= "9":
            result += s
        elif result != "":
            break
        else:
            return 0
    if len(result) > 0:
        if neg:
            if int(result) * (-1) > -0x7FFFFFFF - 1:
                return int(result) * (-1)
            else:
                return int(-0x7FFFFFFF - 1)
        else:
            if int(result) < 0x7FFFFFFF:
                return int(result)
            else:
                return int(0x7FFFFFFF)
    return 0


def myAtoi2(s: str) -> int:
    int_max = 0x7FFFFFFF
    int_min = -0x7FFFFFFF - 1

    trimmedStr = s.strip()  # eliminate space
    numericStr = ""

    if (
        trimmedStr
        and (trimmedStr[0].isdigit())
        or (
            len(trimmedStr) > 1
            and trimmedStr[0] in ["+", "-"]
            and trimmedStr[1].isdigit()
        )
    ):
        numericStr = trimmedStr[0]
        for char in trimmedStr[1:]:
            if char.isdigit():
                numericStr += char
            else:
                break

        print(numericStr)
        result = int(numericStr)
    else:
        return 0

    return max(int_min, min(int_max, result))


if __name__ == "__main__":
    print(myAtoi2("+0-1"))
