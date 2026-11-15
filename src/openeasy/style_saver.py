from openpyxl import load_workbook
import pandas as pd
from copy import copy
from pathlib import Path
def style_saver(origin_file,edited_file,save_as,filetype="excel",**style_configs):
  '''
  Reaplica Estilos da Tabela Excel Não Editada Por Pandas Na tabela Modificada Por Pandas
  Soluciona A Desistilização automática ao salvar Com Pandas No formato .XLSX

  Args:
    origin_file(Caminho do Arquivo): Usa o Arquivo Não editado (original) como Base de 
    Reaplicação Posterior dos Estilos.

    edited_file(Caminho do Arquivo): Arquivo Editado e Salvo em Pandas que se encontra 
    Sem os Estilos Originais.

    save_as("str"): Nome que Será salvo o Arquivo com a estilização do Arquivo Não Editado --origin_file--
    
    style_configs ("str"): aceita os argumento font (estilo da fonte),fill (estilo do preenchimento)
    border (estilo de contorno das Células),alignment (Posicionamento / Orientação do texto dentro da Célula)
    number_format (formato Númerico das Células) 
  
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
      for cel in styles.values():
        for chave, valor in style_configs.items(): 
          if chave in cel.keys():    
              cel[chave] = copy(valor)         
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