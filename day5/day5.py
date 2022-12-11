def organizeLinesIntoCratesAndSteps(Lines):
    crates = [[], [], [], [], [], [], [], [], []]
    steps = []

    lineIndex = 0
    for line in Lines:
        lineIndex += 1
        if (line.startswith("m")):
            splitedLine = line.replace("\n", "").replace(
                "move ", "").replace(
                "from ", "").replace(
                "to ", "").split(" ")
            steps.append(splitedLine)
        elif (lineIndex <= 8):
            splitedLine = line.replace("\n", "").replace(
                "    ", " ").split(" ")

            index = 0
            for split in splitedLine:
                if (split != ""):
                    crates[index].append(split)
                index += 1

    return [crates, steps]


def rearrangeCratesCrateMover9000(crates, steps):
    rearrangedCrates = crates.copy()

    for step in steps:
        move = int(step[0])
        moveFrom = int(step[1]) - 1
        moveTo = int(step[2]) - 1
        for x in range(move):
            crate = rearrangedCrates[moveFrom].pop(0)
            rearrangedCrates[moveTo].insert(0, crate)

    return rearrangedCrates


def rearrangeCratesCrateMover9001(crates, steps):
    rearrangedCrates = crates.copy()

    for step in steps:
        move = int(step[0])
        moveFrom = int(step[1]) - 1
        moveTo = int(step[2]) - 1

        moving = rearrangedCrates[moveFrom][0:move]
        moving.reverse()
        del rearrangedCrates[moveFrom][0:move]
        for val in moving:
            rearrangedCrates[moveTo].insert(0, val)

    return rearrangedCrates


def getTopCrates(rearrangedCrates):
    topCrates = ""

    for crate in rearrangedCrates:
        topCrates += crate[0].replace("[", "").replace("]", "")

    return topCrates


if __name__ == '__main__':
    file = open('./day5/input.txt', 'r')
    Lines = file.readlines()

    result = organizeLinesIntoCratesAndSteps(Lines)
    crates = result[0]
    steps = result[1]
    # for crate in crates:
    #     print(crate)
    # print("steps: ", steps)
    rearrangedCrates = rearrangeCratesCrateMover9000(crates, steps)
    # for crate in rearrangedCrates:
    #     print(crate)
    topCrates = getTopCrates(rearrangedCrates)
    print("Crate Mover 9000: ", topCrates)

    result = organizeLinesIntoCratesAndSteps(Lines)
    crates = result[0]
    steps = result[1]
    # for crate in crates:
    #     print(crate)
    # print("steps: ", steps)
    rearrangedCrates = rearrangeCratesCrateMover9001(crates, steps)
    # for crate in rearrangedCrates:
    #     print(crate)
    topCrates = getTopCrates(rearrangedCrates)
    print("Crate Mover 9001: ", topCrates)
