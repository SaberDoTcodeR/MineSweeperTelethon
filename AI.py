import random


def isInsideGrid(i, j):
    if i >= 8 or j >= 7 or i < 0 or j < 0:
        return False
    return True

probTable = []

def addProb(prob, i, j, minesTable):
    global probTable
    if isInsideGrid(i - 1, j - 1) and minesTable[i - 1][j - 1] == -1 and probTable[i - 1][j - 1] != 0:
        probTable[i - 1][j - 1] += prob
    if isInsideGrid(i - 1, j + 1) and minesTable[i - 1][j + 1] == -1 and probTable[i - 1][j + 1] != 0:
        probTable[i - 1][j + 1] += prob
    if isInsideGrid(i - 1, j) and minesTable[i - 1][j] == -1 and probTable[i - 1][j] != 0:
        probTable[i - 1][j] += prob

    if isInsideGrid(i, j - 1) and minesTable[i][j - 1] == -1 and probTable[i][j - 1] != 0:
        probTable[i][j - 1] += prob
    if isInsideGrid(i, j + 1) and minesTable[i][j + 1] == -1 and probTable[i][j + 1] != 0:
        probTable[i][j + 1] += prob

    if isInsideGrid(i + 1, j - 1) and minesTable[i + 1][j - 1] == -1 and probTable[i + 1][j - 1] != 0:
        probTable[i + 1][j - 1] += prob
    if isInsideGrid(i + 1, j + 1) and minesTable[i + 1][j + 1] == -1 and probTable[i + 1][j + 1] != 0:
        probTable[i + 1][j + 1] += prob
    if isInsideGrid(i + 1, j) and minesTable[i + 1][j] == -1 and probTable[i + 1][j] != 0:
        probTable[i + 1][j] += prob

    if isInsideGrid(i - 1, j - 1) and minesTable[i - 1][j - 1] == -1 and prob==0:
        probTable[i - 1][j - 1] = prob
    if isInsideGrid(i - 1, j + 1) and minesTable[i - 1][j + 1] == -1 and prob==0:
        probTable[i - 1][j + 1] = prob
    if isInsideGrid(i - 1, j) and minesTable[i - 1][j] == -1 and prob==0:
        probTable[i - 1][j] = prob

    if isInsideGrid(i, j - 1) and minesTable[i][j - 1] == -1 and prob==0:
        probTable[i][j - 1] = prob
    if isInsideGrid(i, j + 1) and minesTable[i][j + 1] == -1 and prob==0:
        probTable[i][j + 1] = prob

    if isInsideGrid(i + 1, j - 1) and minesTable[i + 1][j - 1] == -1 and prob==0:
        probTable[i + 1][j - 1] = prob
    if isInsideGrid(i + 1, j + 1) and minesTable[i + 1][j + 1] == -1 and prob==0:
        probTable[i + 1][j + 1] = prob
    if isInsideGrid(i + 1, j) and minesTable[i + 1][j] == -1 and prob==0:
        probTable[i + 1][j] = prob



def find_certain_bombs(minesTable):
    global probTable
    remainedBomb = calBombs(minesTable)
    #t(remainedBomb / calClickable(minesTable))
   # print(remainedBomb // calClickable(minesTable))
    probTable = [[remainedBomb / calClickable(minesTable) for i in range(7)] for j in range(8)]
    for i in range(8):
        for j in range(7):
            #print(i, j, "iters")
            if minesTable[i][j] != -1:
                numOfBomb = minesTable[i][j]
                poss = 0
                directions = []
                if numOfBomb > 0:
                    if isInsideGrid(i - 1, j - 1):
                        if minesTable[i - 1][j - 1] == -1 and probTable[i - 1][j - 1] != 0:
                            poss += 1
                            directions.append((i - 1, j - 1))
                        elif minesTable[i - 1][j - 1] == -2:
                            numOfBomb -= 1
                    if isInsideGrid(i - 1, j):
                        if minesTable[i - 1][j] == -1 and probTable[i - 1][j] != 0:
                            poss += 1
                            directions.append((i - 1, j))
                        elif minesTable[i - 1][j] == -2:
                            numOfBomb -= 1
                  #  print(i, j, "iters1")
                    if isInsideGrid(i - 1, j + 1):
                        if minesTable[i - 1][j + 1] == -1 and probTable[i - 1][j + 1] != 0:
                            poss += 1
                            directions.append((i - 1, j + 1))
                        elif minesTable[i - 1][j + 1] == -2:
                            numOfBomb -= 1
                    if isInsideGrid(i, j - 1):
                        if minesTable[i][j - 1] == -1 and probTable[i][j - 1] != 0:
                            poss += 1
                            directions.append((i, j - 1))
                        elif minesTable[i][j - 1] == -2:
                            numOfBomb -= 1
                   # print(i, j, "iters2")
                    if isInsideGrid(i, j + 1):
                        if minesTable[i][j + 1] == -1 and probTable[i][j + 1] != 0:
                            poss += 1
                            directions.append((i, j + 1))
                        elif minesTable[i][j + 1] == -2:
                            numOfBomb -= 1
                    if isInsideGrid(i + 1, j - 1):
                        if minesTable[i + 1][j - 1] == -1 and probTable[i + 1][j - 1] != 0:
                            poss += 1
                            directions.append((i + 1, j - 1))
                        elif minesTable[i + 1][j - 1] == -2:
                            numOfBomb -= 1
                  #  print(i, j, "iters3")
                    if isInsideGrid(i + 1, j):
                        if minesTable[i + 1][j] == -1 and probTable[i + 1][j] != 0:
                            poss += 1
                            directions.append((i + 1, j))
                        elif minesTable[i + 1][j] == -2:
                            numOfBomb -= 1
                    if isInsideGrid(i + 1, j + 1):
                        if minesTable[i + 1][j + 1] == -1 and probTable[i + 1][j + 1] != 0:
                            poss += 1
                            directions.append((i + 1, j + 1))
                        elif minesTable[i + 1][j + 1] == -2:
                            numOfBomb -= 1
                   # print(poss,numOfBomb)
                    if numOfBomb > 0 and numOfBomb == poss:
                        return directions[0]
                    if poss != 0:
                     #   print(numOfBomb / poss,probTable)
                        addProb(numOfBomb / poss, i, j, minesTable)
                    #    print( probTable)
    return None


def empty_table(minesTable):
    for i in range(8):
        for j in range(7):
            if minesTable[i][j] > 0:
                return False
    return True


def calBombs(minesTable):
    count = 0
    for i in range(8):
        for j in range(7):
            if minesTable[i][j] == -2:
                count += 1
    return 15-count


def calClickable(minesTable):
    count = 0
    for i in range(8):
        for j in range(7):
            if minesTable[i][j] == -1:
                count += 1
    return count


def bestShot(minesTable):
    global probTable
    maxim = 0
    retCell = (0,0)
    for i in range(8):
        for j in range(7):
            #print("iter",i,j)
            if probTable[i][j] > maxim and minesTable[i][j] == -1:
                maxim = probTable[i][j]
                retCell = (i, j)
    return retCell


def decide(minesTable):
    dec = find_certain_bombs(minesTable)
    if dec is not None:
        return dec
    if empty_table(minesTable):
        while True:
           # print("empty")
            choice = random.randint(0, 55)
            x_ch = choice // 7
            y_ch = choice % 7
            if minesTable[x_ch][y_ch] == -1:
                return (x_ch, y_ch)
   # print("best")
    return bestShot(minesTable)
