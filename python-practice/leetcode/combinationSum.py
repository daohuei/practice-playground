def combinationSum(candidates: list(), target: int) -> list():
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
    return ans[target]


print(combinationSum([2, 3, 6, 7], 7))
