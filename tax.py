# -*- coding: utf-8 -*-

def tax(age, money, el):
    res=0
    el=True
    if age >= 16 and age <=65:
        if el == True:    
            if 20000 > money:
                res=money*0.3
            else:
                res=money*0.6
        elif el == False:
            if 20000 < money:
                res=money*0.2
            else:
                res=money*0.5
    else:
        res=money*0
    return int(res)
