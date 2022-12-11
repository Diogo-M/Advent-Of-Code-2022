if __name__ == '__main__':
    file = open('./day1/input.txt', 'r')
    Lines = file.readlines()

    count = 0
    array = []
    # Strips the newline character
    for line in Lines:
        if len(line) == 1:
            array.append(count)
            count = 0
        else:
            count += int(line)

    max = max(array)
    print("Biggest amount of calories: {}".format(max))

    sortedArr = sorted(array, reverse=True)

    print("Top 3 Summed: {}".format(
        sortedArr[0] + sortedArr[1] + sortedArr[2]))
