class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        ans = 0
        n = len(board)
        m = len(board[0])
        for i in range(n):
            for j in range(m):
                if board[i][j]=='X' and ((j==0 or board[i][j-1]!='X') and (i==0 or board[i-1][j]!='X')):
                    ans += 1
        return ans
