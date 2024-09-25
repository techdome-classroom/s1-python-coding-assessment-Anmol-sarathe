def count_islands(grid):
    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    island_count = 0
    
    def dfs(r, c):
        
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 'W':
            return
     
        grid[r][c] = 'W'
   
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'L':
                island_count += 1
                dfs(i, j)  

    return island_count
dispatch_1 = [
    ["L","L","L","L","W"],
    ["L","L","W","L","W"],
    ["L","L","W","W","W"],
    ["W","W","W","W","W"],
]
dispatch_2 = [
    ["L","L","W","W","W"],
    ["L","L","W","W","W"],
    ["W","W","L","W","W"],
    ["W","W","W","L","L"],
]
dispatch_3= [
    ["W", "W", "W", "W"], 
     ["W", "L", "L", "W"],
     ["W", "L", "L", "W"], 
     ["W", "W", "W", "W"]
     ]
print(count_islands(dispatch_1))  
print(count_islands(dispatch_2))  
print(count_islands(dispatch_3))  
