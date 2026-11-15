
def subt(*nums):
    nums = list(nums)
    start = - 1
    for n in nums:
        start += 1
        if start == 0:
            n = n - 1
        if start >= 1:
            v = nums[start - 1] - n
            nums[start] = v
    return nums[-1]

def media(*nums):
  return sum(nums) / len(nums)

def div(*nums):
    nums = list(nums)
    start = -1
    for n in nums:
        start += 1
        if start == 0:
            n = n / 1
        if start >= 1:
            v = nums[start - 1] / n
            nums[start] = v
    return nums[-1]


def multp(*nums):
    nums = list(nums)
    start = -1
    for n in nums:
        start += 1
        if start == 0:
            n = n * 1
        if start >= 1:
            v = nums[start - 1] * n
            nums[start] = v
    return nums[-1]

def calculadora(*numeros,operator="None"):
    '''
    Explain:
        Calcula Números de quantidade variavel e indefinida em quantidade de acordo com a operação  escolhida pelo parâmetro operator

    Params:
        numeros = Qtd Infinita de Números
        operator = div = str = divisão dos Números ,
        multp = str = Multiplicação dos Números  ,
        subt = str = Subtração dos Números
        soma = str = Soma dos Números
    Returns:
         a operação é aplicada a todos os Números
    '''
    if len(numeros) == 1:
     raise ValueError("Quantidade de Números Insuficiente")

    operations = {
      "div":div,
      "multp":multp,
      "subt":subt,
      "media":media
      }
    try:
        for op in operations:
            if operator == op:
                return operations[op](*numeros)
    except ValueError:
        print("Digite apenas Números Inteiros !")
    except ZeroDivisionError:
        print("Não é Possível dividir por 0!")
