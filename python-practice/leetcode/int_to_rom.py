def intToRoman(num: int) -> str:
    M = ["", "M", "MM", "MMM"]  # 0,1000,2000,3000
    C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]  # 0,100,200,300...
    X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]  # 0,10,20,30...
    I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]  # 0,1,2,3...
    return M[num // 1000] + C[(num % 1000) // 100] + X[(num % 100) // 10] + I[num % 10]


if __name__ == "__main__":
    print(intToRoman(3))
    print(intToRoman(4))
    print(intToRoman(9))
    print(intToRoman(58))
    print(intToRoman(1994))
