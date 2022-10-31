# 1 - Rolar dado de D4
# 2 - Rolar dado de D6
# 3 - Rolar dado de D8
# 4 - Rolar dado de D10
# 5 - Rolar dado de D12
# 6 - Rolar dado de D20

import random

print('Seja Bem Vindo ao Rola Dado!')
print('Escolha uma opção de dados de RPG que você gostaria de rolar!')
opcaoDado = int(input('Opções: (1) - D4, (2) - D6, (3) - D8, (4) - D10, (5) - D12, (6) - D20: '))

if opcaoDado == 1:
    print('Seu resultado é: ', random.randrange(1, 4), '!')
elif opcaoDado == 2:
    print('Seu resultado é: ', random.randrange(1, 6), '!')
elif opcaoDado == 3:
    print('Seu resultado é: ', random.randrange(1, 8), '!')
elif opcaoDado == 4:
    print('Seu resultado é: ', random.randrange(1, 10), '!')
elif opcaoDado == 5:
    print('Seu resultado é: ', random.randrange(1, 12), '!')
elif opcaoDado == 6:
    print('Seu resultado é: ', random.randrange(1, 20), '!')
else:
    print('Opção inválida!')
