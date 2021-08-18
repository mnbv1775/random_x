import random
z = 'abcdefjhijklmnopqrstuvwxyz'
Z = 'ABCDEFJHIJKLMNOPQRSTUVWXYZ'
rz = 'adbcdefjhijklmnopqrstuvwxyzABCDEFJHIJKLMNOPQRSTUVWXYZ'
def text_common_random(text=''):
    while '{n}' in text:
        text = text.replace('{n}', str(random.randint(0, 9)), 1)
    while '{z}' in text:
        text = text.replace('{z}', random.choice(z), 1)
    while '{Z}' in text:
        text = text.replace('{Z}', random.choice(Z), 1)
    while '{rz}' in text:
        text = text.replace('{rz}', random.choice(rz), 1)
    return text

if __name__ == '__main__':
    print(text_common_random('{n}'))
    print(text_common_random('{z}'))
    print(text_common_random('{Z}'))
    print(text_common_random('{rz}'))