def romanToInt(s: str) -> int:
    result = 0
    for i in range(len(s)):
        if i < len(s) - 1:
            if r_char_to_int(s[i]) < r_char_to_int(s[i + 1]):
                result -= r_char_to_int(s[i])
            else:
                result += r_char_to_int(s[i])
        else:
            result += r_char_to_int(s[i])
    return result


def r_char_to_int(c):
    return {
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        "I": 1,
    }.get(c, 0)


if __name__ == "__main__":
    print(romanToInt("III"))
    print(romanToInt("IV"))
    print(romanToInt("IX"))
    print(romanToInt("LVIII"))
    print(romanToInt("MCMXCIV"))
