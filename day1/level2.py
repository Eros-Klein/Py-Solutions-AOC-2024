import numpy as np

def splitVals(data: str) -> list[str]:
    return data.split()

def split_string_numbers(data: str):
    return [splitVals(line) for line in data.splitlines()]

with open('src/long_input', 'r') as f:
    data = f.read()

productionData = split_string_numbers(data)

firstColumn = [line[0] for line in productionData]
secondColumn = [line[1] for line in productionData]

firstColumn.sort()
secondColumn.sort()

def findMultiplicator(num: int, col2: list[str]) -> int:
    return num * col2.count(str(num))

func = np.vectorize(findMultiplicator, excluded=['col2'])

results = np.array(func(num=np.array(firstColumn).astype(int), col2=secondColumn)).sum()

print(results)