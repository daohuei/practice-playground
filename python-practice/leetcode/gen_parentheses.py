def generateParenthesis(n: int) -> list():
    if n == 0:
        return [""]
    else:
        ans = list()
        for i in range(n):
            left = generateParenthesis(i)
            for l in left:
                right = generateParenthesis(n - 1 - i)
                for r in right:
                    ans.append("(" + l + ")" + r)
        return ans


if __name__ == "__main__":
    print(generateParenthesis(3))
