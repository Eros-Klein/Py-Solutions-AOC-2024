import numpy as np
import regex as re

data = open('src/big_input').read()

match = re.findall(r"(mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))", data)

isAccepted = True

result = 0

for n in match:
    if n == "do()":
        isAccepted = True
    elif n == "don't()":
        isAccepted = False
    elif isAccepted:
        vals = np.array(re.findall(r"\d{1,3}", n)).astype(int)
        if isAccepted:
            result += np.prod(vals)
    
print(result)