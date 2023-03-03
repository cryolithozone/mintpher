# 65..90 - capital, 97..122 - small

import math as m

# This is literally not going to be decodable LMFAO
def CharTransform(ch):
    oldnum = ord(ch)
    num = ord(ch)

    # Putting the poor sopping wet character through the wringer
    num = m.tan(m.cos(num * m.sqrt(num)) - m.sqrt(num))
    num = m.ceil(m.fabs(num) * 19)
    num = m.lcm(num, oldnum + 23)
    num = num * m.sqrt(oldnum)
    num = (num - m.trunc(num)) * 100

    # Making sure the character fits 65-90 and 97-122 bounds
    flg = False
    temp = (m.sqrt(num) - m.floor(m.sqrt(num))) * 100
    if temp < 1:
        temp += oldnum % 10
    if temp == 0:
        temp = m.fabs(m.cos(m.tan(m.sin(oldnum))) * 10)
    while not flg:
        if (65 > num) or ((90 < num) and (num < 97)):
            num += m.floor(temp)
        elif (num > 123):
            num -= m.ceil(temp)
        else:
            flg = True

    num = m.floor(num)

    return chr(num);

# God.
def Encode(a):
    answer = [];
    for ch in a:
        if (ch == ' '):
            answer.append(ch)
        else:
            answer.append(CharTransform(ch))

    return "".join(answer);

# help
a = input("input string: ")
result = Encode(a)
print(result)