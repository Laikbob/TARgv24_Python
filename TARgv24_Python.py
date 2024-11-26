# from math import pi
# from msilib import PID_LASTPRINTED
# from random import *  #*-kõik funksionid
# from math import * #pi kasutaminseks
import math


# # # #Ülesanene 1
# # # print("Tere tulemast!")
# # # nimi=input("Mis on sinu nimi? "). capitalize() #lower()-aaa, upper()-AAA,capitalize()-Aaa
# # # print("Tere tulemast! Tevitan sind ", nimi)
# # # print("Tere tulemast! Tevitan sind "+ nimi)
# # # vanus=int(input("Kui vana sa oled? "))
# # # print("Tere tulemast! Tervitan sind  "+nimi+"Sa oled",vanus,"aastat vana")
# # # print(f"\tTere tulemast! \nTervitan sind {nimi} Sa oled {vanus} aastat vana")

# # # # Ülesanne 2
# # # vanus = 18
# # # eesnimi = "Jaak"
# # # pikkus = 16.5
# # # kas_käib_koolis = True
# # # print(type(vanus),(eesnimi),(pikkus))

# # # #Ülesanne 3
# # # kokku=randint(1,1000)
# # # print(f"Kokku on {kokku} kommi")
# # # kommi=int(input("Mitu kommi sa tahad? "))
# # # kokku=kokku-kommi
# # # print(f"Jääk on {kokku} kommi")

# # #Ülesanne 4
# print("Labimöödu leidmine ")
# #l-ümbbermõõt
# l=float(input("Ümbermööt: "))
# d=l/pi
# print(f"Läbimõõdu suurus on {round(d,2)}")

# # Ülesanne 5
# N = float(input("Sisestage ristküliku laius (N): "))
# M = float(input("Sisestage ristküliku kõrgus (M): "))
# diagonaal = math.sqrt(N**2 + M**2)
# print(f"Ristküliku diagonaal on {diagonaal:.2f} ühikut.")

# # Üleasnne 6
# aeg = float(input("Mitu tundi kulus sõiduks? "))
# teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
# kiirus = teepikkus / aeg  # Parandatud valem
# print(f"Sinu kiirus oli {kiirus:.2f} km/h")

# # Üleasnne 7
# numbrid = []
# for i in range(5):
#     arv = int(input(f"Sisestage arv {i+1}: "))
#     numbrid.append(arv)
# keskmine = sum(numbrid) / len(numbrid)
# print(f"Nende arvude aritmeetiline keskmine on {keskmine:.2f}")

# # Üleasnne 8
# print("   @..@")
# print("  (----)")
# print(" ( \\__/ )")
# print('^^ "" ^^')

# # Üleasnne 9 
# a = int(input("Sisestage kolmnurga esimese külje pikkus: "))
# b = int(input("Sisestage kolmnurga teise külje pikkus: "))
# c = int(input("Sisestage kolmnurga kolmanda külje pikkus: "))
# P = a + b + c
# print(f"Kolmnurga ümbermõõt on {P}")
