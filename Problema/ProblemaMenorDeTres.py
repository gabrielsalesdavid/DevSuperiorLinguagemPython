num01 = int(input("Primeiro valor: "))
num02 = int(input("Segundo valor: "))
num03 = int(input("Terceiro valor: "))

if num01 < num02 and num01 < num03:
  menorDeTres = num01
elif num02 < num03:
    menorDeTres = num02
else:
    menorDeTres = num03

print(f"Menor = {menorDeTres}")