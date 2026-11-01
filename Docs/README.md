# Projeto Python Open Easy

## Contents

Contém diversas bibliotecas do Python, como Pandas, OpenPyXL e outras que serão adicionadas futuramente.

## Features

Tem o objetivo de, através de opções numéricas, executar códigos intrínsecos à opção, contendo análise de dados, automação e afins.

## Targets

Sendo implementado em um código backend, pode fornecer saídas no terminal de forma simples e intuitiva, livrando o desenvolvedor de diversas linhas de código para operações simples.

## Examples

### Rodando um Cálculo de Soma e Média de Vários Valores (With no Function Calculadora)

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
calculadora(1, 2, 3, 4, 5, 6, 7)  # Aceita uma quantidade variável de valores
```

### Preservando a Formatação de Arquivos Excel com Pandas e OpenPyXL

Ao utilizar o Pandas para editar e salvar arquivos `.xlsx`, a formatação original das células pode ser perdida.

Para solucionar esse problema, foi desenvolvida a função `style_saver()`, que utiliza o Pandas em conjunto com o OpenPyXL para reaplicar os estilos da planilha original após a edição dos dados.

A função trabalha com propriedades como:

- `font`: formatação das fontes.
- `fill`: preenchimento das células.
- `border`: bordas.
- `alignment`: alinhamento.
- `number_format`: formatação dos números.

#### Como utilizar

```python
style_saver(
    origin_file="original.xlsx",
    edited_file="editado_pandas.xlsx",
    save_as="resultado.xlsx"
)
```

**Arquivos para teste:**

Disponibilizei dois arquivos `.xlsx` na pasta `docs` do projeto para que qualquer pessoa interessada possa testar a função `style_saver()` e verificar seu funcionamento.

Basta utilizar os arquivos disponibilizados como entrada da função, seguindo os parâmetros indicados acima.
