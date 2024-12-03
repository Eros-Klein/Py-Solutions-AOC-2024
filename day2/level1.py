import numpy as np

def rowIsValid(num : np.ndarray) -> int:
    if num[0] > num[1]:
        lastNumber = num[0] + 1
        for n in num:
            if n < lastNumber and lastNumber - n <= 3:
                lastNumber = n
            else:
                return 0
    else:
        lastNumber = num[0] - 1
        for n in num:
            if n > lastNumber and n - lastNumber <= 3:
                lastNumber = n
            else:
                return 0

    return 1

data = open('src/big_input').read().splitlines()

productionData = [d.split() for d in data]

print(np.array([rowIsValid(np.array([int(n) for n in row])) for row in productionData]).sum())