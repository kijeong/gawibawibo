# coding:utf-8
# author: kijeong.kim<at>gmail.com

from players import player1
from players import player2


def fighting(cnt_round=10000):
    r1 = []
    r2 = []
    for i in range(cnt_round):
        h1 = player1.show_me_the_hand(r2)
        h2 = player2.show_me_the_hand(r1)
        if h1 == h2:
            # print('match %d of 1000: tie' % i)
            r = 0
        elif (h1 == 'gawi' and h2 == 'bo') or (h1 == 'bawi' and h2 == 'gawi') or (h1 == 'bo' and h2 == 'bawi'):
            # print('match %d of 1000: p1 win' % i)
            r = 1
        else:
            # print('match %d of 1000: p2 win' % i)
            r = -1
        r1.append((h1, r))
        r2.append((h2, -r))

    sum_player1 = 0
    sum_player2 = 0
    for result in r1:
        if result[1] == 1:
            sum_player1 += 3
        elif result[1] == 0:
            sum_player1 += 1
            sum_player2 += 1
        elif result[1] == -1:
            sum_player2 += 3
        else:
            raise IOError
    return sum_player1, sum_player2


def main():
    cnt_game = 100
    cnt_round = 1000
    sum_win_p1 = 0
    sum_win_p2 = 0
    sum_tie = 0
    for i in range(cnt_game):
        score_p1, score_p2 = fighting(cnt_round)
        if score_p1 < score_p2:
            sum_win_p2 += 1
        elif score_p2 < score_p1:
            sum_win_p1 += 1
        else:
            sum_tie += 1
            print("match its not common")
        print("player1: %d score, player2: %d score [win: %s]" %
              (score_p1, score_p2, "player1" if score_p2 < score_p1 else "player2"))
    print("s1 %d: s2: %d" % (sum_win_p1, sum_win_p2))


if __name__ == '__main__':
    main()

