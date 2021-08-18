with open('word_decode.txt', 'r', encoding='utf-8') as f:
    pool = f.readlines()

for i in pool:
    if '-' in i:
        print(i.split('\t')[0].strip().replace('-', ''))
    else:
        print(i.split('\t')[0].strip())