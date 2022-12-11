def organizeRucksacksIntoCompartments(Lines):
    rucksacks = []

    for line in Lines:
        lenght = len(line) - 1
        half = int(lenght/2)

        compartmentOne = line[0:half]
        compartmentTwo = line[half:lenght]

        rucksacks.append([compartmentOne, compartmentTwo])

    return rucksacks


def findMatchInCompartments(rucksacks):
    commonLettersArray = []

    for sack in rucksacks:
        commonLetter = list(set(sack[0]) & set(sack[1]))
        commonLettersArray.append(commonLetter[0])

    return commonLettersArray


def givePoints(commomLetters):
    a = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    points = 0

    for letter in commomLetters:
        points += a.find(letter) + 1

    return points


def organizeRucksacksIntoElfGroups(Lines):
    rucksacksByGroup = []
    count = 0
    currentGroup = []

    for line in Lines:
        count += 1
        lenght = len(line) - 1
        currentGroup.append(line[0:lenght])
        if count > 2:
            rucksacksByGroup.append(currentGroup)
            count = 0
            currentGroup = []

    return rucksacksByGroup


def findMatchInGroup(rucksacksByGroup):
    commonLettersArray = []
    for group in rucksacksByGroup:
        for letter in group[0]:
            if (letter in group[1] and letter in group[2]):
                commonLettersArray.append(letter)
                break

    return commonLettersArray


def givePoints(commomLetters):
    a = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    points = 0

    for letter in commomLetters:
        points += a.find(letter) + 1

    return points


if __name__ == '__main__':
    file = open('./day3/input.txt', 'r')
    Lines = file.readlines()

    rucksacks = organizeRucksacksIntoCompartments(Lines)
    commomLetters = findMatchInCompartments(rucksacks)
    points = givePoints(commomLetters)
    print("Points: ", points)

    rucksacksByGroup = organizeRucksacksIntoElfGroups(Lines)
    commonLetterInGroup = findMatchInGroup(rucksacksByGroup)
    pointsByGroup = givePoints(commonLetterInGroup)
    print("Points by group: ", pointsByGroup)
