from random_x.data.word_cn import *
from random_x.data.word_en import *
from random_x.data.word_nike_en import *
import random
from pypinyin import lazy_pinyin

def text_word_random(text=''):
    while '{word_en}' in text:
        randomList = WORD_EN.split('\n')
        randomText = randomList[random.randint(0, len(randomList) - 1)]
        text = text.replace('{word_en}', randomText, 1)
    while '{word_en_title}' in text:
        randomList = WORD_EN.split('\n')
        randomText = randomList[random.randint(0, len(randomList) - 1)].title()
        text = text.replace('{word_en_title}', randomText, 1)
    while '{word_cn}' in text:
        randomList = WORD_CN.split('\n')
        randomText = randomList[random.randint(0, len(randomList)-1)]
        text = text.replace('{word_cn}', randomText, 1)
    while '{word_pingyin}' in text:
        randomList = WORD_CN.split('\n')
        randomPinyinList = lazy_pinyin(randomList[random.randint(0, len(randomList) - 1)])
        randomText=''.join(randomPinyinList).replace(' ', '')
        text = text.replace('{word_pingyin}', randomText, 1)
    while '{word_pingyin_title}' in text:
        randomList = WORD_CN.split('\n')
        randomPinyinList = lazy_pinyin(randomList[random.randint(0, len(randomList) - 1)])
        randomText = ''.join(randomPinyinList).replace(' ', '').title()
        text = text.replace('{word_pingyin_title}', randomText, 1)
    while '{word_nike}' in text:
        randomList = WORD_NIKE_EN.split('\n')
        randomText = randomList[random.randint(0, len(randomList)-1)]
        text = text.replace('{word_nike}', randomText, 1)
    return text


if __name__ == '__main__':
    print(text_word_random('{word_cn}'))
    print(text_word_random('{word_en}'))
    print(text_word_random('{word_en_title}'))
    print(text_word_random('{word_pingyin}'))
    print(text_word_random('{word_pingyin_title}'))
    print(text_word_random('{word_nike}'))