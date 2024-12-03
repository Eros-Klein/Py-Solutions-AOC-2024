import numpy as np

def splitVals(data: str) -> list[str]:
    return data.split()

def split_string_numbers(data: str):
    # Apply splitVals to each line using a list comprehension
    return [splitVals(line) for line in data.splitlines()]

# Read data from the file
with open('src/long_input', 'r') as f:
    data = f.read()

# Process the data
productionData = split_string_numbers(data)

firstColumn = [line[0] for line in productionData]
secondColumn = [line[1] for line in productionData]

firstColumn.sort()
secondColumn.sort()

def get_difference(firstVal, secondVal):
    if(firstVal > secondVal):
        return firstVal - secondVal
    else:
        return secondVal - firstVal

func = np.vectorize(get_difference)

results = np.array(func(np.array(firstColumn).astype(int),np.array(secondColumn).astype(int))).sum()

print(results)