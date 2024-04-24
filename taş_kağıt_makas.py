import random

while True:
    player = input('taş kağıt makas? ').lower().strip()
    num = random.randint(0, 2)

    if num == 0:
        print('taş')
    elif num == 1:
        print('kağıt')
    elif num == 2:
        print('makas')

    if player == 'taş':
        if num == 0:
            print('Berabere')
        elif num == 1:
            print('Kaybettin')
        elif num == 2:
            print('Kazandın')
    elif player == 'kağıt':
        if num == 0:
            print('Kazandın')
        elif num == 1:
            print('Berabere')
        elif num == 2:
            print('Kaybettin')
    elif player == 'makas':
        if num == 0:
            print('Kaybettin')
        elif num == 1:
            print('Kazandın')
        elif num == 2:
            print('Berabere')
    else:
        print('Geçersiz bir seçenek girdiniz.')
