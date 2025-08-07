# tugas bang dea

# saldo_awal = input('berapa saldo awalmu: ')
# deposit = input('mau deposit berapa? ')
#
# # munculkan output ke terminal hasil setelah saldo awal ditambahkan dengan deposit
#
# saldo_akhir = int(saldo_awal) + int(deposit)
# print('saldo akhir: ' + str(saldo_akhir))

# pekondisian
usia = int(input('kamu umur berapa? '))

if usia >= 0 and usia <= 2:
    print('batita')
elif usia >= 3 and usia <= 4:
    print('balita')
elif usia >= 5 and usia <= 12:
    print('anak-anak')
elif usia >= 13 and usia <= 18:
    print('remaja')
elif usia >= 18 and usia <= 30:
    print('dewasa')
elif usia >= 30 and usia <= 60:
    print('orang tua')
else:
    print('bau tanah jir')