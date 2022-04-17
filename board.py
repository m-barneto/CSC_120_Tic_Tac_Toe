def print_board(board):
  for row in range(len(board)):
    for col in range(len(board[row])):
      print(board[row][col], end='')
    print()


def check_mark(board, x, y):
  return board[y][x] == '-'


def place_mark(board, x, y, playerId):
  if playerId == 1:
    board[y][x] = 'X'
  else:
    board[y][x] = 'O'


def check_win(board, playerId):
  if playerId == 1:
    # Look for 3 in a row of Xs
    if ['X', 'X', 'X'] in board:
      return True
    # Look for 3 in a col of Xs
    for col in range(len(board)):
      if board[0][col] == board[1][col] and board[0][col] == board[2][col] and board[0][col] == 'X':
        return True
    # Check diagonals for Xs
    if board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
      return True
    elif board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X':
      return True
  else:
    # Look for 3 in a row of Os
    if ['O', 'O', 'O'] in board:
      return True
    # Look for 3 in a col of Os
    for col in range(len(board)):
      if board[0][col] == board[1][col] and board[0][col] == board[2][col] and board[0][col] == 'O':
        return True
    # Check diagonals for Os
    if board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O':
      return True
    elif board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O':
      return True
  return False


def main():
  # Unit test print_board
  printBoardTest = [
      ['X', '-', 'O'],
      ['-', 'X', 'X'],
      ['O', '-', 'O']]
  print("Print Board Expected result:\nX-O\n-XX\nO-O")
  print("Print Board Actual result:")
  print_board(printBoardTest)

  # Unit test for check_mark
  checkMarkBoardTest = [
      ['-', '-', 'O'],
      ['-', 'X', 'X'],
      ['O', '-', 'O']]
  print("Check Mark expected for check_mark(board, 0, 0): True")
  print("Check Mark actual for check_mark(board, 0, 0): ",
        check_mark(checkMarkBoardTest, 0, 0))

  # Unit test for place_mark
  placeMarkBoardTest = [
      ['X', '-', 'O'],
      ['-', 'X', 'X'],
      ['O', '-', 'O']]
  print("Board before place_mark(0, 1, 1): ")
  print_board(placeMarkBoardTest)
  place_mark(placeMarkBoardTest, 0, 1, 1)
  print("Board after place_mark(0, 1, 1): ")
  print_board(placeMarkBoardTest)

  # Unit test for check_win
  checkWinBoardTestHori = [
      ['-', '-', '-'],
      ['X', 'X', 'X'],
      ['-', '-', '-']]
  print("Expected result for check_win(checkWinBoardTestHori, 1): True\nResult: ",
        check_win(checkWinBoardTestHori, 1))
  checkWinBoardTestVert = [
      ['-', 'X', '-'],
      ['-', 'X', '-'],
      ['-', 'X', '-']]
  print("Expected result for check_win(checkWinBoardTestVert, 1): True\nResult: ",
        check_win(checkWinBoardTestVert, 1))
  checkWinBoardTestDiag1 = [
      ['X', '-', '-'],
      ['-', 'X', '-'],
      ['-', '-', 'X']]
  print("Expected result for check_win(checkWinBoardTestDiag1, 1): True\nResult: ",
        check_win(checkWinBoardTestDiag1, 1))
  checkWinBoardTestDiag2 = [
      ['-', '-', 'X'],
      ['-', 'X', '-'],
      ['X', '-', '-']]
  print("Expected result for check_win(checkWinBoardTestDiag2, 1): True\nResult: ",
        check_win(checkWinBoardTestDiag2, 1))


main()
