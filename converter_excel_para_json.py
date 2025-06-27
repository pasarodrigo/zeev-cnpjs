import pandas as pd
import json
import re

# Carregar a planilha Excel
df = pd.read_excel("baseAnp.xlsx", engine="openpyxl")

# Extrair a coluna de CNPJs
cnpjs = df["CNPJ"].astype(str)

# Limpar os CNPJs: remover caracteres não numéricos e preencher com zeros à esquerda
cnpjs_limpos = cnpjs.apply(lambda x: re.sub(r"\D", "", x).zfill(14))

# Remover duplicatas e ordenar
cnpjs_unicos = sorted(set(cnpjs_limpos))

# Salvar como JSON
with open("cnpjs_validos.json", "w") as json_file:
    json.dump(cnpjs_unicos, json_file, indent=2)
