
harfler = "abcçdefgğhıijklmnoöprsştuüvyz"
çevrim = {i: harfler.index(i) for i in harfler}

isimler = ["ahmet", "abmet", "ışık", "ismail", "çiğdem",
           "can", "şule", "iskender"]

print(sorted(isimler, key=lambda x: çevrim.get(x[0])))

# Dışarıdan yazımızı giriyoruz. Yazımızı enter tuşuna basmadan girmeliyiz en son bitiminde enter'a basmalıyız.
yazi = input("Bir yazı giriniz:")
# Kelimeleri bir liste içine parçalamak için aşağıdaki kodu giriyoruz.
kelimeler = yazi.split()
# Bu kod ile kelimeleri sıralıyoruz.
kelimeler.sort()
# Sonunda ise ekrana print kodu ile yazdırıyoruz.
print("Alfabetik sırayla dizilen kelimeler : ")
for sirala in kelimeler:
print(sirala)