numero = 0
case1 = 0
case2 = 0
case3 = 0
case4 = 0

while numero >= 0:
    numero = int(input("Digite um numero: "))

    if numero >= 0:
      if numero <= 25:
         case1 += 1
      else:
          if numero <= 50:
              case2 += 1
          else:
              if numero <= 75:
                  case3 += 1
              else:
                  if numero <= 100:
                      case4 += 1

print("Quantidade de numeros digitados entre 0 e 25: ", case1)                               
print("Quantidade de numeros digitados entre 26 e 50: ", case2)                               
print("Quantidade de numeros digitados entre 51 e 75: ", case3)                               
print("Quantidade de numeros digitados entre 76 e 100: ", case4)                               

