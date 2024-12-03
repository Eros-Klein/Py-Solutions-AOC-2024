import numpy as np
import regex as re

data = open('src/big_input').read()

match = re.findall(r"(mul\(\d{1,3},\d{1,3}\))", data)

matchnums = [re.findall(r"\d{1,3}", x) for x in match]

nums = np.array(matchnums).astype(int)

prods = [np.prod(x) for x in nums]

print(sum(prods))