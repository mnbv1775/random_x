import random
def text_date_random(text=''):
    while '{date_mmdd}' in text:
        mm = random.randint(1, 12)
        dd = random.randint(1, 30)
        if mm < 10:
            mm_t = '0' + str(mm)
        else:
            mm_t = str(mm)
        if dd < 10:
            dd_t = '0' + str(dd)
        else:
            dd_t = str(dd)
        random_text = mm_t + dd_t
        text = text.replace('{date_mmdd}', random_text, 1)
    while '{date_yymmdd}' in text:
        yyyy = random.randint(1980, 2001)
        yy = str(yyyy)[:-2]
        mm = random.randint(1, 12)
        dd = random.randint(1, 30)
        if mm < 10:
            mm_t = '0' + str(mm)
        else:
            mm_t = str(mm)
        if dd < 10:
            dd_t = '0' + str(dd)
        else:
            dd_t = str(dd)
        random_text = yy + mm_t + dd_t
        text = text.replace('{date_yymmdd}', random_text, 1)
    while '{date_yyyymmdd}' in text:
        yyyy = random.randint(1980, 2001)
        mm = random.randint(1, 12)
        dd = random.randint(1, 30)
        if mm < 10:
            mm_t = '0' + str(mm)
        else:
            mm_t = str(mm)
        if dd < 10:
            dd_t = '0' + str(dd)
        else:
            dd_t = str(dd)
        random_text = str(yyyy) + mm_t + dd_t
        text = text.replace('{date_yyyymmdd}', random_text, 1)
    return text
if __name__ == '__main__':
    print(text_date_random('{date_mmdd}'))
    print(text_date_random('{date_yymmdd}'))
    print(text_date_random('{date_yyyymmdd}'))