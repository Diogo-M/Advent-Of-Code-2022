def organizeLinesIntoPairs(Lines):
    pairs = []

    for line in Lines:
        lenght = len(line) - 1
        pair = line[0:lenght].split(",")

        elfOne = pair[0].split("-")
        elfOne = [int(elfOne[0]), int(elfOne[1])]
        elfTwo = pair[1].split("-")
        elfTwo = [int(elfTwo[0]), int(elfTwo[1])]

        pairs.append([elfOne, elfTwo])

    return pairs


def countWhereRangeFullyContainsTheOther(pairs):
    count = 0

    for pair in pairs:
        firstInsideSecond = pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1]
        secondInsideFirst = pair[1][0] >= pair[0][0] and pair[1][1] <= pair[0][1]
        if firstInsideSecond or secondInsideFirst:
            count += 1

    return count


def countWhereRangesOverlap(pairs):
    count = 0

    for pair in pairs:
        r = max(pair[0][0], pair[1][0]), min(pair[0][1]+1, pair[1][1]+1)
        test = set(range(*r))

        if (len(test) != 0):
            count += 1

    return count


if __name__ == '__main__':
    file = open('./day4/input.txt', 'r')
    Lines = file.readlines()

    pairs = organizeLinesIntoPairs(Lines)
    count = countWhereRangeFullyContainsTheOther(pairs)
    countRangesOverlap = countWhereRangesOverlap(pairs)
    print("Count part 1: ", count)
    print("Count part 2: ", countRangesOverlap)
