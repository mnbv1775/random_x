# random_x 随机库

你可以使用以下的规则来替换文本
You can use the following rules to replace text

## How to use? 如何使用
```python
import random_x
random_x.random_x("{n}") #Print 0-9 random e.g: 5
random_x.random_x("{n}") #Print 0-9 random e.g: 3
random_x.random_x("{n}") #Print 0-9 random e.g: 7
random_x.random_x("{n}") #Print 0-9 random e.g: 2
```

## common 普通
### {n}
    随机数字 0-9
    Random numbers 0-9
### {z}
    随机小写字母 a-z
    Random lowercase letters a-z
### {Z}
    随机大写字母 A-Z
    Random Capital letter Amurz
### {rz}
    随机大小写字母 a-Z
    Random uppercase and lowercase letters aMuz

## name 姓名

### {name_firstname_yueyu}
    随机粤语名 (一个或两个单词)
### {name_firstname_yueyu_title}
    随机粤语名 首字母大写 (一个或两个单词)
### {name_lastname_yueyu}
    随机粤语名 (单个字符)
### {name_lastname_yueyu_title}
    随机粤语名 首字母大写 (单个字符)
### {name_firstname_en}
    随机英文名
### {name_firstname_en_title}
    随机英文名 首字母大写
### {name_lastname_en}
    随机英文姓
### {name_lastname_en_title}
    随机英文姓 首字母大写
### {name_firstname_pinyin}
    随机中文拼音名 
### {name_firstname_pinyin_title}
    随机中文拼音名 首字母大写
### {name_lastname_pinyin}
    随机中文拼音姓 首字母大写
### {name_lastname_pinyin_title}
    随机中文拼音名
### {name_firstname_cn}
    随机中文名
### {name_lastname_cn}
    随机中文姓

## date 日期
### {date_mmdd}
    随机月份+日期 4位 0726
### {date_yymmdd}
    随机年份+月份+日期 6位 990726
### {date_yyyymmdd}
    随机年份+月分+日期 8位 19990726

## word 词语
### {word_en}
    随机英文单词
### {word_en_title}
    随机英文单词 首字母大写
### {word_pingyin}
    随机词语拼音
### {word_pingyin_title}
    随机词语拼音 首字母大写
### {word_cn}
    随机中文词语
### {word_nike}
    随机和nike有关的词语
