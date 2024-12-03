import numpy as np

def rowIsValidRe(num: np.ndarray):
    if rowIsValid(num) == 1:
        return 1
    for i in range(len(num)):
        num1 = np.delete(num, i)
        if rowIsValid(num1) == 1:
            return 1
    return 0
        
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

data = open('src/mo_input').read().splitlines()

productionData = [d.split() for d in data]

print(np.array([rowIsValidRe(np.array([int(n) for n in row])) for row in productionData]).sum())