import random
def gen(b):
    a = b.upper()
    if len(a)!=6 or a.isalpha()==False:
        return ('Error!')
    result = ''
    alph = ''
    alphn = ''
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',\
                'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for i in range(len(a)):
        if a[i] not in alph:
            alph += a[i]
        else:
            continue
    for i in range(3):
        result += random.choice(alph)
    result += '-'
    for i in range(6):
        number = str((alphabet.index(a[i])+1) % 10)
        if number not in alphn:
            alphn += number
    for i in range(3):
        result += random.choice(alphn)
    result += '-'
    for i in range(3):
        result += random.choice(alph)
    return result
