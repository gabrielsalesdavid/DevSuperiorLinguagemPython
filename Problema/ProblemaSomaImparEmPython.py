print("Digite dois numeros: ")
num01 = int(input())
num02 = int(input())

if num01 > num02:
    troca = num01
    num01 = num02
    num02 = troca

soma = 0
for i in range(num01 + 1, num02):
   if i % 2 != 0:
     soma += i

print(f"Soma dos impares = {soma}")