# count = 0
# while count < 10:
#     print(count)
#     count += 1

# range(qtd)
# print(list(range(10)))

# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in range(10, 0, -1):
#     print(i)
# -----------------------------------------------------
# 1. Utilizando for imprima 10 vezes a mensagem "hello world" na tela

# for i in range(10):
#     print('Hello World')

# 2. Utilizando for imprima uma sequencia de 0 a 100

# for i in range(101):
#     print(i)

# 3. Utilizando for imprima uma sequencia de 0 até um número digitado pelo usuário

# valor = int(input('Digite um valor: '))
#
# for i in range(valor):
#     print(i)

# 4. Utilizando for imprima todos os números pares de 0 a 100

# for i in range(101):
#     if i % 2 == 0:
#         print(i)

# 5. Utilizando for imprima todos os pares de 0 até o número digitado pelo usuário

# valor = int(input('Digite um valor: '))
# for i in range(valor + 1):
#     if i % 2 == 0:
#         print(i)

# 6. Utilizando for leia 10 números,
# se este número for par imprima "este número é par"
# se este número for ímpar imprima "este número é ímpar"

# for i in range(10):
#     valor = int(input('Digite um valor: '))
#     if i % 2 == 0:
#         print(f'Esse número é Par!!!')
#     else:
#         print(f'Esse número é Impar!!!')

# 7. Utilizando for leia 10 números e ao final imprima a quantidade de pares e a quantidade de ímpares

# qtdPares = 0
# qtdImpares = 0
# for i in range(11):
#     valor = int(input('Digite um valor: '))
#     if i % 2 == 0:
#         qtdPares += 1
#     else:
#         qtdImpares += 1
# print(f'Quantidade de numeros pares: {qtdPares}')
# print(f'Quantidade de numeros impares: {qtdImpares}')

# ---------------------------------------------------------------------------


'''
Sintaxe de uma função
def nomeDaFuncao():
    <codigo>

Como executar/chamar uma função?
nomeDaFuncao()
'''
# def autenticar():
#     senha = input('Digite a senha: ')
#     if senha == '123':
#         print('ok')
#     else:
#         print('dados inválidos')
#
# # pix
# autenticar()
#
# #recarga
# autenticar()
#
# -------------------------------------------------------------
# 1. Escreva uma função que leia dois números e imprima a soma dos dois

# def somar():
#     valor01 = int(input('digite o primeiro valor: '))
#     valor02 = int(input('digite o segundo valor: '))
#     resultado = valor01 + valor02
#     print(f'Resultado é: {resultado}')
# somar()

# 2. Escreva uma função que leia base e altura de um triangulo e imprima a sua área
# area = base * altura / 2

# def areaDoTriangulo():
#     altura = float(input('Digite a altura: '))
#     base = float(input('Digite a base: '))
#     area = base * altura / 2
#     print(f'Area do triangulo: {area}')
# areaDoTriangulo()

# 3. Escreva uma função que leia peso e altura de uma pessoa a imprima o seu IMC
# imc = peso / altura ** 2

# def imc():
#     peso = float(input("Digite seu peso: "))
#     altura = float(input('Digite sua altura: '))
#     IMC = peso / altura ** 2
#     print(IMC)
# imc()

# 4. Escreva uma função que leia dois números e imprima o maior

# def maiorOuMenorValor():
#     valor01 = float(input('Digite o primeiro valor: '))
#     valor02 = float(input('Digite o segundo valor: '))
#     if valor01 > valor02:
#         print(f'{valor01} Este é o maior Valor')
#     elif valor02 > valor01:
#         print(f'{valor02} Este é o maior Valor')
#     else:
#         print('Numeros iguais')
# maiorOuMenorValor()

# 5. Escreva uma função que leia 3 notas,
# calcule a média e se a média for maior ou igual a 6 imprima "você esta aprovado"
# senão imprima "você está de recuperação"

# def resultProva():
#     nota01 = float(input('Primeira nota: '))
#     nota02 = float(input('segunda nota: '))
#     nota03 = float(input('terceira nota: '))
#     media = (nota01 + nota02 + nota03) / 3
#     if media >= 6:
#         print(f'{media} Aprovado')
#     else:
#         print(f'{media} Reprovado')
# resultProva()

# 6. Escreva uma função que imprima uma sequencia de 0 a 100.

# def zero100():
#     for i in range(101):
#         print(i)
# zero100()

# 7. Escreva uma função que leia 10 números e imprima
# a quantidade de pares, impares e números maiores que 20

# def quantidades():
#     pares = 0
#     impares = 0
#     maiores20 = 0
#     for i in range(10):
#         num = int(input('Digite um número: '))
#         if num % 2 == 0:
#             pares += 1
#         else:
#             impares += 1
#         if num >= 20:
#             maiores20 += 1
#     print(f"Quantidade de pares = {pares}")
#     print(f"Quantidade de ímpares = {impares}")
#     print(f"Quantidade de valores maiores que 20 = {maiores20}")
#
# quantidades()

# 8. Escreva uma função que leia o tempo de uma viagem e a velocidade média nessa viagem,
# em seguida informe o consumo total de combustivel da viagem,
# levando em consideração que o veiculo faz 10km/l


# 9. Escreva uma função que leia três lados de um triangulo e informe se ele forma um angulo reto.
# a soma dos quadrados de dois lados precisa ser igual ao quadrado do terceiro lado em pelo menos um dos casos.
# -------------------------------------------------------------
# projetosfortal@infinityschool.com.br
# -------------------------------------------------------------