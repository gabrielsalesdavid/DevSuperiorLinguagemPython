num: int

num = int(input("Digite um numero: "))

while (num != 0) :
  if num % 2 != 0:
    print("Impar!")
  else:
      print("Par!")

  num = int(input("Digite outro numero: "))