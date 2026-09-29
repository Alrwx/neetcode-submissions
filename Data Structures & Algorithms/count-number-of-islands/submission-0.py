class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0

        dir = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        def dfs(row, col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == '0':
                return

            grid[row][col] = '0'

            for d in dir:
                dfs(row + d[0], col + d[1])

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    dfs(row, col)
                    ans += 1

        return ans
