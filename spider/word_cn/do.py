with open('text.txt', 'r', encoding='utf-8') as f:
    pool = f.readlines()

for i in pool:
    print(i.split('\t')[0])