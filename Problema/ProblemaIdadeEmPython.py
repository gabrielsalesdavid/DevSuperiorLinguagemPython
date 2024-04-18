nome01: str
nome02: str
idade01: int
idade02: int
media: float

print("Dados da primeira pessoa: ")
nome01 = input("Nome: ")
idade01 = int(input("Idade: "))

print("Dados da segunda pessoa: ")
nome02 = input("Nome: ")
idade02 = int(input("Idade: "))

media = (idade01 + idade02) / 2.0;

print(f"A idade media de {nome01} e {nome02} eh de {media:.1f} anos")