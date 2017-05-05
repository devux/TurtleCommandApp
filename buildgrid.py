# Initial setup
board = []
print "Enter N value to build grid and hurdles \n",
grid_value = int(raw_input())

# Construct n*n grid layer with n hurdles
for row in range(grid_value):
  board.append([])
  random_value = random.randint(0,grid_value-1)
  for column in range(grid_value):
    if column == random_value & column != 0:
      board[row].append('1')
    else:
      board[row].append('0')

# function to print grid
def print_board(board):
  for row in board:
    print " ".join(row)

print_board(board)      