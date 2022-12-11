def getVisibleTreesOutsideTheGrid(Lines):
    visibleTreesOutsideTheGrid = 0

    columnLen = len(Lines)
    for row in range(columnLen):
        rowLen = len(Lines[row]) - 1
        if (row == 0 or row == columnLen - 1):
            # Add the outer edges
            visibleTreesOutsideTheGrid += rowLen
        else:
            for column in range(rowLen):
                if (column == 0 or column == rowLen - 1):
                    # Add the outer edges
                    visibleTreesOutsideTheGrid += 1
                else:
                    currentTree = Lines[row][column]
                    leftPartOfRow = Lines[row][0:column]
                    rightPartOfRow = Lines[row][column+1:rowLen]
                    topPartOfColumn = ""
                    bottomPartOfColumn = ""
                    for row2 in range(columnLen):
                        if (row2 < row):
                            topPartOfColumn = topPartOfColumn + \
                                Lines[row2][column]
                        elif (row2 > row):
                            bottomPartOfColumn = bottomPartOfColumn + \
                                Lines[row2][column]

                    if (
                        checkIfTreeIsVisible(currentTree, leftPartOfRow) or
                        checkIfTreeIsVisible(currentTree, rightPartOfRow) or
                        checkIfTreeIsVisible(currentTree, topPartOfColumn) or
                        checkIfTreeIsVisible(currentTree, bottomPartOfColumn)
                    ):
                        visibleTreesOutsideTheGrid += 1

    return visibleTreesOutsideTheGrid


def checkIfTreeIsVisible(tree, lineOfTrees):
    tree = int(tree)
    isVisible = True
    for t in lineOfTrees:
        if (int(t) >= tree):
            isVisible = False
            break

    return isVisible


def getScenicScore(Lines):
    scenicScore = 0

    columnLen = len(Lines)
    for row in range(columnLen):
        rowLen = len(Lines[row]) - 1
        if (row == 0 or row == columnLen - 1):
            # Ignore the outer edges
            pass
        else:
            for column in range(rowLen):
                if (column == 0 or column == rowLen - 1):
                    # Ignore the outer edges
                    pass
                else:
                    currentTree = Lines[row][column]
                    leftPartOfRow = Lines[row][0:column]
                    rightPartOfRow = Lines[row][column+1:rowLen]
                    topPartOfColumn = ""
                    bottomPartOfColumn = ""
                    for row2 in range(columnLen):
                        if (row2 < row):
                            topPartOfColumn = topPartOfColumn + \
                                Lines[row2][column]
                        elif (row2 > row):
                            bottomPartOfColumn = bottomPartOfColumn + \
                                Lines[row2][column]

                    leftScore = getVisibleTrees(
                        currentTree, leftPartOfRow[::-1])
                    rightScore = getVisibleTrees(currentTree, rightPartOfRow)
                    topScore = getVisibleTrees(
                        currentTree, topPartOfColumn[::-1])
                    bottomScore = getVisibleTrees(
                        currentTree, bottomPartOfColumn)

                    totalScore = leftScore * rightScore * topScore * bottomScore

                    if (totalScore > scenicScore):
                        scenicScore = totalScore

    return scenicScore


def getVisibleTrees(tree, lineOfTrees):
    tree = int(tree)
    visibleTrees = 0
    for t in lineOfTrees:
        if (int(t) >= tree):
            visibleTrees += 1
            break
        else:
            visibleTrees += 1

    return visibleTrees


if __name__ == '__main__':
    file = open('./day8/input.txt', 'r')
    Lines = file.readlines()

    visibleTreesOutsideTheGrid = getVisibleTreesOutsideTheGrid(Lines)
    print("Visible trees outside the grid: ", visibleTreesOutsideTheGrid)

    scenicScore = getScenicScore(Lines)
    print("Scenic Score: ", scenicScore)
