def getSignalStrength(Lines):
    signalStrength = 0
    cycle = 0
    x = 1

    for line in Lines:
        command = line.replace("\n", "").split(" ")

        if (command[0] == "noop"):
            cycle += 1

            if (cycle == 20 or cycle % 40 - 20 == 0):
                signalStrength += cycle * x
        else:
            cycle += 1
            if (cycle == 20 or cycle % 40 - 20 == 0):
                signalStrength += cycle * x
            cycle += 1
            if (cycle == 20 or cycle % 40 - 20 == 0):
                signalStrength += cycle * x

            x += int(command[1])

    return signalStrength


def drawSprite(Lines):
    sprite = []
    currentCTRRow = ""
    cycle = 0
    x = 1

    for line in Lines:
        command = line.replace("\n", "").split(" ")

        if (command[0] == "noop"):
            cycle += 1
            currentCTRRow += getLitOrNotLitPixel(x, cycle)

            if (cycle % 40 == 0 and cycle != 0):
                cycle = 0
                sprite.append(currentCTRRow)
                currentCTRRow = ""
        else:
            cycle += 1
            currentCTRRow += getLitOrNotLitPixel(x, cycle)

            if (cycle % 40 == 0 and cycle != 0):
                cycle = 0
                sprite.append(currentCTRRow)
                currentCTRRow = ""

            cycle += 1
            currentCTRRow += getLitOrNotLitPixel(x, cycle)

            if (cycle % 40 == 0 and cycle != 0):
                cycle = 0
                sprite.append(currentCTRRow)
                currentCTRRow = ""

            x += int(command[1])

    return sprite


def getLitOrNotLitPixel(x, cycle):
    xLeft = x - 1
    xRight = x + 1
    cycle -= 1

    if (x == cycle or xLeft == cycle or xRight == cycle):
        return "#"
    else:
        return "."


if __name__ == '__main__':
    file = open('./day10/input.txt', 'r')
    Lines = file.readlines()

    signalStrength = getSignalStrength(Lines)
    print("Signal Strength: ", signalStrength)

    sprite = drawSprite(Lines)
    print("Sprite:")
    for x in sprite:
        print(x)
