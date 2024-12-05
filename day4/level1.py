import numpy as np

dict = {
    "X": "M",
    "M": "A",
    "A": "S"
}

counter = 0

class Direction:
    x: int
    y: int

    def __init__(self, x, y):
        self.x = x
        self.y = y

combinations : list[Direction] = [ 
    Direction(0, 1),
    Direction(0, -1),
    Direction(-1, 0),
    Direction(1, 0),
    Direction(1, 1),
    Direction(1, -1),
    Direction(-1, -1),
    Direction(-1, 1)
]

def checkForLetter(posx, posy, DArr, letter = 'M'):
    for comb in combinations:
        try:
            new_x = posx + comb.x            
            new_y = posy + comb.y

            if(DArr[new_x][new_y] == letter):
                checkForLetterDir(dict[letter], new_x, new_y, comb, DArr)
        except:
            1+1

def checkForLetterDir(letter, posx, posy, direction : Direction, DArr):
    try:
        new_x = posx + direction.x
        new_y = posy + direction.y

        if(DArr[new_x][new_y] == letter and new_x >= 0 and new_y >= 0):
            if(letter == "S"):
                global counter
                counter += 1
                return

            checkForLetterDir(dict[letter], new_x, new_y, direction, DArr)
    except:
        1+1

data = open("src/small_input2").read().splitlines()

data2DArray = np.array([list(x) for x in data])

for i in range(len(data2DArray)):
    for j in range(len(data2DArray[i])):
        if(data2DArray[i][j] == "X"):
            checkForLetter(i, j, data2DArray)

print("Counter: ", counter)