import random

class SudokuGenerator:
    def __init__(self): #스도쿠 판 생성만 AI 사용
        self.grid = [[0]*9 for _ in range(9)]
        self.generate_full_grid()

    # 1. 완성된 스도쿠 판 생성
    def generate_full_grid(self):
        for i in range(81):
            row = i // 9
            col = i % 9
            if self.grid[row][col] == 0:
                nums = list(range(1, 10))
                random.shuffle(nums)
                for num in nums:
                    if self.is_safe(row, col, num):
                        self.grid[row][col] = num
                        if self.generate_full_grid():
                            return True
                        self.grid[row][col] = 0
                return False
        return True

    # 숫자를 넣어도 안전한지 확인
    def is_safe(self, row, col, num):
        # 행/열 검사
        for i in range(9):
            if self.grid[row][i] == num or self.grid[i][col] == num:
                return False
        # 3x3 박스 검사
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.grid[start_row + i][start_col + j] == num:
                    return False
        return True

    # 2. 난이도에 따라 숫자 지우기
    def remove_digits(self, count):
        while count > 0:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            if self.grid[row][col] != 0:
                self.grid[row][col] = 0
                count -= 1

    def print_grid(self):
        for row in self.grid:
            print(row)

    def is_valid(self, board, row, col, num): #판 채우는 건 직접....
        if(board[row][col] != 0):
            return False
        for i in range(8):
            if(board[row][i] == num):
                return False
            if(board[i][col] == num):
                return False
        if(row<3):
            for i in range(3):
                if(col<3):
                    for j in range(3):
                        if(board[i][j] == num):
                            return False
                elif(col<6):
                    for j in range(3, 6):
                        if(board[i][j] == num):
                            return False
                else:
                    for j in range(6, 9):
                        if(board[i][j] == num):
                            return False
            return True
        elif(row<6):
            for i in range(3,6):
                if(col<3):
                    for j in range(3):
                        if(board[i][j] == num):
                            return False
                elif(col<6):
                    for j in range(3, 6):
                        if(board[i][j] == num):
                            return False
                else:
                    for j in range(6, 9):
                        if(board[i][j] == num):
                            return False
            return True
        else:
            for i in range(6,9):
                if(col<3):
                    for j in range(3):
                        if(board[i][j] == num):
                            return False
                elif(col<6):
                    for j in range(3, 6):
                        if(board[i][j] == num):
                            return False
                else:
                    for j in range(6, 9):
                        if(board[i][j] == num):
                            return False
            return True

    def solve_sudoku(self, board): #선배님들의 도움을 받았습니다.
        n = 0
        record = []
        for i in range(9):
            for j in range(9):
                if board[i][j] ==0:
                    record.append([0, i, j])
                    n+=1
        
        solved =  self.back_trace(board, record, 0)
        return solved
        
        
    
    def print_board(self, board):
        for row in board:
            print(row)

    def back_trace(self, board, record, n):
        if len(record) == n:
            return True
        
        x = record[n][1]
        y = record[n][2]

        for k in range(1, 10):
            if self.is_valid(board, x, y, k):
                board[x][y] = k
                if self.back_trace(board, record, n + 1):
                    return True
                board[x][y] = 0
        return False

# 사용 예시
gen = SudokuGenerator()
gen.remove_digits(40) # 40개의 숫자를 지움 (난이도 조절)
gen.print_grid()
print("\n")
puzzle = gen.grid
print("\n")
if (gen.solve_sudoku(puzzle)):
    gen.print_board(puzzle)
else:
    print("값을 찾을 수 없습니다.")