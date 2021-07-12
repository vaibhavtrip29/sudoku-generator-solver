from random import sample, randint

# pattern for a baseline valid solution
def pattern(r,c): return (3*(r%3)+r//3+c)%9

# randomize rows, columns and numbers (of valid base pattern)
def shuffle(s): return sample(s,len(s)) 
rBase = range(3) 
rows  = [ g*3 + r for g in shuffle(rBase) for r in shuffle(rBase) ] 
cols  = [ g*3 + c for g in shuffle(rBase) for c in shuffle(rBase) ]
nums  = shuffle(range(1,3*3+1))

# produce board using randomized baseline pattern
board = [ [nums[pattern(r,c)] for c in cols] for r in rows ]
solution = [ [nums[pattern(r,c)] for c in cols] for r in rows ]

for line in board:
    number = randint(5,10)
    for i in range(0, number):
        removal = randint(0,8)
        line[removal] = 0

def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i
            
            if solve(bo):
                return True
            
            bo[row][col] = 0

    return False

def valid(bo, num, pos):
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
        
    for i in range(len(bo[0])):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range (box_y * 3, box_y*3 + 3):
        for j in range (box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False
    
    return True

def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - -")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)

    return None

print_board(board)
solve(board)
print("            ")
print_board(board)