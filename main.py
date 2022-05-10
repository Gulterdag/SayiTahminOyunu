import random
sayi = random.randint(1,100)
hak=5
while hak>0:
  tahmin = int(input("Tahmininizi giriniz:"))
  hak -= 1
  if tahmin == sayi:
    print("Tebrikler sayıyı tahmin ettiniz.")
    break
  elif tahmin > sayi:
    print ("Daha küçük bir sayı tahmini yapınız  Kalan Hak:{}".format(hak))
  elif tahmin < sayi:
    print ("Daha büyük bir sayı tahmini yapınız  Kalan Hak:{}".format(hak))
else:
    print ("Oyun Bitti " + "Kaybettin Dostum")