
sayac = 0
print('dizinin boyutu kaç')
boyut = int(input())
dizi = [""] * (boyut)

#dizi oluşturma
for i in range (0, boyut - 1 + 1, 1):
    dizi[i] = input()
for i in range(0, boyut - 1 + 1, 1):
    
    for a in range(i+1, boyut -1 +1, 1):
        
        if ord(dizi[i][0]) > ord(dizi[a][0]):
                bos= dizi[i]
                dizi[i] = dizi[a]
                dizi[a] = bos
               
        else:

            while ord(dizi[i][sayac]) == ord(dizi[a][sayac]):
                sayac = sayac + 1
                
                if ord(dizi[i][sayac]) > ord(dizi[a][sayac]):
                    bos = dizi[i]
                    dizi[i] = dizi[a]
                    dizi[a] = bos
                    
            sayac = 0

    print(dizi[i])
    
