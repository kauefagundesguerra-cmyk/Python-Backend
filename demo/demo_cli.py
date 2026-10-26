
import time
import datetime as dt
from unidecode import unidecode
from math import ceil


data_hora = dt.datetime.now()


print(f"\n Data Atual:{data_hora.strftime('%Y/%m/%d %H:%M')}\n")



def subtracao(nums):
  return sum(nums[1:]) - nums[0]

def media(nums): 
  return sum(nums) / len(nums)

def divisao(nums):
   start = -1
   cont = 0
   results = 0
   while True:
      if len(nums)>=4:
        div = nums[start + 1] / nums[start + 2]
        cont+=2
        div = div / nums[cont+1]
        results+=div
        break
      else:
         if len(nums) == 3:
            div = nums[start + 1] / nums[start + 2]
            div = div / nums[start + 3]
            cont=+3
            results+=div
            break
         elif len(nums) == 2:
            cont+=2
            div = nums[start  + 1] / nums[start + 2]
            results+=div
            break
   return results
      

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
        case "divisao":
            print(f"O resultado Da Divisão foi {ceil(divisao(numeros))}") 
    case "2":
      match op_math:
        case "soma":    
            print(f"O resultado Da Soma foi: {float(sum(numeros))}")
        case "subtracao":
            print(f"O resultado Da Subtração foi: {float(subtracao((numeros)))}")
        case "media":
            print(f"O resultado foi uma Média de: {float(media(numeros))}")
        case "divisao":
            print(f"O resultado Da Divisão foi {float(divisao(numeros))}") 
     
calculadora(3,2.5,1)
  






