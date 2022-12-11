def getStartOfPacket(Lines):
    line = Lines[0]
    startOfPacket = ""
    foundPacket = False

    i = 0
    while not foundPacket:
        startOfPacket = line[0 + i:4 + i]
        count = 0
        for char in startOfPacket:
            packetCount = startOfPacket.count(char)
            count += packetCount
        if (count <= 4):
            foundPacket = True
        else:
            foundPacket = False
            i += 1
        count = 0

    return [startOfPacket, i + 4]


def getStartOfMessage(Lines):
    line = Lines[0]
    startOfMessage = ""
    foundMessage = False

    i = 0
    while not foundMessage:
        startOfMessage = line[0 + i:14 + i]
        count = 0
        for char in startOfMessage:
            messageCount = startOfMessage.count(char)
            count += messageCount
        if (count <= 14):
            foundMessage = True
        else:
            foundMessage = False
            i += 1
        count = 0

    return [startOfMessage, i + 14]


if __name__ == '__main__':
    file = open('./day6/input.txt', 'r')
    Lines = file.readlines()

    result = getStartOfPacket(Lines)
    print("Start of packet: ", result[0])
    print("Characters processed: ", result[1])

    result = getStartOfMessage(Lines)
    print("Start of message: ", result[0])
    print("Characters processed: ", result[1])
