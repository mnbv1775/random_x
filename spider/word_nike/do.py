from lxml import etree
import re
def containsChineseText(text=''):
    zhPattern = re.compile(u'[\u4e00-\u9fa5]+')
    match = zhPattern.search(text)

    if match:
        return True
    else:
        return False
def containsChineseFtText(text=''):
    zhPattern = re.compile(u'[\u4E00-\u9FA5]+')
    match = zhPattern.search(text)

    if match:
        return True
    else:
        return False
def containsEnText(text=''):
    zhPattern = re.compile(u'[a-z]')
    match = zhPattern.search(text)

    if match:
        return True
    else:
        return False
if __name__ == '__main__':
    with open('product-list.html', 'r', encoding='utf-8') as f:
        HTML = etree.HTML(f.read())

    outList = []
    for i in HTML.xpath('//span/text()'):
        if i.strip() == '':
            continue
        if containsChineseText(i.strip()) == True:
            continue
        if containsChineseFtText(i.strip()) == True:
            continue
        if containsEnText(i.strip()) == True:
            outList.append(i.strip())

    wordList = []
    for i in outList:
        for x in i.split(' '):
            x = x.lower()
            if x not in wordList:
                wordList.append(x)

    for i in wordList:
        if containsEnText(i.strip()) == True:
            print(i)