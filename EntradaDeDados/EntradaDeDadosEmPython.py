salario01: float; salario02: float
nome01: str; nome02: str
idade: int
sexo: str

nome01 = input("Nome da primeira pessoa: ")
salario01 = float(input("Salario da primeira pessoa: "))

nome02 = input("Nome da segunda pessoa: ")
salario02 = float(input("Salario da segunda pessoa: "))

idade = int(input("Digite uma idade: "))
sexo = input("Digite um sexo(F/M): ")

print(f"Nome da primeira pessoa he: {nome01} e o nome da segunda pessoa eh: {nome02}, os salarios de cada um sao: "
      f"{salario01} e {salario02}, a idade eh: {idade} e o sexo eh: {sexo} ")