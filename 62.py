# 动态规划
# 个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
# 问总共有多少条不同的路径？
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        DP = [[1]*n]+ [[1]+[0]*(n-1) for _ in range(m-1)]
        # DP = [[0] * n for i in range(m)]
        # for i in range(m):
        #     DP[i-1][0] = 1
        # for i in range(n):
        #     DP[0][i-1] = 1
        for i in range(1, m):
            for j in range(1, n):
                DP[i][j] = DP[i - 1][j] + DP[i][j - 1]
        return DP[m-1][n-1]
