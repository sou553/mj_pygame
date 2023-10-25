import tiles as tls
import copy
import yaku

def yaku_conf(tehai, Flags, dora, ura_dora, p_kaze, bakaze):
    yaku_list = yaku.yaku_check(tehai, Flags, dora, ura_dora, p_kaze, bakaze)#1,2,3,5,6,13

    n = len(yaku_list[0]) + len(yaku_list[1]) + len(yaku_list[2]) + len(yaku_list[3]) + len(yaku_list[4]) + len(yaku_list[5])   

    if n != 0:
        return True
    else:
        return False


def reach(p_tehai):
    mati_hais = []
    dis_hais = []
    for i in range(len(p_tehai[0])):
        tehai_m = copy.deepcopy(p_tehai[0])
        hai = tehai_m.pop(i)
        if len(mati(tehai_m)) != 0:
            dis_hais.append(hai)
            for hai_a in mati(tehai_m):
                mati_hais.append(hai_a)
    return [mati_hais, dis_hais] # 待ち牌, 立直のために捨てる牌


def tumo(tehai, Flags, dora, ura_dora, p_kaze, bakaze):
    n = len(tehai[0])
    tehai_m = tehai[0][:n-1]
    hai = tehai[0][-1]

    if hai in mati(tehai_m):
        if yaku_conf(tehai, Flags, dora, ura_dora, p_kaze, bakaze) == True:
            return True
    else:
        return False
    

def ron(tehai, Flags, dora, ura_dora, p_kaze, bakaze, hai_n):
    tehai_m = copy.deepcopy(tehai[0])
    tehai_n = copy.deepcopy(tehai[1])
    hai = int(hai_n)

    if hai in mati(tehai_m):
        tehai_m.append(hai)
        if yaku_conf([tehai_m,tehai_n], Flags, dora, ura_dora, p_kaze, bakaze) == True:
            return True
    else:
        return False
    

def mati(tehai_m):
    a1 = []
    a4 = []
    agarihai = []
    a1.append(tehai_m)

    #ちーとい
    if seven(tehai_m) != None:
        agarihai.append(seven(tehai_m))

    l =len(tehai_m)
    if l == 1:#くそ鳴き
        agarihai.append(tehai_m[0])
        return agarihai
    elif l == 4:
        a2 = [tehai_m]
    else:
        for _ in range(int(l/4)):
            a2 = []
            for x in a1:
                i = (tehai_del(x))
                for y in i:
                    a2.append(y)
            a1 = a2
    
    a3 = list(map(list, set(map(tuple, a2))))

    for pai4 in a3:
        a4.append(mati_4(pai4))

    for x in a4:
        for y in x:
            agarihai.append(y)

    agarihai = list(set(agarihai))
    agarihai.sort()

    return agarihai


def seven(tehai):#list[13] ちーとい
    j = 0
    for i in range(1,35):
        if tehai.count(i) == 2:
            j += 1
        if tehai.count(i) == 1:
            agarihai = i
    if j == 6:
        return agarihai
    else:
        return None
    

def tehai_del(tehai_m):#list[]
    print_list = []
    
    for i in range(len(tehai_m)):
        exec("tehai_" + str(i) + "= copy.deepcopy(tehai_m)")
        exec("print_list.append(del_3(tehai_" + str(i) + ",i))")

    try:
        while True:
            print_list.remove(0)
    except:
        pass

    p = list(map(list, set(map(tuple, print_list))))

    return p#list[][]
    

def del_3(tehai, i):#list[],int
    j = 0
    max_l = len(tehai)
    for a in range(i, max_l):
        for b in range(a+1, max_l):
            for c in range(b+1, max_l):
                x = tehai[a]
                y = tehai[b]
                z = tehai[c]
                if (x < 10 and y < 10 and z < 10):
                    #print(a,b,c)
                    if (x == y and y == z):
                        tehai[a] = 0
                        tehai[b] = 0
                        tehai[c] = 0
                        j += 1
                        break
                    elif (x+1 == y and y+1 == z):
                        tehai[a] = 0
                        tehai[b] = 0
                        tehai[c] = 0
                        j += 1
                        break
                    else:
                        continue
                elif (x > 9 and y > 9 and z > 9) and (x < 19 and y < 19 and z < 19):
                    #print(a,b,c)
                    if (x == y and y == z):
                        tehai[a] = 0
                        tehai[b] = 0
                        tehai[c] = 0
                        j += 1
                        break
                    elif (x+1 == y and y+1 == z):
                        tehai[a] = 0
                        tehai[b] = 0
                        tehai[c] = 0
                        j += 1
                        break
                    else:
                        continue
                elif (x > 18 and y > 18 and z > 18) and (x < 28 and y < 28 and z < 28):
                    #print(a,b,c)
                    if (x == y and y == z):
                        tehai[a] = 0
                        tehai[b] = 0
                        tehai[c] = 0
                        j += 1
                        break
                    elif (x+1 == y and y+1 == z):
                        tehai[a] = 0
                        tehai[b] = 0
                        tehai[c] = 0
                        j += 1
                        break
                    else:
                        continue
                elif (x > 27 and y > 27 and z > 27):
                    if(x == y and y == z):
                        tehai[a] = 0
                        tehai[b] = 0
                        tehai[c] = 0
                        j += 1
                        break
                    else:
                        continue
                if j == 1:
                    break
            if j == 1:
                break
        if j == 1:
            break
    
        
    try:
        for a in range(3):
            tehai.remove(0)
        return tehai#list[]
    except:
        return 0


def mati_4(tehai_4):
    agarihai = []
    tehai_4.sort()
    w = tehai_4[0]
    x = tehai_4[1]
    y = tehai_4[2]
    z = tehai_4[3]

    if z < 28:
        if w == x:
            if x == y:
                if y == z:
                    pass#槓子なので
                elif w+1 == z and ((w-1)%9+1) != 9:#3334
                    if ((w-1)%9+1) != 1:
                        agarihai.append(w-1)
                    agarihai.append(z)
                    if ((z-1)%9+1) != 9:
                        agarihai.append(z+1)
                elif w+2 == z and ((w-1)%9+1) != 8 and ((w-1)%9+1) != 9:#3335
                    agarihai.append(w+1)
                    agarihai.append(z)
                else:#3336
                    agarihai.append(z)
            elif y == z:#3344
                agarihai.append(w)
                agarihai.append(y)
            elif y+1 == z and ((y-1)%9+1) != 9:#3345
                if ((y-1)%9+1) != 1:
                    agarihai.append(y-1)
                if ((z-1)%9+1) != 9:
                    agarihai.append(z+1)
            elif y+2 == z and ((y-1)%9+1) != 8 and ((y-1)%9+1) != 9:#3346
                agarihai.append(y+1)
        elif w+1 == x and ((w-1)%9+1) != 9:#34
            if x == y:#344
                if x == z:#3444
                    if ((w-1)%9+1) != 1:
                        agarihai.append(w-1)
                    agarihai.append(w)
                    if ((w-1)%9+1) != 8 and ((w-1)%9+1) != 9:
                        agarihai.append(w+2)
                elif y+1 == z and ((y-1)%9+1) != 9:#3445
                    agarihai.append(x)
            elif x+1 == y and ((x-1)%9+1) != 9:#345
                if y == z:#3455
                    if ((w-1)%9+1) != 1:
                        agarihai.append(w-1)
                    if ((w-1)%9+1) != 8 and ((w-1)%9+1) != 9:
                        agarihai.append(w+2)
                elif y+1 == z and ((y-1)%9+1) != 9:#3456
                    agarihai.append(w)
                    agarihai.append(z)
                else:#3457
                    agarihai.append(z)
            elif y == z:#3466
                if ((w-1)%9+1) != 1:
                    agarihai.append(w-1)
                if ((x-1)%9+1) != 9:
                    agarihai.append(x+1)
        elif w+2 == x and ((w-1)%9+1) != 8 and ((w-1)%9+1) != 9:#35
            if x == y:#355
                if y == z:#3555
                    agarihai.append(w)
                    agarihai.append(w+1)
            elif y == z:#3566
                agarihai.append(w+1)
        else:
            if x == y and y == z:#3666
                agarihai.append(w)
            elif x+1 == y and y+1 == z and ((x-1)%9+1) != 8 and ((x-1)%9+1) != 9:#3678
                agarihai.append(w)
    elif y < 28:
        if w == x and w == y:#333東
            agarihai.append(z)
        elif w+1 == x and x+1 == y and ((w-1)%9+1) != 8 and ((w-1)%9+1) != 9:#234東
            agarihai.append(z)
    elif x < 28:
        if w == x and y == z:#22東東
            agarihai.append(w)
            agarihai.append(y)
        elif w+1 == x and y == z and ((w-1)%9+1) != 9:#23東東
            if ((w-1)%9+1) != 1:
                agarihai.append(w-1)
            agarihai.append(x+1)
        elif w+2 == x and y == z and ((w-1)%9+1) != 8 and ((w-1)%9+1) != 9:#24東東
            agarihai.append(w+1)
    elif w < 28:
        if x == y and x == z:#3東東東
            agarihai.append(w)
    else:
        if w == x:#白白
            if w == y:#白白白
                if w == z:##槓子
                    pass
                else:#白白白中
                    agarihai.append(z)
            elif y == z:#白白中中
                agarihai.append(w)
                agarihai.append(z)
        elif x == y and x == z:#中白白白
            agarihai.append(w)    

    return agarihai


###Naki_Judge
def naki_kan_conf(yama, tehai, hai_n):
    tehai_m = tehai[0]
    hai = int(hai_n)
    if tehai_m.count(hai) == 3:
        if yama[-4] == 0:
            print("四槓子聴牌なので槓できない")
        else:
            return True
    return False


def naki_pon_conf(tehai, hai_n):
    tehai_m = tehai[0]
    hai = int(hai_n)
    if tehai_m.count(hai) == 2:
        return True
    return False


def naki_kakan_conf(yama, tehai):
    tehai_m = tehai[0]
    tehai_h = tehai[1]
    for hai in tehai_m:
        if tehai_h.count(int(hai) + 0.1) == 2 and tehai_h.count(int(hai) + 0.3) == 1:
            if yama[-4] == 0:
                print("四槓子聴牌なので槓できない")
            else:
                return True
    return False


def naki_ankan_conf(yama, tehai):
    tehai_m = tehai[0]
    for hai in tehai_m:
        if tehai_m.count(hai) == 4:
            if yama[-4] == 0:
                print("四槓子聴牌なので槓できない")
            else:
                return True
    return False

def naki_c_conf(tehai, hai_n):#チー
    tehai_m = tehai[0]
    hai = int(hai_n)
    if hai > 27:
        return False
    else:
        if (hai % 9) == 1:
            if ((hai + 1) in tehai_m) and ((hai + 2) in tehai_m):
                return True
        if (hai % 9) == 2:
            if ((hai + 1) in tehai_m) and ((hai + 2) in tehai_m):
                return True
            if ((hai - 1) in tehai_m) and ((hai + 1) in tehai_m):
                return True  
        if (hai % 9) >= 3 and (hai % 9) <= 7:
            if ((hai - 1) in tehai_m) and ((hai - 2) in tehai_m):
                return True
            if ((hai - 1) in tehai_m) and ((hai + 1) in tehai_m):
                return True
            if ((hai + 1) in tehai_m) and ((hai + 2) in tehai_m):
                return True
        if (hai % 9) == 8:
            if ((hai - 1) in tehai_m) and ((hai - 2) in tehai_m):
                return True
            if ((hai - 1) in tehai_m) and ((hai + 1) in tehai_m):
                return True
        if (hai % 9) == 0:#9
            if ((hai - 1) in tehai_m) and ((hai - 2) in tehai_m):
                return True
    return False


def naki_c_select(tehai, hai_n):#チー
    tehai_m = tehai[0]
    hai = int(hai_n)
    chi_hai = []
    if hai > 27:
        return False
    else:
        if (hai % 9) == 1:
            if ((hai + 1) in tehai_m) and ((hai + 2) in tehai_m):
                chi_hai.append([hai+1.0, hai+2.0])
        if (hai % 9) == 2:
            if ((hai + 1) in tehai_m) and ((hai + 2) in tehai_m):
                chi_hai.append([hai+1.0, hai+2.0])
            if ((hai - 1) in tehai_m) and ((hai + 1) in tehai_m):
                chi_hai.append([hai-1.0, hai+1.0])
        if (hai % 9) >= 3 and (hai % 9) <= 7:
            if ((hai - 1) in tehai_m) and ((hai - 2) in tehai_m):
                chi_hai.append([hai-2.0, hai-1.0])
            if ((hai - 1) in tehai_m) and ((hai + 1) in tehai_m):
                chi_hai.append([hai-1.0, hai+1.0])
            if ((hai + 1) in tehai_m) and ((hai + 2) in tehai_m):
                chi_hai.append([hai+1.0, hai+2.0])
        if (hai % 9) == 8:
            if ((hai - 1) in tehai_m) and ((hai - 2) in tehai_m):
                chi_hai.append([hai-2.0, hai-1.0])
            if ((hai - 1) in tehai_m) and ((hai + 1) in tehai_m):
                chi_hai.append([hai-1.0, hai+1.0])
        if (hai % 9) == 0:#9
            if ((hai - 1) in tehai_m) and ((hai - 2) in tehai_m):
                chi_hai.append([hai-2.0, hai-1.0])
    return chi_hai


def naki_c_do(tehai, hai_n, turn, all_kawa, num = 0):#チー
    t = (turn[0]+3)%4
    all_kawa[t].append(-all_kawa[t].pop(-1))
    tehai_m = tehai[0]
    hai = int(hai_n)
    try:
        tehai[1].remove(0)
    except:
        pass
    if (hai % 9) == 1:
        if ((hai + 1) in tehai_m) and ((hai + 2) in tehai_m):            
            tehai_m.remove(hai + 1)
            tehai_m.remove(hai + 2)
            tehai[1].extend([hai + 0.3, hai + 1.1, hai + 2.1])
    if (hai % 9) == 2:
        chi = []
        if ((hai + 1) in tehai_m) and ((hai + 2) in tehai_m):
            chi.append(1)
        if ((hai - 1) in tehai_m) and ((hai + 1) in tehai_m):
            chi.append(2)
        j = chi[num]
        if j == 1:
            tehai_m.remove(hai + 1)
            tehai_m.remove(hai + 2)
            tehai[1].extend([hai + 0.3, hai + 1.1, hai + 2.1])
        elif j == 2:
            tehai_m.remove(hai - 1)
            tehai_m.remove(hai + 1)
            tehai[1].extend([hai + 0.3, hai - 0.9, hai + 1.1])           
    if (hai % 9) >= 3 and (hai % 9) <= 7:
        chi = []
        if ((hai - 1) in tehai_m) and ((hai - 2) in tehai_m):
            chi.append(1)
        if ((hai - 1) in tehai_m) and ((hai + 1) in tehai_m):
            chi.append(2)
        if ((hai + 1) in tehai_m) and ((hai + 2) in tehai_m):
            chi.append(3)
        j = chi[num]
        if j == 1:
            tehai_m.remove(hai - 1)
            tehai_m.remove(hai - 2)
            tehai[1].extend([hai + 0.3, hai - 1.9, hai - 0.9])
        elif j == 2:          
            tehai_m.remove(hai - 1)
            tehai_m.remove(hai + 1)
            tehai[1].extend([hai + 0.3, hai - 0.9, hai + 1.1])
        elif j == 3:
            tehai_m.remove(hai + 1)
            tehai_m.remove(hai + 2)
            tehai[1].extend([hai + 0.3, hai + 1.1, hai + 2.1])
    if (hai % 9) == 8:
        chi = []
        if ((hai - 1) in tehai_m) and ((hai - 2) in tehai_m):
            chi.append(1)
        if ((hai - 1) in tehai_m) and ((hai + 1) in tehai_m):
            chi.append(2)
        j = chi[num]   
        if j == 1:
            tehai_m.remove(hai - 1)
            tehai_m.remove(hai - 2)
            tehai[1].extend([hai + 0.3, hai - 1.9, hai - 0.9])
        elif j == 2:
            tehai_m.remove(hai - 1)
            tehai_m.remove(hai + 1)
            tehai[1].extend([hai + 0.3, hai - 0.9, hai + 1.1])
    if (hai % 9) == 0:#9
        if ((hai - 1) in tehai_m) and ((hai - 2) in tehai_m):
            tehai_m.remove(hai - 1)
            tehai_m.remove(hai - 2)
            tehai[1].extend([hai + 0.3, hai - 1.9, hai - 0.9])


def naki_p_do(tehai, hai_n, turn, p_kaze, all_kawa):#ポン
    tehai_m = tehai[0]
    t = (turn[0]+3)%4
    all_kawa[t].append(-all_kawa[t].pop(-1))
    hai = int(hai_n)

    try:
        tehai[1].remove(0)
    except:
        pass
    for i in range(2):
        tehai_m.remove(hai)
    if turn[0] == p_kaze[0]:#下家
        tehai[1].extend([hai + 0.3, hai + 0.1, hai + 0.1])
    if (turn[0]+1)%4 == p_kaze[0]:#対面
        tehai[1].extend([hai + 0.1, hai + 0.3, hai + 0.1])
    if (turn[0]+2)%4 == p_kaze[0]:#上家
        tehai[1].extend([hai + 0.1, hai + 0.1, hai + 0.3])


def naki_k_do(yama, tehai, hai_n, turn, p_kaze, all_kawa, dora, ura_dora):#カン
    tehai_m = tehai[0]
    t = (turn[0]+3)%4
    all_kawa[t].append(-all_kawa[t].pop(-1))
    tehai_m.sort()
    for i in range(1, 5):
        if yama[-i] != 0:
            tehai_m.append(yama.pop(-i))
            break
    yama.append(0)
    yama.pop(-15)#槓したときに山から王牌に移動させるやつ
    hai = int(hai_n)
    dora.append(yama[-(len(dora)+5)])
    ura_dora.append(yama[-(len(dora)+9)])

    try:
        tehai[1].remove(0)
    except:
        pass
    for _ in range(3):
        tehai_m.remove(hai)
    if turn[0] == p_kaze[0]:#下家
        tehai[1].extend([100 + hai + 0.3, 100 + hai + 0.1, 100 + hai + 0.1, 100 + hai + 0.1])
    if (turn[0]+1)%4 == p_kaze[0]:#対面
        tehai[1].extend([100 + hai + 0.1, 100 + hai + 0.3, 100 + hai + 0.1, 100 + hai + 0.1])
    if (turn[0]+2)%4 == p_kaze[0]:#上家
        tehai[1].extend([100 + hai + 0.1, 100 + hai + 0.1, 100 + hai + 0.1, 100 + hai + 0.3])


def naki_kakan_do(yama, tehai, dora, ura_dora):
    tehai_m = tehai[0]
    tehai_h = tehai[1]
    hai_n = 0
    for hai in tehai_m:
        if tehai_h.count(int(hai) + 0.1) == 2 and tehai_h.count(int(hai) + 0.3) == 1:
            hai_n = int(hai)
            break
    tehai_m.sort()
    for i in range(1, 5):
        if yama[-i] != 0:
            tehai_m.append(yama.pop(-i))
            break
    yama.append(0)
    yama.pop(-15)#槓したときに山から王牌に移動させるやつ
    dora.append(yama[-(len(dora)+5)])
    ura_dora.append(yama[-(len(dora)+9)])

    
    l = tehai_h.index(hai_n + 0.3)
    tehai_m.remove(hai)
    tehai_h.insert(l,hai_n + 0.3)
    for i in range(len(tehai_h)):
        if int(tehai_h[i]) == hai_n:
            tehai_h[i] = tehai_h[i] + 100


def naki_ankan_do(yama, tehai, dora, ura_dora):
    tehai_m = tehai[0]
    tehai_h = tehai[1]
    for hai in tehai_m:
        if tehai_m.count(hai) == 4:
            hai_n = int(hai)
            break
    tehai_m.sort()
    for i in range(1, 5):
        if yama[-i] != 0:
            tehai_m.append(yama.pop(-i))
            break
    yama.append(0)
    yama.pop(-15)#槓したときに山から王牌に移動させるやつ
    dora.append(yama[-(len(dora)+5)])
    ura_dora.append(yama[-(len(dora)+9)])

    try:
        tehai[1].remove(0)
    except:
        pass

    tehai_h.extend([100.1, 100 + hai_n + 0.1, 100 + hai_n + 0.1, 100.1])
    for _ in range(4):
        tehai_m.remove(hai)



    