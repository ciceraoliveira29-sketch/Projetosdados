nome = input('Digite seu nome:')
print('Ola,'+ nome + '!')

idade = int(input('Digite sua idade:'))
if (idade >= 18):
    print('Você e maior de idade.')
else:
    print('Você e menor de idade.')

for i in range(1,idade + 1):
    print(i)

