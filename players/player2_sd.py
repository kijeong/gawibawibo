# coding: utf-8
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


dic_hands_indexed = {'gawi':0, 'bawi':1, 'bo':2}
lst_hands = ['gawi', 'bawi', 'bo']


def get_sd(counter_records):
    sum_gawi = 0
    sum_bawi = 0
    sum_bo = 0
    sum_win = 0
    sum_tie = 0
    sum_lose = 0
    for hand, result in counter_records:
        if hand == 'gawi':
            sum_gawi += 1
        elif hand == 'bawi':
            sum_bawi += 1
        elif hand == 'bo':
            sum_bo += 1
        else:
            return hand

        if result == 0:
            sum_tie += 1
        elif result == 1:
            sum_lose += 1
        elif result == -1:
            sum_win += 1
        else:
            return hand
    sd_hands_ = standard_deviation([sum_gawi, sum_bawi, sum_bo], 0)
    sd_result = standard_deviation([sum_tie, sum_lose, sum_win], 0)
    return sd_hands_, sd_result


def get_better_hand_rand(lst_counter_records):
    from collections import Counter
    count = Counter([x[0] for x in lst_counter_records])
    mc = sorted(count, key=lambda x: count[x])
    if mc.count(lst_hands[0]) == 0:
        idx = 0
    elif mc.count(lst_hands[1]) == 0:
        idx = 1
    elif mc.count(lst_hands[2]) == 0:
        idx = 2
    else:
        idx = dic_hands_indexed[mc[0]]
    return lst_hands[(idx + 1) % 3]


sd_hands = 0
better_hand = lst_hands[0]


def get_better_hand_same(result_last):
    if result_last == -1:
        return better_hand
    elif result_last == 0:
        return lst_hands[(dic_hands_indexed[better_hand] + 1) % 3]
    elif result_last == 1:
        return lst_hands[(dic_hands_indexed[better_hand] + 2) % 3]
    else:
        return lst_hands[0]


def show_me_the_hand(records):
    counter_records = records
    if len(counter_records) < 50:
        return lst_hands[0]

    global sd_hands
    global better_hand

    if len(counter_records) % 50 == 0: # 50-20
        sd_hands, sd_result = get_sd(counter_records[-50:])
        better_hand = get_better_hand_same(counter_records[-1][1])

    if 20 < sd_hands:
        return better_hand
    else:
        return get_better_hand_rand(counter_records[-2:])


