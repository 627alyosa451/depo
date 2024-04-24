while True:
    sayı = input('Sayı giriniz (q ile çıkış yapabilirsiniz): ')

    if sayı.lower() == 'q':
        print('Programdan çıkılıyor...')
        break

    try:
        sayı = float(sayı)
        if sayı % 2 == 0:
            print('Çift sayı')
        elif sayı % 2 == 1:
            print('Tek sayı')
        else:
            print('Teklik ya da çiftlik aranmaz')
    except ValueError:
        print('Geçersiz giriş! Bir sayı girmelisiniz.')
