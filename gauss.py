başlangıç = int(input('Başlangıç sayısını girin: ') )
artış_miktarı = int(input('Artış miktarını girin: '))
son = int(input('Son sayıyı girin: '))
total = 0
for number in range(başlangıç, son + 1, artış_miktarı):
    total += number
    print(total)
