def isMatch(s: str, p: str) -> bool:
	if len(p) == 0:
		return (len(s)==0)
	match_1 = len(s) > 0 and (s[0] == p[0] or p[0] == ".")
	if len(p) >= 2 and p[1]=="*":
		return isMatch(s,p[2:]) or (match_1 and isMatch(s[1:], p)) # if first 2 of p were zero, or if already match first one 
	else:
		return match_1 and isMatch(s[1:], p[1:])
def isMatch2(text: str, pattern: str) -> bool:
    if not pattern:
        return not text

    first_match = bool(text) and pattern[0] in {text[0], '.'}

    if len(pattern) >= 2 and pattern[1] == '*':
        return (self.isMatch2(text, pattern[2:]) or
                first_match and self.isMatch2(text[1:], pattern))
    else:
        return first_match and self.isMatch2(text[1:], pattern[1:])
def isMatch3(s: str, p: str) -> bool:
    if s == p:
            return True
    d = {}
        
    def f(si, pi):
        if (si, pi) in d: # this is the main part, if ans is already store, it can cut off all other recursion
            return d[(si, pi)]
        if pi == len(p):
            ans = si == len(s)
        else:
            first = si < len(s) and p[pi] in ('.', s[si]) # s not exceed the length and when first p is "." or first of s
            if pi + 1 < len(p) and p[pi + 1] == '*': # next p is not the last and next is *
                ans = (first and f(si + 1, pi)) or f(si, pi + 2) # if first is right, check next s or check next p after *
            else:
                ans = first and f(si + 1, pi + 1) # if no star and first is true, then check next s and p
            d[(si, pi)] = ans
        return ans
        
    return f(0, 0)


if __name__ == '__main__':
	print(isMatch3("aa","a"))
	print(isMatch3("aa","a*"))
	print(isMatch3("ab",".*"))
	print(isMatch3("abc","c*a*b"))
	print(isMatch3("mississippi","mis*is*p*."))

