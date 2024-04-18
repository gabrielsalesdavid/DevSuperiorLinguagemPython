import math

base: float
altura: float
area: float
perimetro: float
diagonal: float

base = float(input("Base do retangulo: "))
altura = float(input("Altura do retangulo: "))

area = base * altura
perimetro = 2 * (base + altura)
diagonal = math.sqrt(pow(base, 2.0) + pow(altura, 2.0))

print()
print(f"Area = {area:.4f}")
print(f"Perimetro = {perimetro:.4f}")
print(f"Diagonal  = {diagonal:.4f}")
