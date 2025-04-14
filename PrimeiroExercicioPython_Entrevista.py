#Pega input usuário
nome= input("Qual o seu nome?")
idade = input("Qual sua idade?")

#Conversor idade
idadeFuturo = int(idade) + 5

#Exibe resultados do código
print(f"Seu nome é : {nome}")
print(f"Seu nome tem:  {(len(nome))} letras !")
print(f"Daqui a 5 anos voce tera: {(int(idade) + 5)}anos!" )