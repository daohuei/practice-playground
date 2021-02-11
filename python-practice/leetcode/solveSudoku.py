def solveSudoku(board: list()) -> None:
	solver(board)
def solver(board) -> bool:
	for i in range(9):
		for j in range(9):
			if board[i][j] == ".":
				for count in range(1,10):
					print(board)
					if isValidSudoku(board, str(count), i, j):
						board[i][j] = str(count)
						if solver(board):
							return True
						else:
							board[i][j] = "."
				return False
	return True 

def isValidSudoku(board, nstr, row, col) -> bool:
	if nstr in board[row]: return False
	for co in range(9):
		if nstr == board[co][col]: return False
	start_row = row // 3 * 3
	start_col = col // 3 * 3
	for i in range(3):
		for j in range(3):
			if board[start_row+i][start_col+j] == nstr:
				return False
	return True

valid_s = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
print(solveSudoku(valid_s))