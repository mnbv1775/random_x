from random_yangyuchen.word import *
from random_yangyuchen.name import *
from random_yangyuchen.date import *
from random_yangyuchen.common import *

def random_yangyuchen(text=''):
    text = text_common_random(text)
    text = text_word_random(text)
    text = text_name_random(text)
    text = text_date_random(text)
    text = text.strip()
    return text

if __name__ == '__main__':
    print(random_yangyuchen('{n}{Z}{rz}{word_nike}'))