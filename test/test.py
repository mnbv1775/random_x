import random
from main import *
with open('textPool.txt', 'r') as f:
    pool = f.readlines()
#for i in pool:
    #print(random_yangyuchen(i))
for i in range(100):
    print(random_yangyuchen(random.choice(pool)))