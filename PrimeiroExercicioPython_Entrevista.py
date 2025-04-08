#Pega input usuário
nome= input("Qual o seu nome?")
idade = input("Qual sua idade?")

#Conversor idade
idadeFuturo = int(idade) + 6

#Exibe resultados do código
print("Seu nome é : " + nome)
print("Seu nome tem: " + str(len(nome)) + " letras !")
print("Daqui a 6 anos voce tera:" + str(idadeFuturo) + "anos!" )