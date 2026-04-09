
# séries possibilitam cálculos matemáticos com mais facilidade 
#%%

idades = [25, 40, 30, 23, 18, 43, 21, 32, 53, 29, 19, 17,
          30, 22, 27, 31, 26, 24, 28, 33]

import pandas as pd

series_idade = pd.Series(idades)

#%%
media = series_idade.mean()
print("Média =", media)

#%%

variancia = series_idade.var()
print("Variância: ", variancia)

#%%
sumary_idades = series_idade.describe()
print("Resumo dos dados:", sumary_idades) 