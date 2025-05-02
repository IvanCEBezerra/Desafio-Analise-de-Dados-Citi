import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel('dados_tratados.xlsx')

#analise frequencia x media
df = df.sort_values('media', ascending=True)
df['media'] = df['media'].str.replace(',', '.').astype(float)

#cálculo da média de frequência
Freq_media_aprovados = df[df['aprovado'] == 'Sim']['frequencia'].mean()
Freq_media_reporvados = df[df['aprovado'] == 'Não']['frequencia'].mean()

#desenho do gráfico
x = np.array(df['frequencia'])
y = np.array(df['media'])

plt.figure(figsize=(10, 5))
plt.scatter(x, y)
plt.yticks(np.arange(0, 10.5, 0.5))
plt.title('Frequência x Média')
plt.xlabel('Frequência')
plt.ylabel('Média')

#desenha das linhas do gradiente do gráfico
plt.grid(True, linestyle='--', alpha=0.5)
plt.axhline(y=7, color='r', linestyle='--', label='Nota mínima para aprovação')
plt.axvline(x=Freq_media_aprovados, color='#79DF00', linestyle='--', label='Frequência média dos aprovados')
plt.axvline(x=Freq_media_reporvados, color='#FFD700', linestyle='--', label='Frequência média dos reprovados')
plt.legend(loc='lower left')


#comapração de turmas
aprovados = df[df['aprovado'] == 'Sim']
contagem_series = aprovados['serie'].value_counts().sort_index()

#desenha o gráfico de pizza sobre os alunos aprovados por série
cores_pizza = [
    '#2F4858',  # Azul petróleo escuro
    '#33658A',  # Azul aço
    '#86BBD8',  # Azul claro acinzentado
    '#F6AE2D',  # Mostarda suave
    '#F26419',  # Laranja queimado
    '#A1C181',  # Verde oliva claro
    '#6C584C',  # Marrom acinzentado (sofisticado)
    '#8D99AE'   # Cinza azulado moderno
]


plt.figure(figsize=(6, 6))
plt.pie(contagem_series, labels=contagem_series.index,
        autopct='%1.1f%%', startangle=45, colors=cores_pizza, shadow=True, wedgeprops={'edgecolor': 'white', 'linewidth': 1})

plt.title("Distribuição dos Aprovados por Série")
plt.tight_layout()
plt.show()

plt.show()
