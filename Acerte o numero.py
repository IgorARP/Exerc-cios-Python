import random

numeroSecreto = random.randint(1,10)
descobriu = False

for n in range(3):
    if not descobriu:
        chute = int(input("Descubra o numero"))
        if chute < numeroSecreto:
            print("Chute baixo")
        elif chute > numeroSecreto:
            print("Chute alto")
        else:
            descobriu = True

if descobriu:
    print("Parabens")

else:
    print(f"Que pena o numero secreto era {numeroSecreto}")