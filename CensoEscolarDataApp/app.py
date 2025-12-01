import pandas as pd
arquivo_csv = '/home/kemelynfigueiredo/Downloads/microdados_censo_escolar_2024/dados/microdados_ed_basica_2024.csv'



colunas = {
    'NO_ENTIDADE': 'no_entidade', 
    'CO_ENTIDADE': 'co_entidade',
    'NO_UF': 'no_uf', 
    'SG_UF': 'sg_uf', 
    'CO_UF': 'co_uf',
    'NO_MUNICIPIO': 'no_municipio', 
    'CO_MUNICIPIO': 'co_municipio',
    'NO_MESORREGIAO': 'no_mesorregiao', 
    'CO_MESORREGIAO': 'co_mesorregiao',
    'NO_MICRORREGIAO': 'no_microrregiao', 
    'CO_MICRORREGIAO': 'co_microrregiao',
    'NU_ANO_CENSO': 'nu_ano_censo', 
    'NO_REGIAO': 'no_regiao', 
    'CO_REGIAO': 'co_regiao',
    'QT_MAT_BAS': 'qt_mat_bas', 
    'QT_MAT_INF': 'qt_mat_inf',
    'QT_MAT_FUND': 'qt_mat_fund', 
    'QT_MAT_MED': 'qt_mat_med',
    'QT_MAT_PROF': 'qt_mat_prof', 
    'QT_MAT_EJA': 'qt_mat_eja',
    'QT_MAT_ESP': 'qt_mat_esp'
}

df = pd.read_csv(arquivo_csv, encoding='ISO-8859-1', sep=';', low_memory=False)

# Mantém apenas colunas que existem no arquivo
colunas_existentes = {orig: novo for orig, novo in colunas.items() if orig in df.columns}

# Renomeia as colunas existentes
df = df.rename(columns=colunas_existentes)

df = df[list(colunas_existentes.values())]


id_alvo = 25   
coluna_id = "co_uf" 


df_filtrado = df[df[coluna_id] == id_alvo]


arquivo_json = "dados_filtrados.json"
df_filtrado.to_json(arquivo_json, orient="records", force_ascii=False, indent=4)

print("Arquivo JSON criado com sucesso:", arquivo_json)