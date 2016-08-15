#coding: utf-8

import math


def mean(lst_values):
  if len(lst_values) == 0:
      raise EOFError
  return sum(lst_values, 0.0) / len(lst_values)


def standard_deviation(lst_values, option):
  if len(lst_values) < 2:
    raise EOFError

  sd = 0.0
  sum_ = 0.0
  mean_value = mean(lst_values)

  for i in range(0, len(lst_values)):
    diff = lst_values[i] - mean_value
    sum_ += diff * diff

  sd = math.sqrt(sum_ / (len(lst_values) - option))
  return sd

import random


if __name__ == '__main__':
  s_1 = 0
  s_2 = 0
  s_3 = 0
  for idx, x in enumerate([random.choice([1,2,3]) for x in range(0, 50)]):
    print('idx %d: %d, ' % (idx, x), end='')
    if x == 1:
      s_1 += 1
    elif x == 2:
      s_2 += 1
    elif x == 3:
      s_3 += 1
    else:
      raise IOError
  print()
  print(standard_deviation([s_1, s_2, s_3], 0))

