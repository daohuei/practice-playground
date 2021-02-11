import math
def isPalindrome(x: int) -> bool:
	if x < 0: return False
	digits = int(math.log(x,10) + 1)
	print(digits)
	revert,pop = 0,0
	for i in range(int(digits/2)):
		pop = x % 10
		revert = revert * 10 + pop
		x = int(x/10)
	# when x is even
	if digits % 2 == 0 and x == revert:
		return True
	# when x is odd    
	if digits % 2 != 0 and int(x / 10) == revert:
		return True
   
	return False

if __name__ == '__main__':
	print(isPalindrome(4142332414))