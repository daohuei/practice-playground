def letterCombinations(digits: str) -> list():
    if digits == "":
        return []
    result = []
    map_list = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    result.append("")
    for i in range(len(digits)):
        x = int(digits[i])
        while len(result[0]) == i:
            t = result.pop(0)
            for s in map_list[x]:
                result.append(t + s)
    return result


# def letterCombinations2(self, digits: str) -> List[str]:

if __name__ == "__main__":
    print(letterCombinations("23"))
