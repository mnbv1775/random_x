import random
from random_yangyuchen.data.name_cn import *
from random_yangyuchen.data.name_en import *
from random_yangyuchen.data.name_yueyu import *
from pypinyin import lazy_pinyin
def text_name_random(text=''):
    while '{name_firstname_yueyu}' in text:
        randomList = NAME_YUEYU.split('\n')
        if random.randint(1, 2) == 2:
            randomText = random.choice(randomList) + random.choice(randomList)
        else:
            randomText = random.choice(randomList)
        text = text.replace('{name_firstname_yueyu}', randomText, 1)
    while '{name_firstname_yueyu_title}' in text:
        randomList = NAME_YUEYU.split('\n')
        if random.randint(1, 2) == 2:
            randomText = random.choice(randomList).title() + random.choice(randomList)
        else:
            randomText = random.choice(randomList).title()
        text = text.replace('{name_firstname_yueyu_title}', randomText, 1)
    while '{name_lastname_yueyu}' in text:
        randomList = NAME_YUEYU.split('\n')
        randomText = random.choice(randomList)
        text = text.replace('{name_lastname_yueyu}', randomText, 1)
    while '{name_lastname_yueyu_title}' in text:
        randomList = NAME_YUEYU.split('\n')
        randomText = random.choice(randomList).title()
        text = text.replace('{name_lastname_yueyu_title}', randomText, 1)
    while '{name_firstname_en}' in text:
        if random.randint(1, 2) == 2:
            randomText = random.choice(NAME_EN_LIST) + random.choice(NAME_EN_LIST)
        else:
            randomText = random.choice(NAME_EN_LIST)
        text = text.replace('{name_firstname_en}', randomText, 1)
    while '{name_firstname_en_title}' in text:
        if random.randint(1, 2) == 2:
            randomText = random.choice(NAME_EN_LIST).title() + random.choice(NAME_EN_LIST)
        else:
            randomText = random.choice(NAME_EN_LIST).title()
        text = text.replace('{name_firstname_en_title}', randomText, 1)
    while '{name_lastname_en}' in text:
        randomText = random.choice(NAME_EN_LIST)
        text = text.replace('{name_lastname_en}', randomText, 1)
    while '{name_lastname_en_title}' in text:
        randomText = random.choice(NAME_EN_LIST).title()
        text = text.replace('{name_lastname_en_title}', randomText, 1)
    while '{name_firstname_pinyin}' in text:
        if random.randint(1, 2) == 2:
            randomText = random.choice(NAME_FIRSTNAME_CN_LIST)
        else:
            randomText = random.choice(NAME_FIRSTNAME_CN_LIST) + random.choice(NAME_FIRSTNAME_CN_LIST)
        randomPinyinList = lazy_pinyin(randomText)
        randomText = ''.join(randomPinyinList).replace(' ', '').title()
        text = text.replace('{name_firstname_pinyin}', randomText, 1)
    while '{name_firstname_pinyin_title}' in text:
        if random.randint(1, 2) == 2:
            randomText = random.choice(NAME_FIRSTNAME_CN_LIST)
        else:
            randomText = random.choice(NAME_FIRSTNAME_CN_LIST) + random.choice(NAME_FIRSTNAME_CN_LIST)
        randomPinyinList = lazy_pinyin(randomText)
        randomText = ''.join(randomPinyinList).replace(' ', '').title()
        text = text.replace('{name_firstname_pinyin_title}', randomText.title(), 1)
    while '{name_lastname_pinyin}' in text:
        randomText = random.choice(NAME_LASTNAME_CN_LIST)
        randomPinyinList = lazy_pinyin(randomText)
        randomText = ''.join(randomPinyinList).replace(' ', '').title()
        text = text.replace('{name_lastname_pinyin}', randomText, 1)
    while '{name_lastname_pinyin_title}' in text:
        randomText = random.choice(NAME_LASTNAME_CN_LIST)
        randomPinyinList = lazy_pinyin(randomText)
        randomText = ''.join(randomPinyinList).replace(' ', '').title()
        text = text.replace('{name_lastname_pinyin_title}', randomText.title(), 1)
    while '{name_firstname_cn}' in text:
        if random.randint(1, 2) == 2:
            randomText = random.choice(NAME_FIRSTNAME_CN_LIST) + random.choice(NAME_FIRSTNAME_CN_LIST)
        else:
            randomText = random.choice(NAME_FIRSTNAME_CN_LIST)
        text = text.replace('{name_firstname_cn}', randomText, 1)
    while '{name_lastname_cn}' in text:
        randomText = random.choice(NAME_LASTNAME_CN_LIST)
        text = text.replace('{name_lastname_cn}', randomText, 1)
    return text
if __name__ == '__main__':
    print(text_name_random('{name_firstname_yueyu}'))
    print(text_name_random('{name_firstname_yueyu_title}'))
    print(text_name_random('{name_lastname_yueyu}'))
    print(text_name_random('{name_lastname_yueyu_title}'))
    print(text_name_random('{name_firstname_en}'))
    print(text_name_random('{name_firstname_en_title}'))
    print(text_name_random('{name_lastname_en}'))
    print(text_name_random('{name_lastname_en_title}'))
    print(text_name_random('{name_firstname_pinyin}'))
    print(text_name_random('{name_firstname_pinyin_title}'))
    print(text_name_random('{name_firstname_cn}'))
    print(text_name_random('{name_lastname_cn}'))