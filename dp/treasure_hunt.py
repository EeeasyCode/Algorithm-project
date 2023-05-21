def treasure_hunt():
    array = [[0 for _ in range(maxWeight+1)] for _ in range(rowCount+1)]

    for row in range(1, rowCount+1):
        for col in range(1, maxWeight+1):
            if weight[row] > col:
                array[row][col] = array[row-1][col]
            else:
                value1 = money[row] + array[row-1][col-weight[row]] 
                value2 = array[row-1][col]
                array[row][col] = max(value1, value2)
            print(array[row][col], end='')
        print()
    return array[rowCount][maxWeight]

rowCount = 4
maxWeight = 7
weight = [0, 6, 4, 3, 5]
money = [0, 13, 8, 6, 12]

maxValue = treasure_hunt()

print(maxValue)
