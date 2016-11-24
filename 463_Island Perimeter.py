class Solution(object):
    def islandPerimeter(self, grid):
        perimeter = 0
        rowIndex = 0
        while rowIndex < len(grid):
            columnIndex = 0
            while columnIndex < len(grid[rowIndex]):
                if grid[rowIndex][columnIndex] == 1:
                    print str(rowIndex)+":"+str(columnIndex)
                    if rowIndex == 0:
                        perimeter += 1
                    elif grid[rowIndex-1][columnIndex] == 0:
                        perimeter += 1
                    if columnIndex == 0:
                        perimeter += 1
                    elif grid[rowIndex][columnIndex-1] == 0:
                        perimeter += 1
                    if rowIndex == len(grid)-1:
                        perimeter += 1
                    elif grid[rowIndex+1][columnIndex] == 0:
                        perimeter += 1
                    if columnIndex == len(grid[rowIndex])-1:
                        perimeter += 1
                    elif grid[rowIndex][columnIndex+1] == 0:
                        perimeter += 1
                columnIndex += 1
            rowIndex += 1
        return perimeter
