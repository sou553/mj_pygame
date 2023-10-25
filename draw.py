# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import tiles as tls
import judge as jdg
import copy

def haitei_page(info_list, p_kaze_t, screen):
    yama = info_list[0]
    all_tehai = info_list[1]
    all_kawa = info_list[2]
    turn = info_list[3]
    p_kaze = copy.deepcopy(p_kaze_t)
    p_tehai = all_tehai[p_kaze[0]]
    bakaze = info_list[5]
    all_points = info_list[6]
    kyoutaku = info_list[7]
    tumibou = info_list[8]
    # 手牌
    n = 0
    m = int(len(p_tehai[0]) / 3) * 3
    x = 200
    y = 750
    for hai_d in p_tehai[0]:
        filename = tls.hai_filename(hai_d)
        exec("myhai_" + str(n) + "= pygame.image.load(filename).convert_alpha()")
        exec("rect_myhai_" + str(n) + "= myhai_" + str(n) + ".get_rect()")
        exec("rect_myhai_" + str(n) + ".center = (x, y)")
        exec("screen.blit(myhai_" + str(n) + ", rect_myhai_" + str(n) + ")")
        x += 50
        n += 1
    if p_tehai[1] != [0]:
        x = m * 50 + 390
        y += 30
        for hai_d in p_tehai[1]:
            filename = tls.hai_filename(hai_d)
            exec("myhai_" + str(n) + "= pygame.image.load(filename).convert_alpha()")
            exec("rect_myhai_" + str(n) + "= myhai_" + str(n) + ".get_rect()")
            exec("rect_myhai_" + str(n) + ".center = (x, y)")
            exec("screen.blit(myhai_" + str(n) + ", rect_myhai_" + str(n) + ")")
            x += 50
            n += 1
    # 河
    n_1 = 0
    for i in range(4):
        if i == p_kaze[0]:  # player
            (x_1, y_1, x_2, y_2, x_3, y_3) = (350, 600, 350, 670, 350, 670)
            (x_add, y_add) = (50, 0)
        if i == (p_kaze[0] + 1) % 4:  # playerの下家
            (x_1, y_1, x_2, y_2, x_3, y_3) = (750, 550, 820, 550, 890, 550)
            (x_add, y_add) = (0, -50)
        if i == (p_kaze[0] + 2) % 4:  # playerの対面
            (x_1, y_1, x_2, y_2, x_3, y_3) = (700, 140, 700, 60, 700, 60)
            (x_add, y_add) = (-50, 0)
        if i == (p_kaze[0] + 3) % 4:  # playerの上家
            (x_1, y_1, x_2, y_2, x_3, y_3) = (300, 200, 230, 200, 160, 200)
            (x_add, y_add) = (0, 50)
        n_2 = 0
        for hai_d in all_kawa[i]:
            if hai_d < 0:
                continue
            filename = tls.hai_filename(hai_d)
            exec("kawa_" + str(n_1) + "= pygame.image.load(filename).convert_alpha()")
            exec("rect_kawa_" + str(n_1) + "= kawa_" + str(n_1) + ".get_rect()")
            exec("rect_kawa_" + str(n_1) + ".center = (x_1, y_1)")
            exec("screen.blit(kawa_" + str(n_1) + ", rect_kawa_" + str(n_1) + ")")
            n_1 += 1
            n_2 += 1
            x_1 += x_add
            y_1 += y_add
            if n_2 == 8:
                x_1 = x_2
                y_1 = y_2
            if n_2 == 16 and (i == (p_kaze[0] + 1) % 4 or i == (p_kaze[0] + 3) % 4):
                x = x_3
                y = y_3
    # 点数
    for n in range(4):
        if n == 0:
            point_x = 495
            point_y = 500
            point_angle = 0
        elif n == 1:
            point_x = 680
            point_y = 350
            point_angle = 90
        elif n == 2:
            point_x = 495
            point_y = 200
            point_angle = 180
        elif n == 3:
            point_x = 360
            point_y = 350
            point_angle = 270
        point_font = pygame.font.Font("ipaexg.ttf", 40)
        point_text = point_font.render(str(all_points[n][0]), True, (255, 0, 0))
        point_text = pygame.transform.rotozoom(point_text, point_angle, 1)
        screen.blit(point_text, (point_x, point_y))



def agari_page(p_tehai, Flags, yaku_list, point, screen):
    TurnFlag = Flags[0]
    point_x = 800
    point_y = 400
    point_font = pygame.font.Font("ipaexg.ttf", 60)
    point_text = point_font.render(str(point) + " 点", True, (255, 0, 0))
    screen.blit(point_text, (point_x, point_y))
    if len(yaku_list[5]) != 0:
        yaku_x = 250
        yaku_y = 300
        yaku_font = pygame.font.Font("ipaexg.ttf", 60)
        for yaku in yaku_list[5]:
            yaku_text = yaku_font.render(yaku, True, (255, 0, 0))
            screen.blit(yaku_text, (yaku_x, yaku_y))
            yaku_y += 70
    else:
        yaku_x = 250
        yaku_y = 300
        yaku_font = pygame.font.Font("ipaexg.ttf", 30)
        for n in range(5):
            if n > 2:
                han = n+2
            else:
                han = n+1
            if len(yaku_list[n]) != 0:
                for yaku in yaku_list[n]:
                    yaku_text = yaku_font.render(yaku + "  " + str(han) + "翻", True, (0, 0, 0))
                    screen.blit(yaku_text, (yaku_x, yaku_y))
                    yaku_y += 40
        for dora_str in yaku_list[6]:
            yaku_text = yaku_font.render(dora_str, True, (0, 0, 0))
            screen.blit(yaku_text, (yaku_x, yaku_y))        
            yaku_y += 40    
                    
    # ロン or ツモ
    if TurnFlag == "Ron":
        Agari_text = "ロン"
    elif TurnFlag == "Tumo":
        Agari_text = "ツモ"
    title_font = pygame.font.Font("ipaexg.ttf", 60)
    title_text = title_font.render(Agari_text, True, (255, 0, 0))
    title_x = 40
    title_y = 165
    screen.blit(title_text, (title_x, title_y))

    """title_font = pygame.font.Font("ipaexg.ttf", 24)
    title_text = title_font.render("escで終了, Space で もう一回", True, (255, 255, 255))
    title_x = 30
    title_y = 25
    screen.blit(title_text, (title_x, title_y))"""
    # 手牌
    n = 0
    m = int(len(p_tehai[0]) / 3) * 3
    x = 250
    y = 200
    for hai_d in p_tehai[0]:
        filename = tls.hai_filename(hai_d)
        exec("myhai_" + str(n) + "= pygame.image.load(filename).convert_alpha()")
        exec("rect_myhai_" + str(n) + "= myhai_" + str(n) + ".get_rect()")
        exec("rect_myhai_" + str(n) + ".center = (x, y)")
        exec("screen.blit(myhai_" + str(n) + ", rect_myhai_" + str(n) + ")")
        if n == len(p_tehai[0])-2:
            x += 65
        else:
            x += 50
        n += 1
    if p_tehai[1] != [0]:
        x = m * 50 + 450
        for hai_d in p_tehai[1]:
            filename = tls.hai_filename(hai_d)
            exec("myhai_" + str(n) + "= pygame.image.load(filename).convert_alpha()")
            exec("rect_myhai_" + str(n) + "= myhai_" + str(n) + ".get_rect()")
            exec("rect_myhai_" + str(n) + ".center = (x, y)")
            exec("screen.blit(myhai_" + str(n) + ", rect_myhai_" + str(n) + ")")
            x += 50
            n += 1


def table(info_list, screen, button, Oneturn, Reach, start, chi_hai, dora, all_points):
    yama = info_list[0]
    all_tehai = info_list[1]
    all_kawa = info_list[2]
    turn = info_list[3]
    p_kaze = info_list[4]
    bakaze = info_list[5]
    tumibou = info_list[8]
    p_kaze_s = info_list[9]
    p_tehai = all_tehai[p_kaze[0]]
    # 手牌
    n = 0
    m = int(len(p_tehai[0]) / 3) * 3
    x = 200
    y = 750
    for hai_d in p_tehai[0]:
        filename = tls.hai_filename(hai_d)
        exec("myhai_" + str(n) + "= pygame.image.load(filename).convert_alpha()")
        exec("rect_myhai_" + str(n) + "= myhai_" + str(n) + ".get_rect()")
        exec("rect_myhai_" + str(n) + ".center = (x, y)")
        exec("screen.blit(myhai_" + str(n) + ", rect_myhai_" + str(n) + ")")
        x += 50
        n += 1
    if p_tehai[1] != [0]:
        x = m * 50 + 390
        y += 30
        for hai_d in p_tehai[1]:
            filename = tls.hai_filename(hai_d)
            exec("myhai_" + str(n) + "= pygame.image.load(filename).convert_alpha()")
            exec("rect_myhai_" + str(n) + "= myhai_" + str(n) + ".get_rect()")
            exec("rect_myhai_" + str(n) + ".center = (x, y)")
            exec("screen.blit(myhai_" + str(n) + ", rect_myhai_" + str(n) + ")")
            x += 50
            n += 1
    # 河
    n_1 = 0
    for i in range(4):
        if i == p_kaze[0]:  # player
            (x_1, y_1, x_2, y_2, x_3, y_3) = (350, 600, 350, 670, 350, 670)
            (x_add, y_add) = (50, 0)
        if i == (p_kaze[0] + 1) % 4:  # playerの下家
            (x_1, y_1, x_2, y_2, x_3, y_3) = (750, 550, 820, 550, 890, 550)
            (x_add, y_add) = (0, -50)
        if i == (p_kaze[0] + 2) % 4:  # playerの対面
            (x_1, y_1, x_2, y_2, x_3, y_3) = (700, 140, 700, 60, 700, 60)
            (x_add, y_add) = (-50, 0)
        if i == (p_kaze[0] + 3) % 4:  # playerの上家
            (x_1, y_1, x_2, y_2, x_3, y_3) = (300, 200, 230, 200, 160, 200)
            (x_add, y_add) = (0, 50)
        n_2 = 0
        for hai_d in all_kawa[i]:
            if hai_d < 0:
                continue
            filename = tls.hai_filename(hai_d)
            exec("kawa_" + str(n_1) + "= pygame.image.load(filename).convert_alpha()")
            exec("rect_kawa_" + str(n_1) + "= kawa_" + str(n_1) + ".get_rect()")
            exec("rect_kawa_" + str(n_1) + ".center = (x_1, y_1)")
            exec("screen.blit(kawa_" + str(n_1) + ", rect_kawa_" + str(n_1) + ")")
            n_1 += 1
            n_2 += 1
            x_1 += x_add
            y_1 += y_add
            if n_2 == 8:
                x_1 = x_2
                y_1 = y_2
            if n_2 == 16 and (i == (p_kaze[0] + 1) % 4 or i == (p_kaze[0] + 3) % 4):
                x = x_3
                y = y_3
    # 点数
    for n in range(4):
        point_font = pygame.font.Font("ipaexg.ttf", 30)
        point_text = point_font.render(str(all_points[n][0]), True, (255, 0, 0))
        if n == 0:
            point_x = 495
            point_y = 500
            point_angle = 0
        elif n == 1:
            point_x = 680
            point_y = 350
            point_angle = 90
        elif n == 2:
            point_x = 495
            point_y = 200
            point_angle = 180
        elif n == 3:
            point_x = 360
            point_y = 350
            point_angle = 270
        point_text = pygame.transform.rotozoom(point_text, point_angle, 1)
        screen.blit(point_text, (point_x, point_y))
    
    # 誰の手番か
    if 0 < start and 15 > start :
        if turn[0] == p_kaze[0]:
            stick = pygame.image.load("files/png/stick_1.png").convert_alpha()
            rect_stick = stick.get_rect()
            rect_stick.center = (345, 360)
            screen.blit(stick, rect_stick)
        if (turn[0]+1)%4 == p_kaze[0]:
            stick = pygame.image.load("files/png/stick_0.png").convert_alpha()
            rect_stick = stick.get_rect()
            rect_stick.center = (545, 185)
            screen.blit(stick, rect_stick)
        if (turn[0]+2)%4 == p_kaze[0]:
            stick = pygame.image.load("files/png/stick_1.png").convert_alpha()
            rect_stick = stick.get_rect()
            rect_stick.center = (715, 365)
            screen.blit(stick, rect_stick)
        if (turn[0]+3)%4 == p_kaze[0]:
            stick = pygame.image.load("files/png/stick_0.png").convert_alpha()
            rect_stick = stick.get_rect()
            rect_stick.center = (530, 550)
            screen.blit(stick, rect_stick)
    # 場風
    if p_kaze[0] == 0:
        bakaze_0 = pygame.image.load("files/ms_all/c_e_1.gif").convert_alpha()
        rect_bakaze_0 = bakaze_0.get_rect()
        rect_bakaze_0.center = (400, 515)
        screen.blit(bakaze_0, rect_bakaze_0)
        bakaze_0 = pygame.image.load("files/ms_all/c_s_4.gif").convert_alpha()
        rect_bakaze_0 = bakaze_0.get_rect()
        rect_bakaze_0.center = (680, 500)
        screen.blit(bakaze_0, rect_bakaze_0)
        bakaze_0 = pygame.image.load("files/ms_all/c_w_3.gif").convert_alpha()
        rect_bakaze_0 = bakaze_0.get_rect()
        rect_bakaze_0.center = (670, 220)
        screen.blit(bakaze_0, rect_bakaze_0)
        bakaze_0 = pygame.image.load("files/ms_all/c_n_2.gif").convert_alpha()
        rect_bakaze_0 = bakaze_0.get_rect()
        rect_bakaze_0.center = (375, 230)
        screen.blit(bakaze_0, rect_bakaze_0)
    elif p_kaze[0] == 1:
        bakaze_0 = pygame.image.load("files/ms_all/c_s_1.gif").convert_alpha()
        rect_bakaze_0 = bakaze_0.get_rect()
        rect_bakaze_0.center = (400, 515)
        screen.blit(bakaze_0, rect_bakaze_0)
        bakaze_0 = pygame.image.load("files/ms_all/c_w_4.gif").convert_alpha()
        rect_bakaze_0 = bakaze_0.get_rect()
        rect_bakaze_0.center = (680, 500)
        screen.blit(bakaze_0, rect_bakaze_0)
        bakaze_0 = pygame.image.load("files/ms_all/c_n_3.gif").convert_alpha()
        rect_bakaze_0 = bakaze_0.get_rect()
        rect_bakaze_0.center = (670, 220)
        screen.blit(bakaze_0, rect_bakaze_0)
        bakaze_0 = pygame.image.load("files/ms_all/c_e_2.gif").convert_alpha()
        rect_bakaze_0 = bakaze_0.get_rect()
        rect_bakaze_0.center = (375, 230)
        screen.blit(bakaze_0, rect_bakaze_0)
    elif p_kaze[0] == 2:
        bakaze_0 = pygame.image.load("files/ms_all/c_w_1.gif").convert_alpha()
        rect_bakaze_0 = bakaze_0.get_rect()
        rect_bakaze_0.center = (400, 515)
        screen.blit(bakaze_0, rect_bakaze_0)
        bakaze_0 = pygame.image.load("files/ms_all/c_n_4.gif").convert_alpha()
        rect_bakaze_0 = bakaze_0.get_rect()
        rect_bakaze_0.center = (680, 500)
        screen.blit(bakaze_0, rect_bakaze_0)
        bakaze_0 = pygame.image.load("files/ms_all/c_e_3.gif").convert_alpha()
        rect_bakaze_0 = bakaze_0.get_rect()
        rect_bakaze_0.center = (670, 220)
        screen.blit(bakaze_0, rect_bakaze_0)
        bakaze_0 = pygame.image.load("files/ms_all/c_s_2.gif").convert_alpha()
        rect_bakaze_0 = bakaze_0.get_rect()
        rect_bakaze_0.center = (375, 230)
        screen.blit(bakaze_0, rect_bakaze_0)
    elif p_kaze[0] == 3:
        bakaze_0 = pygame.image.load("files/ms_all/c_n_1.gif").convert_alpha()
        rect_bakaze_0 = bakaze_0.get_rect()
        rect_bakaze_0.center = (400, 515)
        screen.blit(bakaze_0, rect_bakaze_0)
        bakaze_0 = pygame.image.load("files/ms_all/c_e_4.gif").convert_alpha()
        rect_bakaze_0 = bakaze_0.get_rect()
        rect_bakaze_0.center = (680, 500)
        screen.blit(bakaze_0, rect_bakaze_0)
        bakaze_0 = pygame.image.load("files/ms_all/c_s_3.gif").convert_alpha()
        rect_bakaze_0 = bakaze_0.get_rect()
        rect_bakaze_0.center = (670, 220)
        screen.blit(bakaze_0, rect_bakaze_0)
        bakaze_0 = pygame.image.load("files/ms_all/c_w_2.gif").convert_alpha()
        rect_bakaze_0 = bakaze_0.get_rect()
        rect_bakaze_0.center = (375, 230)
        screen.blit(bakaze_0, rect_bakaze_0)
    # ドラ表
    x_1 = 60
    y_1 = 70
    n = 0
    for dora_hai in dora:
        filename = tls.hai_filename(dora_hai + 0.1)
        exec("dora_" + str(n) + "= pygame.image.load(filename).convert_alpha()")
        exec("rect_dora_" + str(n) + "= dora_" + str(n) + ".get_rect()")
        exec("rect_dora_" + str(n) + ".center = (x_1, y_1)")
        exec("screen.blit(dora_" + str(n) + ", rect_dora_" + str(n) + ")")
        n += 1
        x_1 += 50
    #東一局
    x = 60
    y = 120
    if bakaze[0] == 0:
        ba = "東"
    elif bakaze[0] == 1:
        ba = "南"
    elif bakaze[0] == 2:
        ba = "西"
    elif bakaze[0] == 3:
        ba = "北"
    if p_kaze[0] == p_kaze_s[0]:
        kyoku = "一局"
    elif p_kaze[0] == (p_kaze_s[0]+3)%4:
        kyoku = "二局"
    elif p_kaze[0] == (p_kaze_s[0]+2)%4:
        kyoku = "三局"
    elif p_kaze[0] == (p_kaze_s[0]+1)%4:
        kyoku = "四局"
    honba = int(tumibou[0]/300)
    text_font = pygame.font.Font("ipaexg.ttf", 30)
    ba_text = text_font.render(ba + kyoku, True, (0, 0, 0))
    screen.blit(ba_text, (x, y))
    y += 40
    honba_text = text_font.render(str(honba) + "本場", True, (0, 0, 0))
    screen.blit(honba_text, (x, y))

    #リー棒
    if Reach != False:    
        stick = pygame.image.load("files/png/reach_stick.png").convert_alpha()
        rect_stick = stick.get_rect()
        rect_stick.center = (530, 485)
        screen.blit(stick, rect_stick)
    # ボタン
    if Oneturn == "Button":
        if button[0] == 1:  # chi-
            chi = pygame.image.load("files/png/button_chi.png").convert_alpha()
            rect_chi = chi.get_rect()
            rect_chi.center = (380, 530)
            screen.blit(chi, rect_chi)
        if button[1] == 1:  # pon
            pon = pygame.image.load("files/png/button_pon.png").convert_alpha()
            rect_pon = pon.get_rect()
            rect_pon.center = (485, 530)
            screen.blit(pon, rect_pon)
        if button[2] == 1 or button[3] == 1 or button[4] == 1:  # kan
            kan = pygame.image.load("files/png/button_kan.png").convert_alpha()
            rect_kan = kan.get_rect()
            rect_kan.center = (590, 530)
            screen.blit(kan, rect_kan)
        if button[5] == 1:  # ron
            ron = pygame.image.load("files/png/button_ron.png").convert_alpha()
            rect_ron = ron.get_rect()
            rect_ron.center = (380, 460)
            screen.blit(ron, rect_ron)
        if button[6] == 1:  # tumo
            tumo = pygame.image.load("files/png/button_tumo.png").convert_alpha()
            rect_tumo = tumo.get_rect()
            rect_tumo.center = (482, 460)
            screen.blit(tumo, rect_tumo)
        if button[7] == 1:  # reach
            reach = pygame.image.load("files/png/button_reach.png").convert_alpha()
            rect_reach = reach.get_rect()
            rect_reach.center = (595, 460)
            screen.blit(reach, rect_reach)
        if button[8] == 1:  # cancel
            cancel = pygame.image.load("files/png/button_cancel.png").convert_alpha()
            rect_cancel = cancel.get_rect()
            rect_cancel.center = (420, 390)
            screen.blit(cancel, rect_cancel)
    # チー牌の選択のため
    if Oneturn == "Chi":
        x_1 = 400
        y_1 = 500
        n_1 = 0
        for hais in chi_hai:
            for hai_c in hais:
                filename = tls.hai_filename(hai_c)
                exec(
                    "chi_" + str(n_1) + "= pygame.image.load(filename).convert_alpha()"
                )
                exec("rect_chi_" + str(n_1) + "= chi_" + str(n_1) + ".get_rect()")
                exec("rect_chi_" + str(n_1) + ".center = (x_1, y_1)")
                exec("screen.blit(chi_" + str(n_1) + ", rect_chi_" + str(n_1) + ")")
                x_1 += 35
                n_1 += 1
            x_1 += 20
    
    

