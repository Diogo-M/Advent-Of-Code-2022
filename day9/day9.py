def getVisibleTreesOutsideTheGrid(Lines):
    grid = []
    row = 500
    column = 500

    for i in range(1000):
        gridRow = []
        for x in range(1000):
            gridRow.append(0)
        grid.append(gridRow)
    for line in Lines:
        action = line.replace("\n", "").split(" ")
        match action[0]:
            case "U":
                row -= int(action[1])
            case "D":
                row += int(action[1])
            case "L":
                column -= int(action[1])
            case "R":
                column += int(action[1])

        grid[row][column] = 1
        # if (row < 0):
        #     print("row: ", row)
        # if (column < 0):
        #     print("column: ", column)

    for r in grid:
        for c in r:
            if (c == 1):
                count

    return grid


if __name__ == '__main__':
    file = open('./day9/input.txt', 'r')
    Lines = file.readlines()

    visibleTreesOutsideTheGrid = getVisibleTreesOutsideTheGrid(Lines)
    # print("Visible trees outside the grid: ", visibleTreesOutsideTheGrid)
