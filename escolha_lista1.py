import random
p1 = input('Digite o nome da pessoa 1: ')
p2 = input('Digite o nome da pessoa 2: ')
p3 = input('Digite o nome da pessoa 3: ')
p4 = input('Digite o nome da pessoa 4: ')
lista = [p1, p2, p3,p4]
sorteio = random.shuffle(lista)
print(lista)
