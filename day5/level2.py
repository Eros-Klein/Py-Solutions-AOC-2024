import numpy as np

class PageOrderRule:
    first: int
    second: int

    def __init__(self, first: int, second: int):
        self.first = first
        self.second = second

def allRulesApply(page: list):
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
                return False
    return True

def correctErrors(page: list):
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
                page.insert(firstVals[0], page.pop(secondVals[0]))
                return page
    

def getMiddleVal(arr: list):
    return int(arr[len(arr) // 2])


data = [x.splitlines() for x in open('src/big_input').read().split('\n\n')]

pageData = [x.split(',') for x in data[1]]

orderRules = [PageOrderRule(int(x.split('|')[0]), int(x.split('|')[1])) for x in data[0]]

resultingOrders = []

for page in pageData:
    store = False
    while not allRulesApply(page):
        page = correctErrors(page)
        store = True

    if store:
        resultingOrders.append(page)

result = np.array([getMiddleVal(x) for x in resultingOrders]).sum()

print(result)