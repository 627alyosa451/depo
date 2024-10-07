MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
# HER TEKRARDA YENİDEN PARA İSTİYOR MU?
# PARAYI KONTROL EDECEK FONKSİYON EKSİK

kullanici_parasi = 0
def para_yukle(mevcut_para = 0):
    penny = float(input("kaç tane penny var?"))
    dime = float(input("kaç tane dime var"))
    nickel = float(input("kaç tane nickel var"))
    quarter = float(input("kaç tane quarter var"))
    kullanici_parasi = (penny * 0.01) + (dime * 0.10) + (nickel * 0.05) + (quarter * 0.25) + mevcut_para
    return kullanici_parasi

while True:

    kalan_su = resources["water"]
    kalan_sut = resources["milk"]
    kalan_kahve = resources["coffee"]

    secim = input(f"What would you like to drink? (espresso/latte/cappuccino)\nmevcut paranız = {kullanici_parasi}\n")
    if secim == "no":
        break
    if secim == "espresso" or secim =="latte" or secim =="cappuccino":
        malzemeler = MENU[secim]["ingredients"]
        su = malzemeler["water"]
        sut = malzemeler["milk"]
        kahve = malzemeler["coffee"]

        if kullanici_parasi < MENU[secim]["cost"]:
            print("Lütfen para atın")
            kullanici_parasi = para_yukle(kullanici_parasi)

    elif secim == "report":
        print(f"kalan su = {kalan_su}\nkalan süt = {kalan_sut}\nkalan kahve = {kalan_kahve}\nkalan para = {kullanici_parasi}$ ")
        continue
    else:
        print("Lütfen geçerli bir isim giriniz")
        continue

    if kullanici_parasi >= MENU[secim]["cost"]:
        kullanici_parasi -= MENU[secim]["cost"]
        print(f"kalan paranız = {round(kullanici_parasi,2)}")
        if kalan_su > su and kalan_sut > sut and kalan_kahve > kahve:
            resources["water"] = kalan_su - su
            resources["milk"] = kalan_sut - sut
            resources["coffee"] = kalan_kahve - kahve
            print(resources)
        else:
            print("Yeterli malzeme yok")
            break
    else:
        print("yetersiz para.")
        continue

