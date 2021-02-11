def divide(dividend: int, divisor: int) -> int:
    sign = 1
    if dividend < 0:
        dividend *= -1
        sign *= -1
    if divisor < 0:
        divisor *= -1
        sign *= -1
    if divisor == 1:
        ret = dividend*sign
    else:
        result = 0
        while (divisor * 2) <= dividend:
            big_div = divisor*2
            count = 0

            while dividend >= big_div:
                big_div *= 2
                count += 1

            if count > 0:
                result += (2**(count))
                dividend -= (big_div / 2)
        while dividend >= divisor:
            dividend -= divisor
            result += 1

        ret = result * sign
    if ret > 0x7FFFFFFF:
        return 0x7FFFFFFF
    if ret < -0x7FFFFFFF-1:
        return -0x7FFFFFFF-1
    return ret


# print(divide(1000,3))
# print(divide(7,-3))
print(divide(-2147483648, -1))
