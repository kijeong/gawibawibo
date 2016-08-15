# coding: utf-8
# author: kijeong

from random import choice


def show_me_the_hand_bawi(records):
    return 'bawi'


def show_me_the_hand_gawi(records):
    return 'gawi'


def show_me_the_hand_bo(records):
    return 'bo'


def show_me_the_hand_last(records):
    if len(records):
        return choice(['gawi', 'bawi', 'bo'])
    return records[0][0]


def show_me_the_hand_rand(records):
    return choice(['gawi', 'bawi', 'bo'])


def show_me_the_hand(records):
    return show_me_the_hand_rand(records)
