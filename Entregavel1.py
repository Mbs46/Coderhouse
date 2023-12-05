'''Crie um programa que calcule o Imposto de Renda devido por um contribuinte. O usuário deve inserir o nome do contribuinte e o salário mensal. O programa deve calcular o imposto com base nas seguintes faixas:

Até R$ 1.903,98: isento
De R$ 1.903,99 até R$ 2.826,65: 7.5%
De R$ 2.826,66 até R$ 3.751,05: 15%
De R$ 3.751,06 até R$ 4.664,68: 22.5%
Acima de R$ 4.664,68: 27.5%
Apresente o nome do contribuinte e o valor do imposto a pagar.'''

contribuinte = input("Nome: ")
salario = float(input("Salário: "))

if salario <= 1903.98:
    ir = 0.0
elif salario <= 2826.65:
    ir = salario * 0.075
elif salario <= 3751.05:
    ir = salario * 0.15
elif salario <= 4664.68:
    ir = salario * 0.225
else:
    ir = salario * 0.275

print(f"Nome: {contribuinte}")
print(f"Salário: R$ {salario:.2f}")
print(f"Imposto: R$ {ir:.2f}")







'''Desenvolva um programa que determine se uma pessoa está apta a votar. O usuário deve informar o nome e a idade. As regras para determinar a elegibilidade são:

Menos de 16 anos: não pode votar
De 16 a 17 anos: voto facultativo
De 18 a 70 anos: voto obrigatório
Mais de 70 anos: voto facultativo
O programa deve informar o nome da pessoa e se ela deve votar, não pode votar ou se o voto é facultativo.'''

nome = input("Nome: ")
idade = float(input("Idade: "))

if idade < 16:
    resultado = "Não pode votar"
elif 16 <= idade <= 17:
    resultado = "Voto facultativo"
elif 18 <= idade <= 70:
    resultado = "Voto Obrigatório"
elif idade > 70:
    resultado = "Voto facultativo"

print(f"Nome: {nome}")
print(f"Resultado: {resultado}")







'''Sistema de Bonificação de Funcionários:
Elabore um programa que calcule a bonificação anual de um funcionário. Peça o nome do funcionário, o salário e o tempo de serviço em anos na empresa. A bonificação é dada da seguinte forma:

Menos de 1 ano de serviço: sem bonificação
De 1 a 3 anos de serviço: 10% do salário
De 4 a 6 anos de serviço: 15% do salário
De 7 a 10 anos de serviço: 20% do salário
Mais de 10 anos de serviço: 25% do salário
O programa deve mostrar o nome do funcionário e o valor da bonificação que ele receberá.'''


nome = input("Nome: ")
salario = float(input("Salário: "))
tempo = float(input("Tempo: "))

if tempo < 1:
    bonus = 0.0
elif 1 <= tempo <= 3:
    bonus = salario * 0.1
elif 4 <= tempo <= 6:
    bonus = salario * 0.15
elif 7 <= tempo <= 10:
    bonus = salario * 0.20
else:
    bonus = salario * 0.25

print(f"Nome: {nome}")
print(f"Salário: R$ {salario:.2f}")
print(f"Bonus: R$ {bonus:.2f}")






'''Calculadora de Consumo de Combustível:
Crie um aplicativo para calcular o consumo médio de combustível de um veículo. O usuário deve inserir o nome do motorista, a quantidade de quilômetros percorridos e a quantidade de combustível gasto em litros. O programa deve calcular o consumo médio (quilômetros por litro) e classificar a eficiência do veículo conforme a tabela:

Menos de 8 km/l: Venda o carro!
Entre 8 e 12 km/l: Econômico
Mais de 12 km/l: Super econômico
Apresente o nome do motorista e a classificação de eficiência do veículo.'''

motorista = input("Nome do motorista: ")
km = float(input("Quantidade de quilômetros percorridos: "))
combustivel = float(input("Quantidade de combustível gasto em L: "))

consumo = km / combustivel

if consumo < 8:
    classificacao = "Venda o carro!"
elif 8 <= consumo <= 12:
    classificacao = "Econômico"
else:
    classificacao = "Super econômico"

print(f"Motorista: {motorista}")
print(f"Consumo: {consumo:.2f} km/l")
print(f"Classificação: {classificacao}")







'''Sistema de Classificação de Hotéis:
Desenvolva um programa que classifique um hotel baseado na avaliação dos hóspedes. O usuário deve digitar o nome do hotel e três notas referentes aos critérios de conforto, limpeza e localização. O programa deve calcular a média das notas e emitir uma classificação:

Média menor que 4: Hotel de 1 estrela
Média de 4 a 6: Hotel de 3 estrelas
Média de 6 a 8: Hotel de 4 estrelas
Média 9 ou superior: Hotel de 5 estrelas
No final, o programa deve exibir o nome do hotel e sua classificação em estrelas.'''


hotel = input("Nome do hotel: ")
conforto = float(input("Nota conforto (0 a 10): "))
limpeza = float(input("Nota limpeza (0 a 10): "))
localizacao = float(input("Nota localização (0 a 10): "))

media = (conforto + limpeza + localizacao) / 3

if media < 4:
    classificacao = "Hotel de 1 estrela"
elif 4 <= media < 6:
    classificacao = "Hotel de 3 estrelas"
elif 6 <= media <= 8:
    classificacao = "Hotel de 4 estrelas"
else:
    classificacao = "Hotel de 5 estrelas"

print(f"Hotel: {hotel}")
print(f"Classificação: {classificacao}")

git init
