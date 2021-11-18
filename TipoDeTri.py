import random
random.seed()

L1 = random.randint(1,3)
L2 = random.randint(1,3)
L3 = random.randint(1,3)
if L1!=L2!=L3:
    print('el Triangulo es Escaleno')
elif L1!=L2==L3:
    print('el Triangulo es Isosceles')
elif L1==L2==L3:
    print('el Triangulo es Equilatero')
else:
    print('numero de lados no validos')
while L1 < 3:
    print()

