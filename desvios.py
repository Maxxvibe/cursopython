#exercicio 1
#numero = int(input("Digite um numero: "))

#if numero >= 100 and numero <=200:
 #    print("Numero esta entre 100 e 200!")

#else:
 #   print("Numero não esta entre 100 e 200!")    

#exercicio 2
nome = input("Digite seu nome: ")

notapt = float(input("Nota de portugues: "))
notamat = float(input("Nota de matematica: "))
notageo = float(input("Nota de geografia: "))

media = (notapt + notamat + notageo)/3

if media >= 7:
   print(nome, "Aprovado!")
else:
    if media < 5:
      print(nome, "Reprovado!")
    else:
      print(nome, "Recuperação")  
        



