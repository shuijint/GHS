#-*-coding:utf-8-*-
import profile
from fractions import Fraction
import random


def count():
    n = random.randint(1,2)
    if n == 1:
        x = ['+','-','*','÷']
        i = random.randint(1,100)
        j = random.choice(x)
        k = random.randint(1,100)
        if j == '+':
            answer = i + k
            print(i, j, k, '=')
        elif j == '-':
            i1 = max(i,k)
            k1 = min(i,k)
            answer = i1 - k1
            print(i1, j, k1, '=')
        elif j == '*':
            answer = i * k
            print(i, j, k, '=')
        elif j == '÷':
            answer = i / k
            print(i, j, k, '=')
        print('答案为：'+str(answer))
    elif n == 2:
        y = ['+', '-', '*', '÷']
        a = random.randint(1,100)
        b = random.randint(1,100)
        c = random.randint(1,100)
        d = random.randint(1,100)
        a1 = min(a,b)
        b1 = max(a,b)
        c1 = min(c,d)
        d1 = max(c,d)
        z = random.choice(y)
        if z == '+':
            ans = Fraction(a1, b1) + Fraction(c1, d1)
            print('(', a1, '/', b1, ')', z, '(', c1, '/', d1, ')', '=')
        elif z == '-':
            big = max(Fraction(a1, b1),Fraction(c1, d1))
            small = min(Fraction(a1, b1),Fraction(c1, d1))
            ans = big - small
            print('(',big,')',z,'(',small,')')
        elif z == '*':
            ans = Fraction(a1, b1) * Fraction(c1, d1)
            print('(', a1, '/', b1, ')', z, '(', c1, '/', d1, ')', '=')
        elif z == '÷':
            ans = Fraction(a1, b1) / Fraction(c1, d1)
            print('(', a1, '/', b1, ')', z, '(', c1, '/', d1, ')', '=')
        print('答案为：' + str(ans))
profile.run('ghscount()')
