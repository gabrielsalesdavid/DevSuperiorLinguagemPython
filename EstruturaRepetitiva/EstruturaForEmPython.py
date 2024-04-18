x: int
soma: int

n = int(input("Quantos numeors serao ddigitados? "))

soma = 0
for i in range (0, n):
   x = int(input("Digite um numero: "))
   soma += x

print("Soma = ", soma)