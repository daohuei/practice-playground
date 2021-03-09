def reverse(x):
    if x > 0x7FFFFFFF or x < -0x7FFFFFFF - 1:
        return 0
    neg = False
    if x < 0:
        x = 0 - x
        neg = True
    str_x = str(x)
    m = len(str_x)
    r_x = int(str_x[0:m][::-1])
    if neg:
        r_x = 0 - r_x

    if r_x > 0x7FFFFFFF or r_x < -0x7FFFFFFF - 1:
        return 0
    return r_x


def reverse2(x):
    neg = x < 0
    if neg:
        r_x = -int(str(x)[1:][::-1])
        if r_x > -0x7FFFFFFF - 1:
            return r_x
    else:
        r_x = int(str(x)[::-1])
        if r_x < 0x7FFFFFFF:
            return r_x
    return 0


if __name__ == "__main__":
    print(reverse2(1563847412))
