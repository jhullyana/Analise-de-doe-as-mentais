import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("mental.xlsx")

class CoeficientesCovariancia:
    def __init__(self, df, coluna1, coluna2):
        self.df = df
        self.coluna1 = coluna1
        self.coluna2 = coluna2

    def tratar_dados(self):
        if self.df[self.coluna2].dtype == 'O':
            mapping = {'Low': 1, 'Medium': 2, 'High': 3}
            self.df[self.coluna2] = self.df[self.coluna2].map(mapping)
        self.df[self.coluna1] = pd.to_numeric(self.df[self.coluna1], errors='coerce')
        self.df[self.coluna2] = pd.to_numeric(self.df[self.coluna2], errors='coerce')

    def calcular_covariancia(self):
        return np.cov(self.df[self.coluna1], self.df[self.coluna2])[0][1]

    def calcular_correlacao(self):
        return np.corrcoef(self.df[self.coluna1], self.df[self.coluna2])[0][1]

    def plot_grafico(self):
        plt.figure(figsize=(10,6))
        sns.scatterplot(x=self.df[self.coluna1], y=self.df[self.coluna2], 
                        hue=self.df[self.coluna2], palette='coolwarm', s=100, alpha=0.7)
        plt.title(f'Relação entre {self.coluna1} e {self.coluna2}', fontsize=16)
        plt.xlabel(self.coluna1, fontsize=14)
        plt.ylabel(self.coluna2, fontsize=14)
        plt.grid(True)
        plt.tight_layout()
        plt.show()

cc = CoeficientesCovariancia(df, coluna1='Work_Hours', coluna2='Stress_Level')

cc.tratar_dados()

covariancia = cc.calcular_covariancia()
correlacao = cc.calcular_correlacao()

print("Coeficiente de Covariância:", covariancia)
print("Coeficiente de Correlação (rho):", correlacao)

cc.plot_grafico()
