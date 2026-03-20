nome_pessoa = input("insira seu nome")
idade_pessoas = int(input("insira sua idade"))
while True:
    if idade > 120 or idade < 0:
        idade_pessoas = int(input("insira sua idade"))
    else: 
        break 
        
dias_vida = idade_pessoas * 365 
print(f"Olá {nome}, você ja viveu cerca de: {dias_de_vida}")