# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys
import create as crt
import tiles as tls
import judge as jdg
import oneround as rnd
import draw
import yaku
import calculation as cl
import copy


def oneround_page(info_list):
    pygame.init()
    (w, h) = 1200, 900
    pygame.display.set_mode((w, h), 0, 32)
    screen = pygame.display.get_surface()
    pygame.display.set_caption("Majong")
    table_png = "files/png/green.png"  # 背景画像
    bg = pygame.image.load(table_png).convert_alpha()
    rect_bg = bg.get_rect()

    # hai_w = 33
    # hai_h = 59
    yama = info_list[0]
    all_tehai = info_list[1]
    all_kawa = info_list[2]
    turn = info_list[3]
    p_kaze = info_list[4]
    bakaze = info_list[5]
    all_points = info_list[6]
    kyoutaku = info_list[7]
    tumibou = info_list[8]
    p_kaze_s = info_list[9]
    p_tehai = all_tehai[p_kaze[0]]

    button = [0, 0, 0, 0, 0, 0, 0, 0, 0]  # chi-,pon,kan,anakan,kakan,ron,tumo,reach,cancel

    Stick = 0
    

    TurnFlag = None
    FirstTurn = True
    Reach = False
    Menzen = True
    Haitei = False
    Rinsyan = False
    Chankan = False
    chi_hai = []
    dora = []
    ura_dora = []

    dora.append(yama[-5])
    ura_dora.append(yama[-9])

    while True:
        # 描写
        screen.fill((0, 0, 0, 0))
        screen.blit(bg, rect_bg)
        draw.table(info_list, screen, button, TurnFlag, Reach, Stick, chi_hai, dora, all_points)

        pygame.time.wait(33)
        pygame.display.update()
        

        # main
        if TurnFlag == None:
            pygame.time.wait(800)
            if turn[0] % 4 == p_kaze[0]:  # Player
                rnd.draw_player(info_list)
                TurnFlag = "Player"
            else:  # CPU
                rnd.draw_cpu(info_list)
                TurnFlag = "CPU"
                hai_n = all_kawa[turn[0]][-1]
                if len(yama) == 14:
                    Haitei = True
                # print(hai_n)
                if not(Reach) and not(Haitei):
                    if jdg.naki_kan_conf(yama, p_tehai, hai_n):
                        button[1] = 1
                        button[2] = 1
                        button[8] = 1
                    if jdg.naki_pon_conf(p_tehai, hai_n):
                        button[1] = 1
                        button[8] = 1
                    if (turn[0] + 1) % 4 == p_kaze[0]:
                        if jdg.naki_c_conf(p_tehai, hai_n):
                            button[0] = 1
                            button[8] = 1
            turn[0] = (turn[0] + 1) % 4

        # リーチ、あがり
        if TurnFlag == "Player":
            if jdg.naki_ankan_conf(yama, p_tehai) and not(Reach):  # Ankan
                button[3] = 1
                button[8] = 1
            if jdg.naki_kakan_conf(yama, p_tehai):  # Kakan
                button[4] = 1
                button[8] = 1
            if Reach == False and Menzen == True:
                mati_hai = jdg.reach(p_tehai)[0]
                dis_hai = jdg.reach(p_tehai)[1] 
                if len(mati_hai) != 0 or len(dis_hai) != 0: # 立直
                    button[7] = 1
                    button[8] = 1
            Flags = [TurnFlag, FirstTurn, Reach, Menzen, Haitei, Rinsyan, Chankan]
            if jdg.tumo(p_tehai, Flags, dora, ura_dora, p_kaze, bakaze):  # つも
                button[6] = 1
                button[8] = 1
        elif TurnFlag == "CPU": 
            Flags = [TurnFlag, FirstTurn, Reach, Menzen, Haitei, Rinsyan, Chankan]
            if jdg.ron(p_tehai, Flags, dora, ura_dora, p_kaze, bakaze, hai_n) and not((int(hai_n) + 0.1) in all_kawa[p_kaze[0]]): # ロン
                button[5] = 1
                button[8] = 1
            else:
                TurnFlag = None

        #Flag
        if TurnFlag != None:
            Stick = (Stick + 1) % 25
        else:
            Stick = 1

        if len(yama) == 14 and button == [0, 0, 0, 0, 0, 0, 0, 0, 0]:  # haitei
            Haitei = True
        
        if TurnFlag == "Ron" or TurnFlag == "Tumo":
            Flags = [TurnFlag, FirstTurn, Reach, Menzen, Haitei, Rinsyan, Chankan]
            result_page(info_list, Flags, dora, ura_dora)
            if p_kaze[0] != 0:
                p_kaze[0] = (p_kaze[0]+3)%4
            pygame.init()
            return p_kaze
        if Haitei == True and button == [0, 0, 0, 0, 0, 0, 0, 0, 0]:
            print("海底")
            print(all_tehai)
            haitei_page(info_list)
            p_kaze[0] = (p_kaze[0]+3)%4 #↑で親が聴牌なら +1 している
            pygame.init()
            return p_kaze
        
        if Reach == "FirstTurn" and len(p_tehai[0])%3 == 2 and button[6] == 0:# 一発かどうか
            j = 0
            for hai_r in all_kawa[p_kaze[0]]:
                if str(hai_r)[-1] == "3":
                    j = 1
            if j == 1:
                Reach = True

        if Reach == True and len(p_tehai[0])%3 == 2 and button == [0, 0, 0, 0, 0, 0, 0, 0, 0]: # 立直の時は自摸切り
            all_kawa[p_kaze[0]].append((p_tehai[0].pop() + 0.1))
            TurnFlag = None
        
        if Rinsyan == True and button == [0, 0, 0, 0, 0, 0, 0, 0, 0]:
            Rinsyan = False

        # 一番下に
        if button != [0, 0, 0, 0, 0, 0, 0, 0, 0]:
            TurnFlag = "Button"


        # event
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                k_x, k_y = event.pos
                #print(k_x, k_y)
                #print(p_tehai)
                if TurnFlag == "Player" or TurnFlag == "Dispose":
                    if 725 <= k_y and 775 >= k_y:
                        x_m = 185
                        for i in range(len(p_tehai[0])):
                            if (x_m + i * 50) <= k_x and (x_m + 30 + i * 50) >= k_x:
                                if FirstTurn == True and Reach == False:
                                    FirstTurn = False
                                if Reach == "FirstTurn":
                                    if p_tehai[0][i] in dis_hai:
                                        all_kawa[p_kaze[0]].append((p_tehai[0].pop(i) + 0.3))
                                    else:
                                        print("捨てれない")
                                        break
                                else:
                                    all_kawa[p_kaze[0]].append((p_tehai[0].pop(i) + 0.1))
                                p_tehai[0].sort()
                                if len(yama) == 14:  # haitei
                                    Haitei = True
                                    TurnFlag = "Player" # cpuはロンできん
                                else:
                                    TurnFlag = None
                if TurnFlag == "Button":
                    if 500 <= k_y and 560 >= k_y:
                        if 330 <= k_x and 430 >= k_x:  # chi
                            if button[0] == 1:
                                chi_hai = jdg.naki_c_select(p_tehai, hai_n)
                                Menzen = False
                                FirstTurn = False
                                if len(chi_hai) == 1:
                                    jdg.naki_c_do(p_tehai, hai_n, turn, all_kawa)
                                    TurnFlag = "Dispose"
                                    button = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                                    turn[0] = (p_kaze[0] + 1) % 4
                                else:
                                    TurnFlag = "Chi"
                                    button = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                        if 430 <= k_x and 530 >= k_x:  # pon
                            if button[1] == 1:
                                jdg.naki_p_do(p_tehai, hai_n, turn, p_kaze, all_kawa)
                                TurnFlag = "Dispose"
                                Menzen = False
                                FirstTurn = False
                                button = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                                turn[0] = (p_kaze[0] + 1) % 4
                        if 530 <= k_x and 630 >= k_x:  # kan
                            Rinsyan = True
                            if not(Reach):
                                FirstTurn = False
                            if button[2] == 1:
                                jdg.naki_k_do(yama, p_tehai, hai_n, turn, p_kaze, all_kawa, dora, ura_dora)
                                TurnFlag = "Player"
                                Menzen = False
                                FirstTurn = False
                                button = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                                turn[0] = (p_kaze[0] + 1) % 4
                            if button[3] == 1:
                                jdg.naki_ankan_do(yama, p_tehai, dora, ura_dora)
                                button = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                                TurnFlag = "Player"
                            if button[4] == 1:
                                jdg.naki_kakan_do(yama, p_tehai, dora, ura_dora)
                                button = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                                TurnFlag = "Player"
                    if 430 <= k_y and 490 >= k_y:
                        if 330 <= k_x and 430 >= k_x:  # ron
                            if button[5] == 1:
                                button = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                                TurnFlag = "Ron"
                                p_tehai[0].append(int(hai_n) + 0.0)
                        if 430 <= k_x and 530 >= k_x:  # tumo
                            if button[6] == 1:
                                button = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                                TurnFlag = "Tumo"
                        if 530 <= k_x and 630 >= k_x:  # reach
                            if button[7] == 1:
                                all_points[0][0] -= 1000
                                kyoutaku[0] += 1000
                                button = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                                TurnFlag = "Dispose"
                                Reach = "FirstTurn"
                    if 330 <= k_x and 500 >= k_x and 380 <= k_y and 420 >= k_y:  # cancel
                        if button[8] == 1:
                            button = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                            if (turn[0] + 3) % 4 == p_kaze[0]:
                                TurnFlag = "Dispose"
                            else:
                                TurnFlag = None

                if TurnFlag == "Chi":
                    if 470 <= k_y and 530 >= k_y:
                        x_m = 385
                        for i in range(len(chi_hai)):
                            if (x_m + i * 90) <= k_x and (x_m + 60 + i * 90) >= k_x:
                                jdg.naki_c_do(p_tehai, hai_n, turn, all_kawa, i)
                                TurnFlag = "Dispose"
                                turn[0] = (p_kaze[0] + 1) % 4


def result_page(info_list, Flags, dora, ura_dora):
    yama = info_list[0]
    all_tehai = info_list[1]
    all_kawa = info_list[2]
    turn = info_list[3]
    p_kaze = info_list[4]
    bakaze = info_list[5]
    all_points = info_list[6]
    kyoutaku = info_list[7]
    tumibou = info_list[8]
    tehai = all_tehai[p_kaze[0]]
    pygame.init()
    (w, h) = 1200, 900
    pygame.display.set_mode((w, h), 0, 32)
    screen = pygame.display.get_surface()
    pygame.display.set_caption("Majong")
    table_png = "files/png/green.png"  # 背景画像
    bg = pygame.image.load(table_png).convert_alpha()
    rect_bg = bg.get_rect()
    TurnFlag = Flags[0]
    yaku_list = yaku.yaku_check(tehai, Flags, dora, ura_dora, p_kaze, bakaze)

    points = cl.points(tehai, Flags, p_kaze, bakaze, yaku_list)
    all_points[0][0] += kyoutaku[0]
    kyoutaku[0] = 0
    if p_kaze[0] == 0 and TurnFlag == "Ron":
        point = points[0]
        all_points[(turn[0]+3)%4][0] -= point
        all_points[0][0] += point
    elif p_kaze[0] == 0 and TurnFlag == "Tumo":
        point = points[0] * 3
        all_points[1][0] -= points[0]
        all_points[2][0] -= points[0]
        all_points[3][0] -= points[0]
        all_points[0][0] += point
    elif p_kaze[0] != 0 and TurnFlag == "Ron":
        point = points[0]
        all_points[(turn[0]+3)%4][0] -= point
        all_points[0][0] += point
    elif p_kaze[0] != 0 and TurnFlag == "Tumo":
        point = points[0] + points[1] * 2
        if p_kaze[0] == 1:
            all_points[1][0] -= points[1]
            all_points[2][0] -= points[1]
            all_points[3][0] -= points[0]
        if p_kaze[0] == 2:
            all_points[1][0] -= points[1]
            all_points[2][0] -= points[0]
            all_points[3][0] -= points[1]
        if p_kaze[0] == 3:
            all_points[1][0] -= points[0]
            all_points[2][0] -= points[1]
            all_points[3][0] -= points[1]
        all_points[0][0] += point

    while True:
        screen.fill((0, 0, 0, 0))
        screen.blit(bg, rect_bg)
        draw.agari_page(tehai, Flags, yaku_list, point, screen)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    return
                if event.key == K_ESCAPE:
                    sys.exit()


def haitei_page(info_list):
    yama = info_list[0]
    all_tehai = info_list[1]
    all_kawa = info_list[2]
    turn = info_list[3]
    p_kaze = info_list[4]
    bakaze = info_list[5]
    all_points = info_list[6]
    kyoutaku = info_list[7]
    tumibou = info_list[8]
    tehai = all_tehai[p_kaze[0]]
    p_kaze_t = copy.deepcopy(p_kaze)
    pygame.init()
    (w, h) = 1200, 900
    pygame.display.set_mode((w, h), 0, 32)
    screen = pygame.display.get_surface()
    pygame.display.set_caption("Majong")
    table_png = "files/png/green.png"  # 背景画像
    bg = pygame.image.load(table_png).convert_alpha()
    rect_bg = bg.get_rect()
    #聴牌
    tenpai_t = [0,0,0,0]
    haitei_font = pygame.font.Font("ipaexg.ttf", 90)
    
    for n in range(4):
        tehai_t = copy.deepcopy(all_tehai[n])
        while True:
            if len(tehai_t[0])%3 != 1:
                tehai_t[0].pop()
            else:
                break
        mati_hai = jdg.mati(tehai_t[0])
        if n == p_kaze_t[0]:#player
            haitei_x_0 = 450
            haitei_y_0 = 590
            haitei_angle_0 = 0
            if len(mati_hai) != 0:
                tenpai_t[0] = 1
                if p_kaze_t[0] == 0:
                    p_kaze[0] = (p_kaze[0]+1)%4
                haitei_text = haitei_font.render("聴牌", True, (255, 0, 0))
            else:
                haitei_text = haitei_font.render("不聴", True, (0, 0, 0))
            haitei_text_0 = pygame.transform.rotozoom(haitei_text, haitei_angle_0, 1)
        elif n == (p_kaze_t[0]+1)%4:#下家
            haitei_x_1 = 730
            haitei_y_1 = 300
            haitei_angle_1 = 90
            if len(mati_hai) != 0:
                tenpai_t[1] = 1
                if p_kaze_t[0] == 3:
                    p_kaze[0] = (p_kaze[0]+1)%4
                haitei_text = haitei_font.render("聴牌", True, (255, 0, 0))
            else:
                haitei_text = haitei_font.render("不聴", True, (0, 0, 0))
            haitei_text_1 = pygame.transform.rotozoom(haitei_text, haitei_angle_1, 1)
        elif n == (p_kaze_t[0]+2)%4:#対面
            haitei_x_2 = 450
            haitei_y_2 = 55
            haitei_angle_2 = 180
            if len(mati_hai) != 0:
                tenpai_t[2] = 1
                if p_kaze_t[0] == 2:
                    p_kaze[0] = (p_kaze[0]+1)%4
                haitei_text = haitei_font.render("聴牌", True, (255, 0, 0))
            else:
                haitei_text = haitei_font.render("不聴", True, (0, 0, 0))
            haitei_text_2 = pygame.transform.rotozoom(haitei_text, haitei_angle_2, 1)
        elif n == (p_kaze_t[0]+3)%4:#上家
            haitei_x_3 = 220
            haitei_y_3 = 300
            haitei_angle_3 = 270
            if len(mati_hai) != 0:
                tenpai_t[3] = 1
                if p_kaze_t[0] == 1:
                    p_kaze[0] = (p_kaze[0]+1)%4
                haitei_text = haitei_font.render("聴牌", True, (255, 0, 0))
            else:
                haitei_text = haitei_font.render("不聴", True, (0, 0, 0))
            haitei_text_3 = pygame.transform.rotozoom(haitei_text, haitei_angle_3, 1)

    #点数のやり取り
    j = tenpai_t.count(1)
    if j == 0 or j == 4:
        pass
    elif j == 1:
        for n in range(4):
            i = tenpai_t[n]
            if i == 1:
                all_points[n][0] += 3000
            else:
                all_points[n][0] -= 1000
    elif j == 2:
        for n in range(4):
            i = tenpai_t[n]
            if i == 1:
                all_points[n][0] += 1500
            else:
                all_points[n][0] -= 1500
    elif j == 3:
        for n in range(4):
            i = tenpai_t[n]
            if i == 1:
                all_points[n][0] += 1000
            else:
                all_points[n][0] -= 3000
    screen.fill((0, 0, 0, 0))
    screen.blit(bg, rect_bg)
    draw.haitei_page(info_list, p_kaze_t, screen)
    screen.blit(haitei_text_0 , (haitei_x_0, haitei_y_0))
    screen.blit(haitei_text_1 , (haitei_x_1, haitei_y_1))
    screen.blit(haitei_text_2 , (haitei_x_2, haitei_y_2))
    screen.blit(haitei_text_3 , (haitei_x_3, haitei_y_3))

    while True:    
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    return
                if event.key == K_ESCAPE:
                    sys.exit()



if __name__ == "__main__":
    p_kaze = [0]
    bakaze = [0]
    yama = crt.make_yama()
    all_tehai = crt.idv_tehai(yama)  # all_tehai[[player],[pl
    turn = []
    turn.append(0)
    all_tehai[p_kaze[0]] = [[1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,11.0,11.0,33.0,13.0], [0]]
    yama[4] = 12.0
    all_kawa = [[], [], [], []]
    all_points = [[25000], [25000], [25000], [25000]] 
    info_list = [yama, all_tehai, all_kawa, turn, p_kaze, bakaze, all_points, [0], [0] ,[0]]
    oneround_page(info_list)
