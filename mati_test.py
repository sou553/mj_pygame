import judge as jdg
import tiles as tls


tehai =[[3,3,3,4,4,5,5,29,29,29,30,30,30], [0]]
tehai[0].sort()

tehai_num = [[], [0]]
tehai_ans = []

for i in tehai[0]:
    s = tls.hai_name(i)
    tehai_num[0].append(s)

print(tehai_num)

for i in (jdg.mati(tehai)):
    s = tls.hai_name(i)
    tehai_ans.append(s)

print(tehai_ans)