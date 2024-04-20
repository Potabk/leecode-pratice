class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        DP = [[0] * n for _ in range(m)]
        DP[0][0] = grid[0][0]
        for i in range(1, m):
            DP[i][0] = DP[i - 1][0] + grid[i][0]
        for i in range(1, n):
            DP[0][i - 1] = DP[0][i - 1] + grid[0][i]
        for i in range(1, m):
            for j in range(1, n):
                DP[i][j] = min(DP[i - 1][j], DP[i][j - 1]) + grid[i][j]
        return DP[-1][-1]

    def __init__(self):
        pass


if __name__ == '__main__':
    s = Solution()
    a = s.minPathSum([[1, 3, 1],[1, 5, 1],[4, 2, 1]])
    print(a)
