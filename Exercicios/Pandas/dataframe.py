import pandas as pd
import numpy as np


# Criar um DataFrame a partir de um dicionário
dados = {"Nome": ["Ana", "Bruno", "Carlos", "Diana"],
         "Idade": [20, 30, 50, 40]}

# Transformar este dicionário em um DataFrame]
df = pd.DataFrame(dados)

print(df)
