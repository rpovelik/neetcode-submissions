from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num = 0
        rows = len(grid)
        cols = len(grid[0])
        directions = [[1,0], [0,1], [-1,0], [0,-1]]

        def water_down(i, j):
            q = deque()
            q.append((i, j))
            grid[i][j] = '0'

            while q:
                row, col = q.popleft()
                for direction_row, direction_col in directions:
                    new_row = row + direction_row
                    new_col = col + direction_col
                    if (new_row < 0 or new_col < 0
                        or new_row >= rows or new_col >= cols
                        or grid[new_row][new_col] == '0'):
                        continue
                    q.append((new_row, new_col))
                    grid[new_row][new_col] = '0'

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    num += 1
                    water_down(i, j)
        
        return num