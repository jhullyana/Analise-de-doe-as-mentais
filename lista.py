import pandas as pd


arquivo_excel = "mental.xlsx"
df = pd.read_excel(arquivo_excel)
print("Colunas do DataFrame:", df.columns)
