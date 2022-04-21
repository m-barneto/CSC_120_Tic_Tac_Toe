import sqlite3
from datetime import datetime

def print_board(board, returnStr=False):
  boardStr = ''
  for row in range(len(board)):
    for col in range(len(board[row])):
      if returnStr:
        boardStr += board[row][col]
      else:
        print(board[row][col], end='')
    if returnStr:
      boardStr += '\n'
    else:
      print()
  if returnStr:
    return boardStr


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


def is_draw(board):
  for row in range(len(board)):
    for col in range(len(board[row])):
      if board[row][col] == '-':
        return False
  return True


def is_game_complete(board):
  if is_draw(board):
    return 3
  winner = 0
  if check_win(board, 1):
    winner = 1
  elif check_win(board, 2):
    winner = 2
  return winner


def valid_move(move, board):
  if move.count(',') != 1:
    return "Unexpected format. Please enter a value such as: 0,2"
  try:
    temp = move.split(',')
    x = int(temp[0])
    y = int(temp[1])
  except ValueError:
    return 'Please enter two integers between 0 and 2. ex: 0,2'
  if x < 0 or x > 2 or y < 0 or y > 2:
    return 'Out of range, please enter values between 0-2.'
  if not check_mark(board, x, y):
    return 'Space is occupied.'

  return 'valid'


def test():
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


def main():
  board = [
      ['-', '-', '-'],
      ['-', '-', '-'],
      ['-', '-', '-']]
  playerTurn = 1
  winner = is_game_complete(board)
  moves = 0

  conn = sqlite3.connect('tictactoe.db')
  cur = conn.cursor()

  # Create table
  cur.execute('CREATE TABLE IF NOT EXISTS games (date text, final_board text, winner text, move_count real)')
  conn.commit()

  while winner == 0:
    print_board(board)
    move = input("Player " + str(playerTurn) +
                 " please enter your move (x,y): ")
    is_valid = valid_move(move, board)
    while is_valid != 'valid':
      print_board(board)
      print("Invalid move:", is_valid)
      move = input("Player " + str(playerTurn) +
                   " please enter your move (x,y): ")
      is_valid = valid_move(move, board)
    temp = move.split(',')
    x = int(temp[0])
    y = int(temp[1])

    place_mark(board, x, y, playerTurn)

    winner = is_game_complete(board)
    moves += 1
    if playerTurn == 1:
      playerTurn = 2
    else:
      playerTurn = 1
  
  winnerText = "Player 1" if winner == 1 else "Player 2" if winner == 2 else "Draw"
  cur.execute(f"INSERT INTO games VALUES ('{datetime.now().strftime('%m/%d/%Y, %H:%M:%S')}','{print_board(board, True)}','{winnerText}',{moves})")
  conn.commit()
  conn.close()

  if winner == 3:
    print("It's a draw!")
  else:
    print("The winner is player", str(winner) + "!")


main()
