#Questão 1 - Escreva uma função que receba um número inteiro como parâmetro e informe se ele é positivo, negativo ou ZERO.

def number(num):
  if num > 0:
    print(f'{num} é positivo')
  elif num < 0:
    print(f'{num} é negativo')
  else:
    print(f'{num} é neutro')

numero = int(input('Digite um número: '))

# number(numero)

#Questão 2 - Crie uma função que receba dois números como parâmetros, verifique e retorne a quantidade (0, 1 ou 2) de números pares.

numero1=int(input(f'Digite um número: '))
numero2=int(input(f'Digite outro número: '))

def numeroPar(num1,num2):
  total = 0
  if num1 % 2 == 0:
    total+= 1
  if num2 % 2 == 0:
    total+= 1
  return total
print(f"O total de números pares é {numeroPar(numero1,numero2)}")

#Questão 3 - Escreva uma função que receba dois parâmetros, sendo o primeiro um número inteiro e o segundo uma porcentagem, depois calcule e retorne o valor do número somado ao aumento percentual informado.

numeroInt=int(input(f'Digite um número: '))
porcentagem=int(input(f'Digite outro número: '))

def numPorcento(num1,por):
  por = por / 100
  numMultiplicado = por * num1
  soma = numMultiplicado + num1
  return soma
print(numPorcento(numeroInt, porcentagem))

