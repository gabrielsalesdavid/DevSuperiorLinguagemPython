num01: int; num02: int; num03: int; menorDeTres: int

num01 = int(input("Digite o prrimeiro valor: "))
num02 = int(input("Digite o segundo valor: "))
num03 = int(input("Digite o terceiro valor: "))

if num01 < num02 and num01 < num03:
  menorDeTres = num01
elif num02 < num03:
    menorDeTres = num02
else:
    menorDeTres = num03

print(f"O menor eh: {menorDeTres}")