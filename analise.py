import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

df = pd.read_excel("mental.xlsx")

print("Valores únicos na coluna 'Stress_Level':", df['Stress_Level'].unique())

df['Stress_Level'] = df['Stress_Level'].str.strip().str.lower()
df['Stress_Level'] = df['Stress_Level'].map({'low': 1, 'medium': 2, 'high': 3})

print("Coluna 'Stress_Level' após mapeamento:", df['Stress_Level'].head())

if df['Stress_Level'].isna().sum() > 0:
    print("Há valores NaN na coluna 'Stress_Level' após o mapeamento.")

class TeoremaCentralLimite:
    def __init__(self, df, coluna, tamanho_amostra, num_amostras):
        self.df = df
        self.coluna = coluna
        self.tamanho_amostra = tamanho_amostra
        self.num_amostras = num_amostras
        self.media_populacional = np.mean(df[coluna])
        self.variancia_populacional = np.var(df[coluna], ddof=1)

    def gerar_medias_amostrais(self):
        medias_amostrais = []
        valores_z = []
        for _ in range(self.num_amostras):
            amostra = np.random.choice(self.df[self.coluna], size=self.tamanho_amostra)
            media_amostra = np.mean(amostra)
            medias_amostrais.append(media_amostra)
            
            z = (media_amostra - self.media_populacional) / (np.sqrt(self.variancia_populacional / self.tamanho_amostra))
            valores_z.append(z)
        
        return medias_amostrais, valores_z

    def interpretar_probabilidades(self, valores_z):
        probabilidades = [1 - stats.norm.cdf(abs(z)) for z in valores_z]
        return probabilidades

    def plot_distribuicao(self, medias_amostrais):
        plt.hist(medias_amostrais, bins=20, edgecolor='black', alpha=0.7)
        plt.title("Distribuição das Médias Amostrais de Stress_Level")
        plt.xlabel("Média Amostral")
        plt.ylabel("Frequência")
        plt.show()

tcl = TeoremaCentralLimite(df, coluna='Stress_Level', tamanho_amostra=30, num_amostras=1000)

medias_amostrais, valores_z = tcl.gerar_medias_amostrais()

probabilidades = tcl.interpretar_probabilidades(valores_z)
print("Probabilidades (Tabela Z):", probabilidades[:5])

tcl.plot_distribuicao(medias_amostrais)
