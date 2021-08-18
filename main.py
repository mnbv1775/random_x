from random_x.word import *
from random_x.name import *
from random_x.date import *
from random_x.common import *

def random_x(text=''):
    text = text_common_random(text)
    text = text_word_random(text)
    text = text_name_random(text)
    text = text_date_random(text)
    text = text.strip()
    return text

if __name__ == '__main__':
    print(random_x('{n}{Z}{rz}{word_nike}'))