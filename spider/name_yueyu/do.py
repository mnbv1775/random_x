with open('text.txt', 'r',  encoding='utf-8') as f:
    pool = f.readlines()

namelist = []

for i in pool:
    if i .split(',')[1].strip().lower() not in namelist:
        namelist.append(i .split(',')[1].strip().lower())


for i in namelist:
    print(i)