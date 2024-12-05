import numpy as np

dict = {
    "M": "A",
    "A": "S"
}

counter = 0

class Direction:
    x: int
    y: int

    def __init__(self, x, y, direction = None):
        self.x = x
        self.y = y
        if direction is None:
            self.opposite = self
        else: self.opposite = direction

# Left-Down, Left-Up, Right-Down, Right-Up
directions = [
    Direction(-1, 1, Direction(1, -1)),
    Direction(-1, -1, Direction(1, 1)),
    Direction(1, 1, Direction(-1, -1)),
    Direction(1, -1, Direction(-1, 1))
]

def checkForLetter(posx, posy, DArr):
        try:
            counter = 0
            for direction in directions:
                new_x = posx + direction.x
                new_y = posy + direction.y

                if(DArr[new_x][new_y] == "M"):
                    if checkForLetterDir(dict["M"], new_x, new_y, direction.opposite, DArr): 
                        counter += 1
            if counter >= 2:
                return 1
        except:
            1+1
        return 0

def checkForLetterDir(letter, posx, posy, direction : Direction, DArr):
    try:
        new_x = posx + direction.x
        new_y = posy + direction.y

        if(DArr[new_x][new_y] == letter and new_x >= 0 and new_y >= 0):
            if(letter == "S"):
                return True

            return checkForLetterDir(dict[letter], new_x, new_y, direction, DArr)
    except:
        1+1

data = open("src/big_input").read().splitlines()

data2DArray = np.array([list(x) for x in data])

for i in range(len(data2DArray)):
    for j in range(len(data2DArray[i])):
        if(data2DArray[i][j] == "A"):
            counter += checkForLetter(i, j, data2DArray)

print("Counter: ", counter)