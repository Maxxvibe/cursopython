somatoria = 0 
quantidade = 0 
temperatura = 0

while temperatura != 999:
    temperatura = float(input("Digite a temperatura ou 99 para sair: "))

    if temperatura != 999:
        somatoria += temperatura
        quantidade += 1

media = somatoria / quantidade
print ("A media das temperaturas digitadas é: ", media,"º")        