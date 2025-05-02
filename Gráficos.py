import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel("dados_tratados.xlsx")

#Contagem de alunos aprovados e reprovados
conta_aprovados = df['aprovado'].value_counts()
aprovado = conta_aprovados.get('Sim', 0)
reprovado = conta_aprovados.get('Não', 0)

#Desenho do gráfico de pizza sobre os aprovados e reprovados
plt.figure(figsize=(6, 6))
plt.title("Aprovação dos alunos")
y = np.array([aprovado, reprovado])
mylabels = ['Aprovados', 'Reprovados']
plt.pie(y, labels=mylabels, autopct='%1.1f%%', startangle=45, colors=['#4CAF50', '#FF5733'])


#Contagem de alunos por sexo
plt.figure(figsize=(6, 4))
conta_sexo = df['sexo'].value_counts()
homens = conta_sexo.get('Masculino', 0)
mulheres = conta_sexo.get('Feminino', 0)

#Desenho do gráfico de barra sobre os alunos por sexo
plt.title("Sexo dos alunos")
x = np.array(['Masculino', 'Feminino'])
y = np.array([homens, mulheres])

plt.bar(x, y, color=['#2196F3', '#FF4081'])
plt.xlabel("Sexo")
plt.ylabel("Quantidade de alunos")

# -- Destaque dos melhores alunos --

# transforma a coluna 'media' para float
df['media_float'] = df['media'].str.replace(',', '.').astype(float)
top5 = df.nlargest(5, 'media_float').sort_values('media_float', ascending=True)

#desenho do gráfico de barra sobre os melhores alunos
plt.figure(figsize=(12, 8))
plt.title("Melhores médias")

x = np.array(top5['nome'])
y = np.array(top5['media_float'])


#gera o degradê a partir do colormap 'Greens
tons = top5['media_float']      # Série de médias correspondentes
cmap  = plt.get_cmap('Greens')
cores = cmap(np.linspace(0.4, 0.9, len(tons)))

plt.barh(x, y, color=cores)
plt.xlabel("Média")
plt.ylabel("Alunos")


#desenha gráfico de frequência
plt.figure(figsize=(12, 8))
plt.title("Frequência dos alunos")

#analisa alunos com maior frequência
freq5 = df.nlargest(5, 'frequencia')
lista_cor = []
lista_nome = []
for i in df['id_aluno']:
    if i in freq5['id_aluno'].values:
        lista_cor.append('#D4AF37')  # Cor ouro para os alunos com maior frequência
        #acha informações da linha correspondente
        linha = df[df['id_aluno'] == i]
        nome = linha['nome'].values[0]
        lista_nome.append(nome)
    else:
        lista_cor.append('#D3D3D3')  # Cor cinza para os demais alunos
        lista_nome.append('')

x = np.array(df['id_aluno'])
y = np.array(df['frequencia'])

plt.barh(x, y, color=lista_cor, tick_label=lista_nome)
plt.ylabel("Alunos")
plt.xlabel("Frequência (%)")

# Adiciona mais linhas de grid na vertical
plt.grid(axis='x', linestyle='--', alpha=0.8)
plt.axvline(x=60.2, color='red', linestyle='--', label='Menor frequência')
plt.axvline(x=99.4, color='green', linestyle='--', label='Maior frequência')
plt.legend(loc='lower left')
plt.xticks(np.arange(60, 101, 5))  

plt.show()
