import numpy as np
import copy as cp

class PageOrderRule:
    first: int
    second: int

    def __init__(self, first: int, second: int):
        self.first = first
        self.second = second

    def __str__(self):
        return f'{self.first} -> {self.second}'

data = [x.splitlines() for x in open('src/big_input').read().split('\n\n')]

pageOrder = data[1]

pageData = [x.split(',') for x in pageOrder]

pageOrderRule = data[0]

orderRules = [PageOrderRule(int(x.split('|')[0]), int(x.split('|')[1])) for x in pageOrderRule]

resultingOrders = cp.deepcopy(pageData)

for page in pageData:
    for rule in orderRules:
        firstVals = []
        secondVals = []
        for i in range(len(page)):
            if rule.first == int(page[i]):
                firstVals.append(i)
            elif rule.second == int(page[i]):
                secondVals.append(i)
        
        if(len(firstVals) > 0 and len(secondVals) > 0):
            success = False
            for first in firstVals:
                for second in secondVals:
                    if first < second:
                        success = True

            if success == False:
                resultingOrders.remove(page)
                break


print(resultingOrders)

def getMiddleVal(arr: list):
    return int(arr[len(arr) // 2])

result = np.array([getMiddleVal(x) for x in resultingOrders]).sum()

print(result)