import pandas as pd
import openpyxl
import time
import datetime as dt
from unidecode import unidecode
from math import ceil


data_hora = dt.datetime.now()
print("----------Bem vindo a Semantic Programming-------------")

print(f"\n Data Atual:{data_hora.strftime('%Y/%m/%d %H:%M')}\n")

def subtracao(nums):
  return sum(nums[1:]) - nums[0]

def media(nums): 
  return sum(nums) / len(nums)

def padronizar(text):
  return unidecode(text.lower().strip())

def type_num(num): 
   try:
      return int(num)
   except ValueError:
      try:
         return float(num)
      except ValueError:
         return None

print("Opções\n1-Calculadora (Normal e Científica)\n2-Análise de Dados (Lib Pandas e Openpyxl)\n")

def calculadora(*numeros):
  op_changed = int(input("Digite o Número da Opção correspondente à desejada: "))
  print(['Soma','Subtração','Média','Divisão'])
  op_math = str(input("Digite a Operação Desejada com Base nas Disponíveis Acima: "))
  op_math = padronizar(op_math)
  int_or_full = input("Deseja o Resultado em [ 1 ]-Números arredondados\n[ 2 ]-Números Quebrados?: ")

  match int_or_full:
    case "1":
      match op_math:
        case "soma":    
            print(f"O resultado Da Soma foi: {ceil(sum(numeros))}")
        case "subtracao":
            print(f"O resultado Da Subtração foi: {ceil(subtracao((numeros)))}")
        case "media":
            print(f"O resultado foi uma Média de: {ceil(media(numeros))}")
    case "2":
      match op_math:
        case "soma":    
            print(f"O resultado Da Soma foi: {float(sum(numeros))}")
        case "subtracao":
            print(f"O resultado Da Subtração foi: {float(subtracao((numeros)))}")
        case "media":
            print(f"O resultado foi uma Média de: {float(media(numeros))}")
      #case "divisao" em breve
calculadora(3,2.5,1)
  






