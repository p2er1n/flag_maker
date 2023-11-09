import random
import string

ori = input("input: ")

mapping = {
    'a': ['4', '@'],
    'e': ['3'],
    'l': ['1'],
    '1': ['l', '!'],
    's': ['5', '4'],
    '!': ['1', 'l'],
}

for c in string.ascii_letters:
    if c not in mapping:
        if c.islower():
            mapping[c] = [c.upper(), c]
        elif c.isupper():
            mapping[c] = [c.lower(), c]
    else:
        mapping[c].append(c)
        if c.islower():
            mapping[c].append(c.upper())
        elif c.isupper():
            mapping[c].append(c.lower())

edi = [c for c in ori]

round_num = int(input('round: '))
old_round_num = round_num
while round_num > 0:
    random.seed()
    cnt = random.randrange(len(ori))
    for i in range(len(edi)):
        if edi[i] in mapping and cnt > 0:
            if random.randrange(100) > 50:
                edi[i] = mapping[edi[i]][random.randrange(len(mapping[edi[i]]))]
                cnt -= 1
                
    cnt = random.randrange(int(len(ori)/5))
    for i in range(len(edi)-1):
        if edi[i] == '_' or edi[i + 1] == '_':
            continue
        if cnt > 0:
            if random.randrange(100) > 90 + (1-round_num/old_round_num)*10:
                edi[i], edi[i+1] = edi[i+1], edi[i]
                cnt -= 1
    round_num -= 1

print("".join(edi))
    

