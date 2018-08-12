juros = float(input("Qual a taxa de juros %: "))
capital = float(input("Qual o valor desejado R$: "))
meses = int(input("Quantidade de parcelas: "))
for i in range (0,meses):
    i = i+1
    capital = capital + (capital*(juros/100))
    print(i,"º", "mês", "R$", capital)   
    