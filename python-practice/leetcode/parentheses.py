left = {
	"(":1,
	"[":2,
	"{":3,
}
right = {
	")":-1,
	"]":-2,
	"}":-3,
}
def isValid(s: str) -> bool:
	c_stack = list()
	for i in range(len(s)):
		if s[i] in left:
			c_stack.append(s[i])
		else:
			if not c_stack:
				return False
			else:
				if left[c_stack.pop()] + right[s[i]] != 0:
					return False
	if not c_stack:
		return True	

if __name__ == '__main__':
	print(isValid("()"))
	print(isValid("()[]{}"))
	print(isValid("(]"))
	print(isValid("([)]"))
	print(isValid("{[]}"))