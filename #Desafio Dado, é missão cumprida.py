#Desafio Dado, é missão cumprida
import pandas as pd
import datetime

def identifica_classe(valor):
    if isinstance(valor, (int, float)):
        valor = float(valor)
        valor = round(valor, 1)
        return str(valor)
    elif isinstance(valor, str):
        valor = float(valor)
        valor = round(valor, 1)
        return str(valor)
    elif isinstance(valor, (datetime.datetime, datetime.date)):
        dia = valor.day
        mes = valor.month
        return str(f"{dia}.{mes:01d}")
    
def verifica_aprovacao(media):
    if media >= 7:
        return 'Sim'
    else:
        return 'Não'

#leitura do arquvivo excel
df = pd.read_excel('Base_despadronizada.xlsx')

#filtra e padroniza os dados
df['nota_matematica'] = df['nota_matematica'].apply(identifica_classe)
df['nota_portugues'] = df['nota_portugues'].apply(identifica_classe)

#calculo da media do aluno
df['nota_matematica'] = df['nota_matematica'].astype(float)
df['nota_portugues'] = df['nota_portugues'].astype(float)
df['frequencia'] = df['frequencia'].astype(float)
df['media'] = ((df['nota_matematica'] + df['nota_portugues'] + df['frequencia']/10) / 3).round(1)

#clacula se o aluno foi aprovado ou reprovado
df['aprovado'] = df['media'].apply(verifica_aprovacao)

#padranizaçao brasileira para as notas
df['media'] = df['media'].astype(str).str.replace('.', ',')


#padronização das notas
df['nota_matematica'] = df['nota_matematica'].astype(str).str.replace('.', ',')
df['nota_portugues'] = df['nota_portugues'].astype(str).str.replace('.', ',')




#padronizaçao dos sexos
df['sexo'] = df['sexo'].replace({
    'F': 'Feminino',
    'M': 'Masculino', 
    'fem': 'Feminino', 
    'masc': 'Masculino'})

df.to_excel("dados_tratados.xlsx", index=False)
