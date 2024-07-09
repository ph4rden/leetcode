from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # check cols
        for i in range(9): 
            s = set()
            for j in range(9): 
                val = board[j][i]
                if val in s: 
                    return False 
                elif val is not '.': 
                    s.add(val)

        # check rows
        for i in range(9): 
            s = set() 
            for j in range(9): 
                val = board[i][j]
                if board[i][j] in s: 
                    return False 
                elif board[i][j] is not '.': 
                    s.add(board[i][j])
        
        # check 3x3 squares 
        squares = [(0, 0), (0, 3), (0, 6),
                  (3, 0), (3, 3), (3, 6),
                  (6, 0), (6, 3), (6, 6)]

        for i, j in squares: 
            s = set() 
            for row in range(i, i+3): 
                for col in range(j, j+3): 
                    if board[row][col] in s: 
                        return False 
                    elif board[row][col] is not '.': 
                        s.add(board[row][col])
        return True
    
if __name__ == "__main__": 
    sol = Solution()
    board = [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    print(sol.isValidSudoku(board)) # expected true
    