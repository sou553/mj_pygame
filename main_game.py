# coding: utf-8
import copy
import random
import create as crt
import oneround as rnd
import calculation as cal
import pages 


def onegame_loop(all_points, p_kaze, p_kaze_s, bakaze, kyoutaku, tumibou):
    p_kaze_t = copy.deepcopy(p_kaze)
    yama = crt.make_yama()
    all_tehai = crt.idv_tehai(yama)  # all_tehai[[player1],[pl
    turn = []
    turn.append(0)
    all_kawa = [[], [], [], []]
    info_list = [yama, all_tehai, all_kawa, turn, p_kaze, bakaze, all_points, kyoutaku, tumibou, p_kaze_s]
    if pages.oneround_page(info_list) == p_kaze_t:
        tumibou[0] += 300
        onegame_loop(all_points, p_kaze, p_kaze_s, bakaze, kyoutaku, tumibou)
    else:
        tumibou[0] = 0
        return
    


def main_loop_hanchan():
    all_points = [[25000], [25000], [25000], [25000]]
    p_kaze_s = [0]#playerが何家スタートか
    p_kaze = copy.deepcopy(p_kaze_s)
    bakaze = [0]#東風 or 半荘　　
    kyoutaku = [0]
    tumibou = [0]

    while bakaze[0] < 2:
        onegame_loop(all_points, p_kaze, p_kaze_s, bakaze, kyoutaku, tumibou)
        print(p_kaze, bakaze)
        print()
        if p_kaze[0] == p_kaze_s[0]:
            bakaze[0] = bakaze[0] + 1



if __name__ == "__main__":
    main_loop_hanchan()

