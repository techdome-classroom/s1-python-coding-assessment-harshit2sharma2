class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
    #    write your code here
        def count_islands(map):
    


    rows = len(map)
    cols = len(map[0])
    visited = [[False] * cols for _ in range(rows)]
    islands = 0

    def dfs(i, j):
        if i < 0 or i >= rows or j < 0 or j >= cols or map[i][j] != 'L' or visited[i][j]:
            return
        visited[i][j] = True
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    for i in range(rows):
        for j in range(cols):
            if map[i][j] == 'L' and not visited[i][j]:
                islands += 1
                dfs(i, j)

    return islands

# Example usage:
map1 = [
    ["L", "L", "L", "L", "W"],
    ["L", "L", "W", "L", "W"],
    ["L", "L", "W", "W", "W"],
    ["W", "W", "W", "W", "W"]
]

map2 = [
    ["L", "L", "W", "W", "W"],
    ["L", "L", "W", "W", "W"],
    ["W", "W", "W", "W", "W"],
    ["W", "W", "W", "W", "W"]
]

print(count_islands(map1))  # Output: 1
print(count_islands(map2))  # Output: 2
                    
        return 0


