clientes = [
    ("ana", "xxx", "xxx@email.com"),
    ("joao", "xxx", "xxx@gmail.com")
]

for cliente in clientes:
    nome = cliente[0]
    cpf = cliente[1]
    email = cliente[2]
    print(f"cliente: {nome}\nCPF {cpf}\nEmail {email}\n")

    for nome,cpf,email in clientes:
        print(f"cliente: {nome}\nCPF: {cpf}\nEmail: {email}\n")



for n in range(-5,6):
    if n == 0:
        continue
    resultado = 1/n
    print(f"o resultado é: {resultado}")


while True:
    entrada = input("Digite qualquer coisa(q para sair)")
    print(f"O valor digitado é {entrada}")
    if entrada == "q":
        break