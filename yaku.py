import copy
import yaku_sub as sub
import judge as jdg


def yaku_check(p_tehai, Flags, dora, ura_dora, p_kaze, bakaze):  # return list[[][][][]] 役の翻数ごとに
    yaku_list = [[], [], [], [], [], [], [], []]  # 1, 2, 3, 5, 6, 13, ドラ, dora
    TurnFlag = Flags[0]
    FirstTurn = Flags[1]
    Reach = Flags[2]
    Menzen = Flags[3]
    Haitei = Flags[4]
    Rinsyan = Flags[5]
    Chankan = Flags[6]
    tehai = [[], []]  # 手牌の小数点を捨てる
    tehai_t = copy.deepcopy(p_tehai)
    for hai in tehai_t[0]:
        tehai[0].append(int(hai))
    if tehai_t[1] != [0]:
        while len(tehai_t[1]) > 0:
            if tehai_t[1][0] >= 100:
                tehai[1].append(int(tehai_t[1][0]))
                tehai_t[1].pop(0)
            else:
                tehai_sub = []
                tehai_sub.append(tehai_t[1][0])
                tehai_sub.append(tehai_t[1][1])
                tehai_sub.append(tehai_t[1][2])
                tehai_sub.sort()
                for hai in tehai_sub:
                    tehai[1].append(int(hai))
                for _ in range(3):
                    tehai_t[1].pop(0)
    #print(tehai)
    
    #ドラ
    dora_n = 0
    ura_dora_n = 0
    for hai in dora:
        if hai == 9 or hai == 18 or hai == 27:
            dora_hai = hai-8
        elif hai == 31:
            dora_hai = 28
        elif hai == 34:
            dora_hai = 32
        else:
            dora_hai = hai+1
        dora_n += (tehai[0].count(dora_hai) + tehai[1].count(dora_hai))
    yaku_list[6].append("ドラ " + str(dora_n) + "翻")
    yaku_list[7].append(dora_n)
    if Reach != False:
        for hai in ura_dora:
            if hai == 9 or hai == 18 or hai == 27:
                dora_hai = hai-8
            elif hai == 31:
                dora_hai = 28
            elif hai == 34:
                dora_hai = 32
            else:
                dora_hai = hai+1
            ura_dora_n += (tehai[0].count(dora_hai) + tehai[1].count(dora_hai))
        yaku_list[6].append("裏ドラ " + str(ura_dora_n) + "翻")
        yaku_list[7].append(ura_dora_n)
    # 1翻役
    reach(Reach, yaku_list)
    ippatu(Reach, yaku_list)
    menzentumo(Menzen, TurnFlag, yaku_list)
    zikaze_ton(tehai, p_kaze, yaku_list)
    zikaze_nan(tehai, p_kaze, yaku_list)
    zikaze_sya(tehai, p_kaze, yaku_list)
    zikaze_pe(tehai, p_kaze, yaku_list)
    bakaze_ton(tehai, p_kaze, yaku_list)
    bakaze_nan(tehai, p_kaze, yaku_list)
    bakaze_sya(tehai, p_kaze, yaku_list)
    bakaze_pe(tehai, p_kaze, yaku_list)
    sangen_haku(tehai, yaku_list)
    sangen_hatu(tehai, yaku_list)
    sangen_chun(tehai, yaku_list)
    tanyao(tehai, yaku_list)
    pinfu(tehai, p_kaze, bakaze, yaku_list)
    ipeko(tehai, Menzen, yaku_list)
    haitei(TurnFlag, Haitei, yaku_list)
    houtei(TurnFlag, Haitei, yaku_list)
    rinsyankaihou(Rinsyan, yaku_list)
    chankan(Chankan, yaku_list)
    # 2翻役
    doubreach(FirstTurn, Reach, yaku_list)
    sansyoku_123(tehai, Menzen, yaku_list)
    sansyoku_111(tehai, yaku_list)
    sanankou(tehai, TurnFlag, Menzen, yaku_list)
    sankantu(tehai, yaku_list)
    ittuu(tehai, Menzen, yaku_list)
    chitoitu(tehai, yaku_list)
    toitoi(tehai, Menzen, yaku_list)
    chanta(tehai, Menzen, yaku_list)
    syousangen(tehai, yaku_list)
    honroutou(tehai, yaku_list)
    # 3翻役
    ryanpeko(tehai, yaku_list)
    junchan(tehai, Menzen, yaku_list)
    honitu(tehai, Menzen, yaku_list)
    # 6翻役
    #chinitu(tehai, Menzen, yaku_list) ホンイツでまとめてやってまう
    # 役満
    tenhou(FirstTurn, Reach, p_kaze, yaku_list)
    tihou(FirstTurn, Reach, p_kaze, yaku_list)
    suankou(tehai, TurnFlag, Menzen, yaku_list)
    daisangen(tehai, yaku_list)
    kokusi(tehai, yaku_list)
    ryuiso(tehai, yaku_list)
    tuiso(tehai, yaku_list)
    chinroutou(tehai, yaku_list)
    syoususi(tehai, yaku_list)
    daisusi(tehai, yaku_list)
    churen(tehai, yaku_list)
    sukantu(tehai, yaku_list)

    if "一盃口" in yaku_list[0] and "三暗刻" in yaku_list[1]:
        yaku_list[0].remove("一盃口")
    if "一盃口" in yaku_list[0] and "二盃口" in yaku_list[2]:
        yaku_list[0].remove("一盃口")
    if "平和" in yaku_list[0] and "三暗刻" in yaku_list[1]:
        yaku_list[0].remove("平和")
    return yaku_list
        


# 1翻役
def reach(Reach, yaku_list):  # 立直
    if Reach == True or Reach == "FirstTurn":
        yaku_list[0].append("立直")


def ippatu(Reach, yaku_list):  # 一発
    if Reach == "FirstTurn":
        yaku_list[0].append("一発")


def menzentumo(Menzen, Agari, yaku_list):  # 門前清自摸
    if Menzen == True and Agari == "Tumo":
         yaku_list[0].append("門前清自摸")


def zikaze_ton(tehai, p_kaze, yaku_list):  # 東自風
    tehai_m = tehai[0]
    tehai_n = tehai[1]
    hai = 28
    if (tehai_m.count(hai) == 3 or tehai_n.count(hai) == 3 or tehai_n.count(hai) == 4) and p_kaze[0] == 0:
        yaku_list[0].append("自風:東")


def zikaze_nan(tehai, p_kaze, yaku_list):  # 南自風
    tehai_m = tehai[0]
    tehai_n = tehai[1]
    hai = 29
    if (tehai_m.count(hai) == 3 or tehai_n.count(hai) == 3 or tehai_n.count(hai) == 4) and p_kaze[0] == 1:
        yaku_list[0].append("自風:南")


def zikaze_sya(tehai, p_kaze, yaku_list):  # 西自風
    tehai_m = tehai[0]
    tehai_n = tehai[1]
    hai = 30
    if (tehai_m.count(hai) == 3 or tehai_n.count(hai) == 3 or tehai_n.count(hai) == 4) and p_kaze[0] == 2:
        yaku_list[0].append("自風:西")


def zikaze_pe(tehai, p_kaze, yaku_list):  # 北自風
    tehai_m = tehai[0]
    tehai_n = tehai[1]
    hai = 31
    if (tehai_m.count(hai) == 3 or tehai_n.count(hai) == 3 or tehai_n.count(hai) == 4) and p_kaze[0] == 3:
        yaku_list[0].append("自風:北")


def bakaze_ton(tehai, bakaze, yaku_list):  # 東場風
    tehai_m = tehai[0]
    tehai_n = tehai[1]
    hai = 28
    if (tehai_m.count(hai) == 3 or tehai_n.count(hai) == 3 or tehai_n.count(hai) == 4) and bakaze[0] == 0:
        yaku_list[0].append("場風:東")


def bakaze_nan(tehai, bakaze, yaku_list):  # 南場風
    tehai_m = tehai[0]
    tehai_n = tehai[1]
    hai = 29
    if (tehai_m.count(hai) == 3 or tehai_n.count(hai) == 3 or tehai_n.count(hai) == 4) and bakaze[0] == 1:
        yaku_list[0].append("場風:南")


def bakaze_sya(tehai, bakaze, yaku_list):  # 西場風
    tehai_m = tehai[0]
    tehai_n = tehai[1]
    hai = 30
    if (tehai_m.count(hai) == 3 or tehai_n.count(hai) == 3 or tehai_n.count(hai) == 4) and bakaze[0] == 2:
        yaku_list[0].append("場風:西")


def bakaze_pe(tehai, bakaze, yaku_list):  # 北場風
    tehai_m = tehai[0]
    tehai_n = tehai[1]
    hai = 31
    if (tehai_m.count(hai) == 3 or tehai_n.count(hai) == 3 or tehai_n.count(hai) == 4) and bakaze[0] == 3:
        yaku_list[0].append("場風:北")


def sangen_haku(tehai, yaku_list):  # 白
    tehai_m = tehai[0]
    tehai_n = tehai[1]
    hai = 32
    if tehai_m.count(hai) == 3 or tehai_n.count(hai) == 3 or tehai_n.count(hai) == 4:
        yaku_list[0].append("役牌:白")


def sangen_hatu(tehai, yaku_list):  # 発
    tehai_m = tehai[0]
    tehai_n = tehai[1]
    hai = 33
    if tehai_m.count(hai) == 3 or tehai_n.count(hai) == 3 or tehai_n.count(hai) == 4:
        yaku_list[0].append("役牌:発")


def sangen_chun(tehai, yaku_list):  # 中
    tehai_m = tehai[0]
    tehai_n = tehai[1]
    hai = 34
    if tehai_m.count(hai) == 3 or tehai_n.count(hai) == 3 or tehai_n.count(hai) == 4:
        yaku_list[0].append("役牌:中")


def tanyao(tehai, yaku_list): # 断么九
    j = 0
    for hai in tehai[0]:
        if hai >= 28:
            j = 1
        if ((hai-1)%9+1) == 1 or ((hai-1)%9+1) == 9:
            j = 1
    for hai in tehai[1]:
        if hai >= 28:
            j = 1
        if ((hai-1)%9+1) == 1 or ((hai-1)%9+1) == 9:
            j = 1
    if j == 0:
        yaku_list[0].append("断么九")


def pinfu(tehai, p_kaze, bakaze, yaku_list): # 平和
    tehai_m = copy.deepcopy(tehai[0])
    hai = tehai_m.pop()
    matihai = jdg.mati(tehai_m)
    if len(tehai_m) == 13 and len(matihai) != 1:
        if sub.pinfu_sub(tehai[0]) != False and sub.pinfu_sub(tehai[0]) != p_kaze[0]+28 and sub.pinfu_sub(tehai[0]) != bakaze[0]+28 and sub.pinfu_sub(tehai[0]) < 32:
            if matihai[0]+3 != matihai[1] and matihai[0] != matihai[1]+3:
                return
            if sub.pinfu_sub(tehai[0]) != hai:
                yaku_list[0].append("平和")
                return
            elif tehai[0].count(hai) != 2:
                yaku_list[0].append("平和")
                return
            else:
                if sub.pinfu_re_sub(tehai[0]) != False and sub.pinfu_re_sub(tehai[0]) != p_kaze[0]+28 and sub.pinfu_re_sub(tehai[0]) != bakaze[0]+28 and sub.pinfu_re_sub(tehai[0]) < 32:
                    if sub.pinfu_re_sub(tehai[0])!= hai:
                        yaku_list[0].append("平和")
                        return
                    elif tehai[0].count(hai) != 2:
                        yaku_list[0].append("平和")
                        return


def ipeko(tehai, Menzen, yaku_list): # 一盃口
    tehai_m = copy.deepcopy(tehai[0])
    if Menzen:
        if sub.ipeko_sub(tehai_m):
            yaku_list[0].append("一盃口")

        
def haitei(TurnFlag, Haitei, yaku_list): # 海底撈月
    if Haitei == True and TurnFlag == "Tumo":
        yaku_list[0].append("海底撈月")


def houtei(TurnFlag, Haitei, yaku_list): # 河底撈魚
    if Haitei == True and TurnFlag == "Ron":
        yaku_list[0].append("河底撈魚")


def rinsyankaihou(Rinsyan, yaku_list): # 嶺上開花
    if Rinsyan:
        yaku_list[0].append("嶺上開花")


def chankan(Chankan, yaku_list): # 槍槓
    if Chankan:
        yaku_list[0].append("槍槓")


#2翻役
def doubreach(First_turn, Reach, yaku_list):  # ダブリー
    if First_turn == True and Reach == True:
        yaku_list[1].append("ダブル立直")


def sansyoku_123(tehai, Menzen, yaku_list): # 三色同順
    if sub.sansyoku_123_sub(tehai) and Menzen == True:
        yaku_list[1].append("三色同順")
    elif sub.sansyoku_123_sub(tehai) and Menzen == False:
        yaku_list[0].append("三色同順")


def sansyoku_111(tehai, yaku_list): # 三色同刻
    if sub.sansyoku_111_sub(tehai):
        yaku_list[1].append("三色同刻")


def sanankou(tehai, Agari, Menzen, yaku_list): # 三暗刻
    tehai_m = copy.deepcopy(tehai[0])
    hai = tehai_m.pop()
    if Agari == "Ron":
        if sub.suankou_sub(tehai, Menzen):
            yaku_list[1].append("三暗刻")
        elif sub.sanankou_sub(tehai, Menzen):
            matihai = jdg.mati(tehai_m)
            if len(matihai) >= 2:
                if hai+3 in matihai and hai < 28 and hai%9 != 0 and hai%9 != 8 and hai%9 != 7:
                    if (hai+1 in tehai_m) and (hai+2 in tehai_m):
                        yaku_list[1].append("三暗刻")
                elif hai-3 in matihai and hai < 28 and hai%9 != 1 and hai%9 != 2 and hai%9 != 3:
                    if (hai-1 in tehai_m) and (hai-2 in tehai_m):
                        yaku_list[1].append("三暗刻")
                else:
                    return
            elif len(matihai)== 1:
                yaku_list[1].append("三暗刻")
    elif Agari == "Tumo":
        if sub.sanankou_sub(tehai, Menzen):
            yaku_list[1].append("三暗刻")


def ittuu(tehai, Menzen, yaku_list): # 一気通貫
    if sub.ittuu_sub(tehai) and Menzen == True:
        yaku_list[1].append("一気通貫")
    elif sub.ittuu_sub(tehai) and Menzen == False:
        yaku_list[0].append("一気通貫")


def chitoitu(tehai, yaku_list): # 七対子
    tehai_m = copy.deepcopy(tehai[0])
    if sub.chitoi_sub(tehai_m):
        if not(sub.ryanpeko_sub(tehai)):
            yaku_list[1].append("七対子")


def toitoi(tehai, Menzen, yaku_list): # 対々和
    if sub.toitoi_sub(tehai) == True and Menzen == False:
        yaku_list[1].append("対々和")


def chanta(tehai, Menzen, yaku_list): # 混全帯幺九
    if not(sub.junchan_sub(tehai)):
        if sub.chanta_sub(tehai):
            if Menzen:
                yaku_list[1].append("混全帯幺九")
            else:
                yaku_list[0].append("混全帯幺九")


def sankantu(tehai, yaku_list): # 三槓子
    kan = 0
    if tehai[1] != [0]:
        kan = len(tehai[0]) + len(tehai[1]) - 14
    if kan == 3:
        yaku_list[1].append("三槓子")


def syousangen(tehai, yaku_list): # 小三元 32 33 34
    tehai_all = tehai[0] + tehai[1] 
    if tehai_all.count(32) == 2 and tehai_all.count(33) == 3 and tehai_all.count(34) == 3:
        yaku_list[1].append("小三元")
    elif tehai_all.count(32) == 3 and tehai_all.count(33) == 2 and tehai_all.count(34) == 3:
        yaku_list[1].append("小三元")
    elif tehai_all.count(32) == 3 and tehai_all.count(33) == 3 and tehai_all.count(34) == 2:
        yaku_list[1].append("小三元")


def honroutou(tehai, yaku_list): # 混老頭
    if not(sub.chinroutou_sub(tehai)):
        if sub.honroutou_sub(tehai):
            yaku_list[1].append("混老頭")


# 3翻役
def ryanpeko(tehai, yaku_list): # 二盃口
    if sub.ryanpeko_sub(tehai):
        yaku_list[2].append("二盃口")


def junchan(tehai, Menzen, yaku_list): # 純全帯公九
    if sub.junchan_sub(tehai):
        if Menzen:
            yaku_list[2].append("純全帯公九")
        else:
            yaku_list[1].append("純全帯公九")


def honitu(tehai, Menzen, yaku_list): # 混一色
    if chinitu(tehai, Menzen, yaku_list):
        return
    tehai_all = tehai[0] + tehai[1]
    for i in range(3):
        Yaku = True
        for hai in tehai_all:
            if hai >= 100:
                continue
            if not((1 + (9 * i) <= hai and 9 + (9 * i) >= hai) or hai > 27):
                Yaku = False
                break
        if Yaku:
            break
    if  Yaku:
        if Menzen:
            yaku_list[2].append("混一色")
        else:
            yaku_list[1].append("混一色")


# 6翻役
def chinitu(tehai, Menzen, yaku_list): # 清一色
    tehai_all = tehai[0] + tehai[1]
    for i in range(3):
        Yaku = True
        for hai in tehai_all:
            if hai >= 100:
                continue
            if not(1 + (9 * i) <= hai and 9 + (9 * i) >= hai):
                Yaku = False
                break
        if Yaku:
            break
    if  Yaku:
        if Menzen:
            yaku_list[4].append("清一色")
            return True
        else:
            yaku_list[3].append("清一色")
            return True

# 役満
def tenhou(First_turn, Reach, p_kaze, yaku_list):  # 天和
    if First_turn == True and Reach == False and p_kaze[0] == 0:
        yaku_list[5].append("天和")


def tihou(First_turn, Reach, p_kaze, yaku_list):  # 地和
    if First_turn == True and Reach == False and p_kaze[0] != 0:
        yaku_list[5].append("地和")


def suankou(tehai, TurnFlag, Menzen, yaku_list): # 四暗刻
    if sub.suankou_sub(tehai, Menzen):
        if tehai[0].count(tehai[0][-1]) == 2:
            yaku_list[5].append("四暗刻単騎")
        else:
            if TurnFlag == "Tumo":
                yaku_list[5].append("四暗刻")


def daisangen(tehai, yaku_list): # 大三元 32 33 34
    tehai_all = tehai[0] + tehai[1] 
    if tehai_all.count(32) == 3 and tehai_all.count(33) == 3 and tehai_all.count(34) == 3:
        yaku_list[5].append("大三元")


def kokusi(tehai, yaku_list): # 国士無双
    Yaku = False
    tehai_m = copy.deepcopy(tehai[0])
    tehai_m.pop()
    kokusi_13 = [1,9,10,18,19,27,28,29,30,31,32,33,34]
    if len(tehai[0]) == 14:
        kokusi_t = copy.deepcopy(tehai[0])
        kokusi_t = list(set(kokusi_t))
        kokusi_t.sort()
        if kokusi_t == kokusi_13:
            Yaku = True
    if Yaku:
        if tehai_m == kokusi_13:
            yaku_list[5].append("国士無双十三面待ち")
        else:
            yaku_list[5].append("国士無双")
        

def ryuiso(tehai, yaku_list): # 緑一色 11 12 13 15 17 33
    tehai_all = tehai[0] + tehai[1] 
    Yaku = True
    for hai in tehai_all:
        if hai >= 100:
            continue
        if hai != 11 and hai != 12 and hai != 13 and hai != 15 and hai != 17 and hai != 33:
            Yaku = False
            break
    if Yaku:
        yaku_list[5].append("緑一色")


def tuiso(tehai, yaku_list): # 字一色
    tehai_all = tehai[0] + tehai[1] 
    Yaku = True
    for hai in tehai_all:
        if hai >= 100:
            continue
        if hai <= 27:
            Yaku = False
            break
    if Yaku:
        yaku_list[5].append("字一色")


def chinroutou(tehai, yaku_list): # 清老頭
    if sub.chinroutou_sub(tehai):
        yaku_list[5].append("清老頭")


def syoususi(tehai, yaku_list): # 小四喜
    tehai_all = tehai[0] + tehai[1] 
    if tehai_all.count(28) == 2 and tehai_all.count(29) == 3 and tehai_all.count(30) == 3 and tehai_all.count(31) == 3:
        yaku_list[5].append("小四喜")
    if tehai_all.count(28) == 3 and tehai_all.count(29) == 2 and tehai_all.count(30) == 3 and tehai_all.count(31) == 3:
        yaku_list[5].append("小四喜")
    if tehai_all.count(28) == 3 and tehai_all.count(29) == 3 and tehai_all.count(30) == 2 and tehai_all.count(31) == 3:
        yaku_list[5].append("小四喜")
    if tehai_all.count(28) == 3 and tehai_all.count(29) == 3 and tehai_all.count(30) == 3 and tehai_all.count(31) == 2:
        yaku_list[5].append("小四喜")


def daisusi(tehai, yaku_list): # 大四喜
    tehai_all = tehai[0] + tehai[1] 
    if tehai_all.count(28) == 3 and tehai_all.count(29) == 3 and tehai_all.count(30) == 3 and tehai_all.count(31) == 3:
        yaku_list[5].append("大四喜")
    

def churen(tehai, yaku_list):
    tehai_m = copy.deepcopy(tehai[0])
    for i in range(3):
        churen = []
        for j in range(1, 10):
            if j == 1 or j == 9:
                for _ in range(3):
                    churen.append(j + (i*9))
            else:
                churen.append(j + (i*9))
        for j in range(1, 10):
            churen_t = copy.deepcopy(churen)
            churen_t.append(j + (i*9))
            tehai_m.sort()
            churen_t.sort()
            if churen_t == tehai_m:
                tehai_m = copy.deepcopy(tehai[0])
                tehai_m.pop()
                if churen == tehai_m:
                    yaku_list[5].append("純正九蓮宝燈")
                    return
                else:
                    yaku_list[5].append("九蓮宝燈")
                    return


def sukantu(tehai, yaku_list): # 四槓子
    if tehai[1] != [0]:
        kan = len(tehai[0]) + len(tehai[1]) - 14
        if kan == 4:
            yaku_list[5].append("四槓子")





if __name__ == "__main__":
    p_tehai = [[1,1,2,2,3,3,4,4,5,5,6,6,9,9],[0]]
    TurnFlag = "Tumo"
    FirstTurn = True
    Reach = False
    Menzen = True
    Flags = [TurnFlag, FirstTurn, Reach, Menzen]
    dora = []
    ura_dora = []
    p_kaze = [0]
    bakaze = [0]
    yaku_list = [[],[],[],[],[]]
    print(ryanpeko(p_tehai, yaku_list))
    print(yaku_list)
    #yaku_check(p_tehai, Flags, dora, ura_dora, p_kaze, bakaze)
