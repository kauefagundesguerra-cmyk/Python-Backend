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
calculadora(1, 2, 3, 4, 5, 6, 7,operation="divisao")  # Aceita uma quantidade variável de valores,com Parâmetro do tipo de operação
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

Disponibilizei dois arquivos `.xlsx` na pasta `demo` do projeto para que qualquer pessoa interessada possa testar a função `style_saver()` e verificar seu funcionamento.

Basta utilizar os arquivos disponibilizados como entrada da função, seguindo os parâmetros indicados acima.

## 🎨 Personalização Flexível de Estilos Excel (Pandas + OpenPyXL)

Uma das funcionalidades do projeto é a capacidade de **editar planilhas utilizando o poder do Pandas sem perder a formatação original do Excel**.

Normalmente, ao utilizar `pandas` para salvar uma planilha no formato `.xlsx`, os estilos originais das células não são preservados. Para solucionar esse problema, foi desenvolvida a função `style_saver()`, que utiliza a biblioteca `openpyxl` para armazenar e reaplicar os estilos da planilha original após a edição.

### ⚙️ Personalização dinâmica

Além de preservar os estilos existentes, a função permite personalizar elementos específicos da planilha por meio de argumentos nomeados (`**style_configs`).

Isso significa que você pode modificar apenas os elementos desejados, mantendo os demais estilos originais.

Os elementos personalizáveis são:

| Argumento       | Descrição                                                   |
| --------------- | ----------------------------------------------------------- |
| `font`          | Personaliza fonte, tamanho, cor e negrito.                  |
| `fill`          | Altera a cor e o preenchimento das células.                 |
| `border`        | Personaliza as bordas das células.                          |
| `alignment`     | Modifica o alinhamento e a orientação do conteúdo.          |
| `number_format` | Define a exibição de números, datas, moedas e porcentagens. |

### 🧩 Exemplo 1 — Personalizando fonte e preenchimento

Primeiro, podemos criar nossos próprios estilos utilizando o OpenPyXL:

```python
from openpyxl.styles import Font, PatternFill

minha_fonte = Font(
    name="Arial",
    size=12,
    bold=True,
    color="FF0000"
)

meu_fundo = PatternFill(
    start_color="FFFF00",
    end_color="FFFF00",
    fill_type="solid"
)
```

Agora, basta passar esses estilos como argumentos na função:

```python
style_saver(
    "demo/original_with_style.xlsx",
    "demo/edited_with_no_style.xlsx",
    "teste",
    font=minha_fonte,
    fill=meu_fundo
)
```

Nesse exemplo:

- Todas as células recebem a fonte personalizada.
- O preenchimento das células também é substituído pela cor amarela.
- As bordas, os alinhamentos e os formatos numéricos continuam preservando os estilos originais.

### 🧩 Exemplo 2 — Personalizando somente um elemento

Não é necessário modificar todos os estilos simultaneamente.

Por exemplo, podemos alterar somente a fonte:

```python
style_saver(
    "original.xlsx",
    "editado.xlsx",
    "resultado.xlsx",
    font=minha_fonte
)
```

Nesse caso, os preenchimentos, bordas, alinhamentos e formatos numéricos permanecem baseados na planilha original.

### 🧩 Exemplo 3 — Personalização completa

Também é possível combinar diferentes configurações:

```python
style_saver(
    "original.xlsx",
    "editado.xlsx",
    "resultado.xlsx",
    font=minha_fonte,
    fill=meu_fundo,
    border=minha_borda,
    alignment=meu_alinhamento
)
```

Cada argumento representa um estilo independente, permitindo construir diferentes combinações de formatação.

### 💡 Como funciona a personalização?

A flexibilidade dessa funcionalidade está na utilização de `**style_configs` em conjunto com `copy()`.

Dentro da função, os estilos originais são armazenados em um dicionário utilizando as coordenadas das células como referência (`A1`, `B2`, `C3` etc.).

Posteriormente, os argumentos recebidos são comparados com as propriedades armazenadas:

```python
for cel in styles.values():
    for chave, valor in style_configs.items():
        if chave in cel.keys():
            cel[chave] = copy(valor)
```

Assim, somente as propriedades informadas pelo usuário são substituídas. As demais continuam preservadas.

### 🚀 Resultado

Essa abordagem combina duas bibliotecas com funções diferentes:

- **Pandas:** manipulação, análise e tratamento dos dados.
- **OpenPyXL:** preservação e personalização da estrutura visual da planilha.

O resultado é uma solução flexível que permite manipular dados programaticamente sem abrir mão da apresentação visual original do Excel.

# Guia de instalação

Este guia apresenta as diferentes formas de instalar o **OpenEasy** utilizando o gerenciador de pacotes `pip`, com ou sem ambiente virtual (`venv`).

As instruções contemplam Windows e distribuições Linux.

## 1. Pré-requisitos

Antes de iniciar a instalação, verifique se você possui:

- Python 3.10 ou superior.
- Pip (gerenciador de pacotes do Python).
- Acesso ao terminal do sistema operacional.

Para verificar as versões instaladas:

**Windows:**

```bash
python --version
python -m pip --version
```

**Linux:**

```bash
python3 --version
python3 -m pip --version
```

## 2. Instalação utilizando ambiente virtual (recomendado)

O ambiente virtual permite instalar dependências isoladamente, evitando conflitos entre projetos Python.

### Windows

**1. Criar o ambiente virtual:**

```powershell
python -m venv .venv
```

**2. Ativar o ambiente virtual:**

```powershell
.venv\Scripts\activate
```

**3. Instalar o pacote:**

```bash
pip install openeasy
```

**4. Desativar o ambiente virtual:**

```bash
deactivate
```

### Linux

**1. Instalar o suporte ao venv (se necessário):**

Ubuntu / Debian / Linux Mint:

```bash
sudo apt install python3-venv python3-full
```

Fedora:

```bash
sudo dnf install python3
```

Arch Linux:

```bash
sudo pacman -S python python-pip
```

**2. Criar o ambiente virtual:**

```bash
python3 -m venv .venv
```

**3. Ativar o ambiente virtual:**

```bash
source .venv/bin/activate
```

**4. Instalar o pacote:**

```bash
pip install openeasy
```

**5. Desativar o ambiente virtual:**

```bash
deactivate
```

## 3. Instalação normal (sem ambiente virtual)

Também é possível instalar o pacote diretamente no ambiente Python disponível no sistema.

> Atenção: essa modalidade pode gerar conflitos entre dependências de diferentes projetos. Em distribuições Linux modernas, a instalação global via pip pode ser bloqueada pelo gerenciamento de pacotes do sistema (PEP 668).

### Windows

Abra o PowerShell ou CMD e execute:

```powershell
python -m pip install openeasy
```

Para atualizar:

```powershell
python -m pip install --upgrade openeasy
```

### Linux

Em distribuições que permitem a instalação global pelo pip:

```bash
python3 -m pip install openeasy
```

Para atualizar:

```bash
python3 -m pip install --upgrade openeasy
```

**Observação para Ubuntu, Debian e Linux Mint:**

Caso apareça o erro `externally-managed-environment`, o sistema está protegendo o Python gerenciado pela distribuição.

Nesse caso, utilize um ambiente virtual (`venv`) ou instale a versão disponibilizada pelo gerenciador de pacotes da distribuição, caso exista.

Evite utilizar `--break-system-packages`, pois isso pode comprometer dependências do próprio sistema operacional.

## 4. Instalação a partir do código-fonte

Caso queira instalar o projeto diretamente de um repositório Git:

```bash
git clone URL_DO_REPOSITORIO
```

Entre na pasta do projeto:

```bash
cd NOME_DO_PROJETO
```

Instale utilizando pip:

```bash
pip install .
```

Para instalação editável, destinada ao desenvolvimento:

```bash
pip install -e .
```

## 5. Verificar a instalação

Para verificar se o pacote foi instalado corretamente:

```bash
pip show openeasy
```

Também é possível verificar se o Python consegue localizar o pacote:

```bash
python -c "import openeasy; print('Instalação concluída!')"
```

No Linux, caso utilize `python3`:

```bash
python3 -c "import openeasy; print('Instalação concluída!')"
```

## 6. Desinstalação

Para remover o pacote:

```bash
pip uninstall openeasy
```

Para confirmar, digite `y` quando solicitado.

---

## Considerações finais

- Recomenda-se utilizar ambientes virtuais para projetos Python.
- Não é necessário versionar a pasta `.venv` no Git.
- Para compartilhar as dependências do projeto, utilize um arquivo `requirements.txt`.
- Mantenha o Python e o pip atualizados sempre que possível.

**OpenEasy — Simplificando operações com Python.**
