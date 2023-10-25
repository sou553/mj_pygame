from decimal import Decimal

def print_tehai(tehai, turn):
    #print(tehai)
    print()
    t = turn[0]
    if t%4 == 0:
        print("東")
    if t%4 == 1:
        print("南")
    if t%4 == 2:
        print("西")
    if t%4 == 3:
        print("北")

    tehai_m = []
    tehai_n = []
    
    for i in tehai[0]:
        h = hai_name(i)
        tehai_m.append(h)
    if tehai[1][0] != 0:
        for i in tehai[1]:
            h = hai_name(i)
            tehai_n.append(h)

    tehai_s = [tehai_m, tehai_n]


    print("".join(map(str,tehai_s)))
    tehai[0].sort()#自摸後に並び替え
    tehai[1].sort()


def hai_num(s):#str to int
    if len(s) == 1:
        if s == "東":
            i = 28.0
        elif s == "南":
            i = 29.0
        elif s == "西":
            i = 30.0
        elif s == "北":
            i = 31.0
        elif s == "白":
            i = 32.0
        elif s == "発":
            i = 33.0
        elif s == "中":
            i = 34.0
    else:
        if s[1] == "m":
            i = float(s[0] + ".0")
        if s[1] == "p":
            i = float(str((int(s[0]) + 9)) + ".0")
        if s[1] == "s":
            i = float(str((int(s[0]) + 18)) + ".0")

    return i


def hai_name(hai_i):#int to str
    i = int(hai_i)
    i -= 1
    if int(i/9) == 0:#萬子
        hai = (str(i % 9 + 1) + "m")
    elif int(i/9) == 1:#筒子
        hai = (str(i % 9 + 1) + "p")
    elif int(i/9) == 2:#索子
        hai = (str(i % 9 + 1) + "s")
    elif int(i/9) == 3:#字牌
        i = i % 9 + 1
        if i == 1:
            hai = ("東")
        elif i == 2:
            hai = ("南")
        elif i == 3:
            hai = ("西")
        elif i == 4:
            hai = ("北")
        elif i == 5:
            hai = ("白")
        elif i == 6:
            hai = ("発")
        elif i == 7:
            hai = ("中")
    
    return hai


def hai_filename(hai_i):
    if hai_i >= 101:
        hai_i = float(Decimal(str(hai_i)) - Decimal("100"))
    muki = str(hai_i)[-1]
    i = int(hai_i)
    i -= 1
    if int(i/9) == 0:#萬子p_ms1_0.gif
        filename = ("files/manzu_all/p_ms" + str(i % 9 + 1) + "_" + str(muki) + ".gif")
    elif int(i/9) == 1:#筒子
        filename = ("files/pinzu_all/p_ps" + str(i % 9 + 1) + "_" + str(muki) + ".gif")
    elif int(i/9) == 2:#索子
        filename = ("files/sozu_all/p_ss" + str(i % 9 + 1) + "_" + str(muki) + ".gif")
    elif int(i/9) == 3:#字牌p_ji_c_0.gif
        i = i % 9 + 1
        if i == 1:
            filename = ("files/tupai_all/p_ji_e_" + str(muki) + ".gif")
        elif i == 2:
            filename = ("files/tupai_all/p_ji_s_" + str(muki) + ".gif")
        elif i == 3:
            filename = ("files/tupai_all/p_ji_w_" + str(muki) + ".gif")
        elif i == 4:
            filename = ("files/tupai_all/p_ji_n_" + str(muki) + ".gif")
        elif i == 5:
            filename = ("files/tupai_all/p_no_" + str(muki) + ".gif")
        elif i == 6:
            filename = ("files/tupai_all/p_ji_h_" + str(muki) + ".gif")
        elif i == 7:
            filename = ("files/tupai_all/p_ji_c_" + str(muki) + ".gif")
    elif int(hai_i) == 100:
        filename = ("files/ms_all/p_bk_" + str(muki) + ".gif")
    
    return filename