# Mavzu: Lug'atlar bilan ishlash

# talaba = {
#     'name': 'Abdullajon',
#     'yoshi': '14',
#     'maktab': '2',
#     'sinf': '8'
# }
# print(f"Mening ismim {talaba['name']} yoshim {talaba['yoshi']} da. Men {talaba['maktab']} - maktabning {talaba['sinf']} - sinifida da o'qiyman.")
# talab = talaba.items()
# for kalit, qiymat in talaba.items():
#     # print(f"{kalit}" )
#     print(f"{qiymat}" )

# ombor = {
#     'olma': 10000,
#     'banan': 21000,
#     'uzum': 18000,
#     'kola': 16000,
#     'anor': 25000,
#     'fanta': 18000
# }
# print(ombor.items())
# print(ombor.keys())
# print(ombor.values())
# ombor['banan']
# print(f"Do'kondagi maxsulotlar: ")
# Vazifa: Bozorlini avtomatlashtirish, user istagan maxsulotini kritsin
# bozorlik = ['uzum', 'nok', 'kola']
# for mahsulot in ombor:
#     if mahsulot.lower() in bozorlik:
#         print(f"{mahsulot.title()} - {ombor[mahsulot]} so'm.")
# for omborda_yogi in bozorlik:
#     if omborda_yogi not in ombor:
#         print(f"Iltimos, do'koningizga {omborda_yogi} ni ham olib kelsangiz.")

# print(f"Do'kondagi maxsulotlar: ")
# for mahsulot in sorted(ombor):
#     print(mahsulot.title())
    
# ***** NESTING ******

# car_0 = {
#     'model': 'lacetti',
#     'rang': 'oq',
#     'yil': 2015,
#     'narh': 130000,
#     'km':5000,
#     'karopka': 'avtomat'
# }
# car_1 = {
#     'model': 'Jentra',
#     'rang': 'qora',
#     'yil': 2019,
#     'narh': 180000,
#     'km':6000,
#     'karopka': 'mexanika'
# }
# car_2 = {
#     'model': 'Nexia_3',
#     'rang': 'qizil',
#     'yil': 2020,
#     'narh': 151000,
#     'km':3000,
#     'karopka': 'avtomat'
# }
# car = car_0
# print(f"{car['model'].title()},"
#       f"{car['rang']} rang "
#       f"{car['yil']} - yil, {car['narh']} $")

# car_0['rang'] = 'qora'
# cars = [car_0, car_1, car_2]
# for car in cars:
#     print(f"{car['model'].title()},"
#       f"{car['rang']} rang "
#       f"{car['yil']} - yil, {car['narh']} $")
    
dasturchilar = {
    'abdullajon': ['pyhton','c','html','css'],
    'otabek': ['pyhton','c','html','css','photoshop'],
    'ahmadjon': ['pyhton','c','html','css','photoshop','unitiy']
}
# print(dasturchilar.items()) 
for ism, tillar in dasturchilar.items():
    print(f"\n {ism.title()} quydagi dasturlash tillarini biladi: ")
    for til in tillar:
        print(til.upper())

# for ism, tillar in dasturchilar.items():
#     print(f"\n {ism.title()} quydagi dasturlash tillarini biladi: ")
#     for til in tillar:
#         print(f"{til.upper()}" , end =' ')