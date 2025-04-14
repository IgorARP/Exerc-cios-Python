usuario = input("Digite seu nome de usuário") == "igor"
senha = input("Digite sua senha") == "arroz"
if usuario and senha:
    print("Acesso Liberado seja Bem Vindo")

if usuario and not senha:
    print("Senha incorreta por favor tentar novamente ")

else:
    print("Usuario incorreto")