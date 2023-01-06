# Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
'''
10
-> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
-> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]
'''

from copy import deepcopy
from random import randint

lst = [i for i in range(0, 10)]
print(lst)


def shuffle(lst):
  dc_lst = deepcopy(lst)
  x = len(dc_lst)
  while x:
    x -= 1
    i = randint(0, x)
    dc_lst[x], dc_lst[i] = dc_lst[i], dc_lst[x]
  return dc_lst


print(shuffle(lst))