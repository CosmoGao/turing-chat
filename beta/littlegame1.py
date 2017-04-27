# ! /usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import unicode_literals

try:
    input = raw_input
except:
    pass


def fight(a, b):
    _vs = 'A:%s\nB:%s\n' % (a, b)
    if a > b:
        print(_vs + 'A Win!')
        return 1
    elif a < b:
        print(_vs + 'B Win!')
        return -1
    else:
        print(_vs + 'Draw!')
        return 0


def main():
    print('请定义游戏回合数：')
    n = int(input())
    a = []
    b = []
    for ns in range(n):
        a.append(str(ns + 1))
        b.append(str(ns + 1))
    score = 0
    i = 1
    while i <= n:
        print('第%s回合' % i)
        p1T = True
        print('请玩家1输入数字：')
        while p1T:
            p1 = input()
            try:
                a.pop(a.index(p1))
                p1T = False
            except:
                print('输入有误，请玩家1重新输入：')
                print(a)
        p2T = True
        print('请玩家2输入数字：')
        while p2T:
            p2 = input()
            try:
                b.pop(b.index(p2))
                p2T = False
            except:
                print('输入有误，请玩家2重新输入：')
                print(b)
        score = score + fight(int(p1), int(p2))
        i += 1
    if score > 0:
        print('玩家1胜出！')
    elif score < 0:
        print('玩家2胜出！')
    else:
        print('平局！')
    input()


if __name__ == '__main__':
    main()
