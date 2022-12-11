def matchLettersPart1(letter, var):
    match letter:
        case "A" | "X":
            var += 1
            return ["Rock", var]
        case "B" | "Y":
            var += 2
            return ["Paper", var]
        case "C" | "Z":
            var += 3
            return ["Scissors", var]


def partOne(Lines):
    myPoints = 0
    enemyPoints = 0
    for line in Lines:
        response = matchLettersPart1(line[2], myPoints)
        myPlay = response[0]
        myPoints = response[1]

        response = matchLettersPart1(line[0], enemyPoints)
        enemyPlay = response[0]
        enemyPoints = response[1]

        if (myPlay == enemyPlay):
            myPoints += 3
            enemyPoints += 3
        elif (myPlay == "Rock" and enemyPlay == "Scissors"):
            myPoints += 6
        elif (myPlay == "Paper" and enemyPlay == "Rock"):
            myPoints += 6
        elif (myPlay == "Scissors" and enemyPlay == "Paper"):
            myPoints += 6
        else:
            enemyPoints += 6

    print("Part 1:")
    print("My Points: {}".format(myPoints))
    print("Enemy Points: {}".format(enemyPoints))


def assignPointsForPlay(letter, var):
    match letter:
        case "A":
            var += 1
            return var
        case "B":
            var += 2
            return var
        case "C":
            var += 3
            return var


def findMyPlay(win, letter):
    match letter:
        case "A":
            return "B" if win == True else "C"
        case "B":
            return "C" if win == True else "A"
        case "C":
            return "A" if win == True else "B"


def partTwo(Lines):
    myPoints = 0
    enemyPoints = 0
    for line in Lines:
        if (line[2] == "Y"):
            # Draw
            myPoints = assignPointsForPlay(line[0], myPoints)
            myPoints += 3
            enemyPoints = assignPointsForPlay(line[0], enemyPoints)
            enemyPoints += 3
        elif (line[2] == "X"):
            # Lose
            myPlay = findMyPlay(False, line[0])
            myPoints = assignPointsForPlay(myPlay, myPoints)
            enemyPoints = assignPointsForPlay(line[0], enemyPoints)
            enemyPoints += 6

        elif (line[2] == "Z"):
            # Win
            myPlay = findMyPlay(True, line[0])
            myPoints = assignPointsForPlay(myPlay, myPoints)
            myPoints += 6
            enemyPoints = assignPointsForPlay(line[0], enemyPoints)

    print("Part 2:")
    print("My Points: {}".format(myPoints))
    print("Enemy Points: {}".format(enemyPoints))


if __name__ == '__main__':
    file = open('./day2/input.txt', 'r')
    Lines = file.readlines()
    partOne(Lines)
    print("--------------------------------------------")
    partTwo(Lines)
