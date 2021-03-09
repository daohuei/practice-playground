s = "anviaj"
repeat = {}
max_val = 0
start_point = 0
for i in range(len(s)):
    c = s[i]
    if c in repeat and repeat[c] >= start_point:
        start_point = repeat[c] + 1
    length = i - start_point + 1
    repeat[c] = i
    print(start_point)
    print(repeat)
    print(length)
