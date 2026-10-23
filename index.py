import pandas as pd
import openpyxl
import time
import datetime as dt
from unidecode import unidecode

data_hora = dt.datetime.now()
print("----------Bem vindo a Multi Lib V1.0-------------")

print(f"\n Data Atual:{data_hora.strftime('%Y/%m/%d %H:%M')}\n")
print("Opções\n1-Calculadora (Normal e Científica)\n2-Análise de Dados (Lib Pandas e Openpyxl)\n")

def subtracao(*numeros):
  return numeros[0] - sum(numeros[1:])

def media(*numeros): 
  return sum(numeros) / len(numeros)

def padronizar(text):
  return unidecode(text.lower().strip())

def calculadora(*numeros):
  op_escolhida = int(input("Digite o Número da Opção correspondente à desejada: "))
  operacoes=['Soma','Subtração','Média','Divisão']
  match op_escolhida:
    case 1:
      match operacoes:
      case "soma":
        print(f"O resultado foi uma Média de :{sum(numeros)}")
      case "subtracao":
        print(f"O resultado foi uma Média de :{subtracao(numeros)}")
      case "media":
        print(f"O resultado foi uma Média de :{media(numeros)}")
      #case "divisao" em breve
calculadora(3,2,1)
  






