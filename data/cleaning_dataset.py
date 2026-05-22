import pandas as pd

# Carrega o arquivo limpo
df = pd.read_csv('data/ufc_fighters_cleaned.csv')

# 1. Criar o DataFrame de Informações (Identificação)
df_info = df[['Nome', 'DOB', 'Fighter_URL']]
df_info.to_csv('data/fighters_info.csv', index=False)

# 2. Criar o DataFrame de Físicos
df_fisico = df[['Nome', 'Height', 'Altura_cm', 'Weight', 'Reach', 'Stance']]
df_fisico.to_csv('data/fighters_physical.csv', index=False)

# 3. Criar o DataFrame de Estatísticas
cols_stats = ['Nome', 'Vitorias', 'Derrotas', 'Draws', 'SLpM', 'Str_Acc', 
              'SApM', 'Str_Def', 'TD_Avg', 'TD_Acc', 'TD_Def', 'Sub_Avg']
df_stats = df[cols_stats]
df_stats.to_csv('fighters_stats.csv', index=False)

print("Arquivos criados com sucesso: fighters_info.csv, fighters_physical.csv, fighters_stats.csv")