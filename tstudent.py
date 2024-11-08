import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

class MentalEstatisticas:
    def __init__(self, arquivo_excel):
        self.df = pd.read_excel(arquivo_excel)
        print("Colunas do DataFrame:", self.df.columns)

    def teste_t_student(self, coluna, mu_0, alpha=0.05):
        # Cálculos do teste t
        x_bar = np.mean(self.df[coluna])
        s = np.std(self.df[coluna], ddof=1)
        n = len(self.df[coluna])
        t_stat = (x_bar - mu_0) / (s / np.sqrt(n))
        df = n - 1
        p_value = 2 * (1 - stats.t.cdf(abs(t_stat), df))

        # Exibindo resultados
        print(f"Média amostral: {x_bar}")
        print(f"Desvio padrão amostral: {s}")
        print(f"Valor t calculado: {t_stat}")
        print(f"Valor p: {p_value}")

        if p_value < alpha:
            print(f"Rejeita a hipótese nula (H₀). O valor p ({p_value:.4f}) é menor que o nível de significância ({alpha}).")
        else:
            print(f"Não rejeita a hipótese nula (H₀). O valor p ({p_value:.4f}) é maior ou igual ao nível de significância ({alpha}).")

        if 'Sleep_Hours' in self.df.columns:
            corr, _ = stats.pearsonr(self.df[coluna], self.df['Sleep_Hours'])
            print(f"Correlação r_h entre {coluna} e Sleep_Hours: {corr:.2f}")
        
        x = np.linspace(stats.t.ppf(0.001, df), stats.t.ppf(0.999, df), 1000)
        plt.plot(x, stats.t.pdf(x, df), label=f'Distribuição t (df={df})', color='blue')
        plt.fill_between(x, 0, stats.t.pdf(x, df), where=(x >= t_stat), color='red', alpha=0.5, label=f'Área crítica (t > {t_stat:.2f})')
        plt.axvline(x=t_stat, color='orange', linestyle='--', label=f'Valor t: {t_stat:.2f}')
       
        plt.text(t_stat + 1, 0.05, f'Correlação r_h: {corr:.2f}', fontsize=12, color='green')

       
        plt.title(f'Sleep_Hour', fontsize=16)
        plt.xlabel('Valor t', fontsize=12)
        plt.ylabel('Densidade de Probabilidade', fontsize=12)
        plt.legend()
        plt.grid(True)
        plt.tight_layout() 
        plt.show()


mental = MentalEstatisticas("mental.xlsx")


mental.teste_t_student(coluna='Sleep_Hours', mu_0=7)
