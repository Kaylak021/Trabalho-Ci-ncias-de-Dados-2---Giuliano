import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

tb = pd.read_excel("tabela_dados.xls")

# >> -- Exercicio 1 -- Crie listas com nomes para as características financeiras restantes -- <<
col_fatura = ['BILL_AMT1', 'BILL_AMT2', 'BILL_AMT3', 'BILL_AMT4', 'BILL_AMT5', 'BILL_AMT6']

col_pagamento = ['PAY_AMT1', 'PAY_AMT2', 'PAY_AMT3', 'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6']

# >> -- Exercicio 2 -- Use .describe() para examinar as sínteses estatísticas das características de valor da fatura. Reflita sobre o que viu. Faz sentido? -- <<
print(f"{"="*262}\n>>> Descrição dos dados:\n{tb.describe(include="all")}\n{"="*262}") # --

# >> -- Possivelmente ex 3 -- <<
tb[col_fatura].hist(bins=20, figsize=(12, 6)) # >> -- Cria o Historograma -- <<

"""
    >>> Explicação 
    - .hist() = cria gráficos;s
    - bins=20 = divide os valores em 20 partes;
    - figsize=(12, 6) → define o tamanho da figura; <<<
"""

plt.show() # >> -- Historograma -> Aparece o Grafico na tela -- <<


# >> -- Exercicio 4 -- Obtenha o resumo de .describe() para as características de valor do pagamento. Faz sentido? -- <<
print(f"\n{"="*262}\n>>>Descrição dos pagamentos:\n{tb[col_pagamento].describe(include='all')}\n{"="*262}")


# >> -- Exercício 5 -- (4,0pts): Plote um histograma das características de pagamento da fatura semelhante ao das características de valor da fatura ... -- <<
tb[col_pagamento].hist(bins=20, figsize=(20,6), xrot=45) # -- Cria o grafico-- <<

"""
Explicação:
- .hist() = gera gráficos de histograma
- bins=20 = divide os dados em 20 intervalos
- figsize=(12, 6) = define o tamanho da figura
- xrot=45 = gira os rótulos do eixo X em 45 graus (evita sobreposição)
"""

plt.show() # >> -- Mostra o segundo grafico -- <<


# >> -- Exercicio 6 -- Use uma máscara booleana para ver quantos dos dados de valor do pagamento são exatamente iguais a 0... -- <<

# >> conta quantos 0 possuem <<
total_zeros = (tb[col_pagamento] == 0).sum()

print(f"\n{"="*262}\n>>>Verificar quais pagamentos são igual a '0':\n{total_zeros}\n{"="*262}")

# >> -- Exercicio 7 -- Ignorando os pagamentos iguais a 0 usando a máscara que criou na etapa anterior, utilize o método .apply() do pandas
# e o método np.log10() do NumPy para plotar histogramas de transformações logarítmicas dos pagamentos diferentes de zero. -- <<

tb_sem_zero = tb[col_pagamento].replace(0, np.nan)

tb_log = tb_sem_zero.apply(np.log10)

tb_log.hist(bins=20, figsize=(12, 6))

plt.show()

"""
Explicação:
- replace(0, np.nan) = remove valores 0 (log10 não é definido para zero)
- .apply(np.log10) = aplica logaritmo base 10 em todos os dados
- log10 = reduz o impacto de valores extremos (outliers)
- melhora a distribuição dos dados para análise
- .hist() = gera histogramas dos dados transformados
- bins=20 = divide os valores em 20 faixas
"""