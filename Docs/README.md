# Projeto Python Open Easy

## Contents

Contém Diversas Bibliotecas do Python como Pandas, Openpyxl e mais em breve.

## Features

Tem o objetivo de através de opções numéricas executar códigos intrínsecos a Opção Contendo Análise de Dados, automação e afins

## Targets

Sendo Implementado em um código backend pode fornecer saídas no terminal de forma simples e intuitiva livrando de diversas linhas de código para coisas simples.

## Examples

### Rodando Um Cálculo de Soma e Média de Vários Valores (With no Function Calculadora)

```python
quantidade = int(input("Quantos valores você quer informar? "))

soma = 0
for i in range(quantidade):
    valor = float(input(f"Digite o valor {i + 1}: ").replace(",", "."))
    soma += valor

if quantidade > 0:
    media = soma / quantidade
    print(f"Soma: {soma}")
    print(f"Média: {media:.2f}")
else:
    print("Nenhum valor informado.")
```

### Usando a Função Calculadora (With Calculadora Function)

```python
calculadora(1, 2, 3, 4, 5, 6, 7)  # Aceita uma quantidade infinita de valores
```
