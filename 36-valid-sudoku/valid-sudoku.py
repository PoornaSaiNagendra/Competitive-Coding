class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N, M  = len(board), len(board[0])

        # Checking rows 
        for i in range(N):
            occur = {}
            for j in range(M):
                num = board[i][j]
                if num != '.' and occur.get(num, 0) >= 1:
                    return False
                else:
                    occur[num] = occur.get(num, 0) + 1

        # Checking columns
        for i in range(M):
            occur = {}
            for j in range(N):
                num = board[j][i]
                if num != '.' and occur.get(num, 0) >= 1:
                    return False
                else:
                    occur[num] = occur.get(num, 0) + 1

        # Checking 3x3 grid
        for i in range(0, N, 3):
            for j in range(0, M, 3):
                occur = {}
                for a in range(i, i+3):
                    for b in range(j, j+3):
                        num = board[a][b]
                        if num != '.' and occur.get(num, 0) >= 1:
                            return False
                        else:
                            occur[num] = occur.get(num, 0) + 1
        return True



        