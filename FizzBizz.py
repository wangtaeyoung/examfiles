# -*- coding: utf-8 -*-

def fizzbizz(num):
    if num % 3 == 0 and num != 0:
        return 'Fizz'
    elif num % 5 ==0 and num != 0:
        return 'Bizz'
    else:
        return 'ValueError'
    
