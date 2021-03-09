def combinationSum2(candidates: list(), target: int) -> list():
    candidates.sort()
    ans = {}
    if candidates[0] > target:
        return []
    for i in range(target + 1):
        ans[i] = []
    for i in range(len(candidates)):
        s = candidates[i]
        while s <= target:
            ans_sum = ans[s]
            ans_sub = ans[s - candidates[i]]
            if s == candidates[i]:
                ans_sum.append([candidates[i]])
            if len(ans_sub) > 0:
                for j in range(len(ans_sub)):
                    if type(ans_sub[j]) == type(list()):
                        temp = [sub for sub in ans_sub[j]]
                    else:
                        temp = [ans_sub[j]]
                    temp.append(candidates[i])
                    ans_sum.append(temp)
            s += 1
    return remove(ans[target], candidates)


def remove(ans_target, candi):
    nhmap = {}
    ans = list(ans_target)
    for n in candi:
        s = 0
        if n in nhmap.keys():
            s = nhmap[n]
        nhmap[n] = s + 1
    for i in range(len(ans_target)):
        l = ans_target[i]
        temp = {}
        for n in l:
            s = 0
            if n in temp.keys():
                s = temp[n]
            temp[n] = s + 1
        for n in l:
            if temp[n] > nhmap[n]:
                ans.remove(l)
                break

    temp = []
    for a in ans:
        if a not in temp:
            temp.append(a)
    return temp


print(combinationSum2([2, 3, 6, 7], 7))

print(combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))

print(combinationSum2([2, 5, 2, 1, 2], 5))
