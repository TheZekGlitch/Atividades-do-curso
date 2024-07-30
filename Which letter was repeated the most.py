frase = input("Digite uma frase: ")
contagem = len(frase)

i = 0
letra_mais_apareceu = ''

while i < contagem:

    letra_atual = frase[i]
    quantas_vezes_ap = frase.count(letra_atual)
    print(letra_atual, quantas_vezes_ap)
    i += 1
