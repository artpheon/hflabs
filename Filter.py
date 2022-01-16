# coding=utf-8
import re


class Filter(object):
    def __init__(self):
        pass

    def filter(self, string):
        # result = re.findall(r'(\d+\s[А-Я]+)\s\d+\s([А-Я]+.*)', string)
        result = re.findall(r'(\d+\s[А-Я]+)[\d+\s]+([А-Я]+.*)', string)
        return None if not result else result[0][0] + ' ' + result[0][1]


if __name__ == '__main__':
    f = Filter()
    # res1 = f.filter('140002 ЛЮБЕРЦЫ  ОКТЯБРЬСКИЙ ПР 123/4-115')
    # res2 = f.filter('140002 ЛЮБЕРЦЫ 2 ОКТЯБРЬСКИЙ ПР 123/4-115')
    # res3 = f.filter('140002 ЛЮБЕРЦЫ 97 ОКТЯБРЬСКИЙ ПР 123/4-115')
    # res4 = f.filter('140002 ЛЮБЕРЦЫ 0 ОКТЯБРЬСКИЙ ПР 123/4-115')
    # res5 = f.filter('140002 ЛЮБЕРЦЫ ОКТЯБРЬСКИЙ ПР 123/4-115')
