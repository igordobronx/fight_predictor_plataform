import sqlite3
import pandas as pd
import os


DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__)) if '__file__' in locals() else '.'

caminho_features = os.path.join(DIRETORIO_ATUAL, "fighters_features.csv")
caminho_fights = os.path.join(DIRETORIO_ATUAL, "fights_features.csv")

conn = sqlite3.connect(os.path.join(DIRETORIO_ATUAL, "ufc_predictor.db"))

print("criando/migrando banco de dados ")

if os.path.exists(caminho_features):
    df_fighters = pd.read_csv(caminho_features)
    df_fighters.to_sql("fighters", conn, if_exists="replace", index=False)
    print(" -> Tabela 'fighters' criada com sucesso!")
else:
    print("Error: 'fighters_features.csv' não foi encontrado. Rode o script de limpeza primeiro.")

if os.path.exists(caminho_fights):
    df_fights = pd.read_csv(caminho_fights)
    df_fights.to_sql("fights", conn, if_exists="replace", index=False)
    print(" -> Tabela 'fights' criada com sucesso!")
else:
    print("Error: 'fights_features.csv' não foi encontrado. Rode o script de cruzamento de lutas primeiro.")

conn.close()
print("migration completed.")