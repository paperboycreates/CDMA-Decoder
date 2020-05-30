M1 = "ABC"
M2 = "XYZ"

C1 = [1,1,-1,1]
C2 = [-1,1,-1,-1]

DECODING_MAP = {"A" : [1,1,1,1,1], \
                "B" : [1,1,1,1,-1], \
                "C" : [1,1,1,-1,1], \
                "D" : [1,1,1,-1,-1], \
                "E" : [1,1,-1,1,1], \
                "F" : [1,1,-1,1,-1], \
                "G" : [1,1,-1,-1,1], \
                "H" : [1,1,-1,-1,-1], \
                "I" : [1,-1,1,1,1], \
                "J" : [1,-1,1,1,-1], \
                "K" : [1,-1,1,-1,1], \
                "L" : [1,-1,1,-1,-1], \
                "M" : [1,-1,-1,1,1], \
                "N" : [1,-1,-1,1,-1], \
                "O" : [1,-1,-1,-1,1], \
                "P" : [1,-1,-1,-1,-1], \
                "Q" : [-1,1,1,1,1], \
                "R" : [-1,1,1,1,-1], \
                "S" : [-1,1,1,-1,1], \
                "T" : [-1,1,1,-1,-1], \
                "U" : [-1,1,-1,1,1], \
                "V" : [-1,1,-1,1,-1], \
                "W" : [-1,1,-1,-1,1], \
                "X" : [-1,1,-1,-1,-1], \
                "Y" : [-1,-1,1,1,1], \
                "Z" : [-1,-1,1,1,-1], \
                " " : [-1,-1,1,-1,1], \
                "," : [-1,-1,1,-1,-1], \
                "." : [-1,-1,-1,1,1], \
                "'" : [-1,-1,-1,1,-1], \
                "?" : [-1,-1,-1,-1,1], \
                "!" : [-1,-1,-1,-1,-1]}


def decodeStringToCDMA(stringInput, cdmaCode):
    stringDecodedCDMA = []
    stringDecodedCDMAFinal = ""
    i = 0
    cmdaCodeSize = len(cdmaCode)
    temp = []
    for dataBit in stringInput:
        temp.append(dataBit * cdmaCode[i])
        i = i + 1
        if (len(temp) == cmdaCodeSize):
            stringDecodedCDMA.append(sum(temp)//cmdaCodeSize)
            i = 0
            temp = []        
            
    databitList = [stringDecodedCDMA[i:i+5] for i in range(0,len(stringDecodedCDMA),5)]
    for databyte in databitList:
        for letter in DECODING_MAP:
            if databyte == DECODING_MAP[letter]:
                stringDecodedCDMAFinal = stringDecodedCDMAFinal + letter

    return stringDecodedCDMAFinal

##################################################################################
# MAIN #
##################################################################################
input = []
with open("pa4_transmission.txt", "r") as filestream:
        for line in filestream:
            currentline = line.split(",")
            for data in currentline:
                input.append(data)

input = list(map(int, input))
answer = decodeStringToCDMA(input, C1)
answer2 = decodeStringToCDMA(input, C2)

print(answer2)
print (answer)







