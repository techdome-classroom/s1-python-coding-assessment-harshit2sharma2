class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
    #    write your code here
        class Solution:
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        
        def dfs(r, c):
            if (r < 0 or r >= rows or 
                c < 0 or c >= cols or 
                grid[r][c] == 'W' or (r, c) in visited):
                return
            visited.add((r, c))
            # Traverse the neighboring land cells (up, down, left, right)
            dfs(r-1, c)  # Up
            dfs(r+1, c)  # Down
            dfs(r, c-1)  # Left
            dfs(r, c+1)  # Right
        
        islands_count = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 'L' and (r, c) not in visited:
                    islands_count += 1
                    dfs(r, c)
        
        return islands_count
                    
        return 0


