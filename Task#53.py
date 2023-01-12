# Вычислить число c заданной точностью d
'''
Пример:
- при d = 0.001, π = 3.141    10^{-1} ≤ d ≤10^{-10}
'''


import math


num = float(input("Введите точность числа в диапазоне [0.1, 1e-10] >>> "))

s = str(num)
if '.' not in s:
    d = abs(int(s[s.index('1e') + 2 :]))
else:
    d = len(s[s.index('.') + 1:])


res = format(math.pi, f'.{d}f')
print(res)
