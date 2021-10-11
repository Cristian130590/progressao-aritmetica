#crie um programa que leia o primeiro termo e a razao de uma PA,no final mostre os 10 primeiros termos dessa progressao.

primeiro = int(input('primeiro termo '))
razao = int(input('razao'))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo+razao, razao):
    print('{} '.format(c), end='-> ')
print(' ACABOU ')
