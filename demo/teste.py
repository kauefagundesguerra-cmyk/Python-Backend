import pandas as pd 
from openpyxl import load_workbook
from copy import copy
from pathlib import Path
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

#Função que une o poder de Pandas , sem perder os estilos da Tabela Excel Original
def style_saver(origin_file,edited_file,save_as,filetype="excel"):
  '''
  Reaplica Estilos da Tabela Excel Não Editada Por Pandas Na tabela Modificada Por Pandas
  Soluciona A Desistilização automática ao salvar Com Pandas No formato .XLSX

  Args:
    origin_file(Caminho do Arquivo): Usa o Arquivo Não editado (original) como Base de 
    Reaplicação Posterior dos Estilos.

    edited_file(Caminho do Arquivo): Arquivo Editado e Salvo em Pandas que se encontra 
    Sem os Estilos Originais.

    save_as("str"): Nome que Será salvo o Arquivo com a estilização do Arquivo Não Editado --origin_file--
  
  Return:
    Retorna o Arquivo Editado com Pandas --edited_file-- Porém com os Estilos de --origin_file-- Aplicados.
  '''
  styles = {}
  match filetype:
    case "excel":
      if ".xlsx" not in origin_file:
        origin_file= origin_file + ".xlsx"
      if ".xlsx" not in save_as:
        save_as = save_as + ".xlsx"
      wb_origin = load_workbook(origin_file)
      ws_origin = wb_origin.active
      for line in ws_origin:
        for cel in line:
          styles[cel.coordinate] = {
          "font" : copy(cel.font),
          "fill" : copy(cel.fill),
          "border" : copy(cel.border),
          "alignment" : copy(cel.alignment),
          "number_format" : cel.number_format 
          }
      edited_file = pd.read_excel(edited_file)
      tmp_xlsx = Path("Não Interaja No Touch.xlsx")
      edited_file.to_excel(tmp_xlsx,index=False)
      wb_none = load_workbook(tmp_xlsx)
      ws_none= wb_none.active
      for line in ws_none:
        for cel in line:      
          if cel.coordinate in styles:
            cont_style = cel.coordinate
            style = styles[cel.coordinate]
          elif cel.coordinate == "A1":
              style = styles[cel.offset(row=0,column=0).coordinate]
          else:
            style = styles[cont_style]
          cel.font = style["font"]
          cel.fill = style["fill"]
          cel.border = style["border"]
          cel.alignment = style["alignment"]
          cel.number_format = style["number_format"]   
      origin_file = Path(origin_file)
      if tmp_xlsx.exists():
        tmp_xlsx.unlink()
      return wb_none.save(save_as)
style_saver(origin_file,edited_file,save_as)
    