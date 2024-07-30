palavra = "secret"
npalavra = "******"
newstring = ''
inpt_acertos = ""

contagempalavra = len(palavra)

i = 0

inpt = input("Digite uma letra: ")

while True:
    if inpt in palavra:
    
        inpt_acertos += inpt

    palavra_formada = ''
    
    for letra_secreta in palavra:
        if letra_secreta in inpt_acertos:
            print(letra_secreta)
            palavra_formada += letra_secreta
        else:
            print("*")
