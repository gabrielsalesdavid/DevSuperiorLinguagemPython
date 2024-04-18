print("Digite dois numeros: ")
num01 = int(input())
num02 = int(input())

while num01 != num02:
     if num01 < num02:
       print("Crescente!")
     else:
          print("Decrescente!")
     print("Digite outros dois numeros: ")
     num01 = int(input())
     num02 = int(input())