# -*- coding: utf-8 -*-

def isyear(num):
    res=''
    if(((num % 400) == 0) or ((num % 4) == 0) and ((num % 100) != 0)):
        res='윤년'
    else:
        res='평년'
    return res


