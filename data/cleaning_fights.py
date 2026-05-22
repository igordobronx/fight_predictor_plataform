import pandas as pd

f_stats = pd.read_csv("data/cleaned_data_fighter/fighters_stats.csv")
fights = pd.read_csv("data/ufc_gold_dataset_final.csv")

ufc_stats = {}

#iterrows -> percorre cada linha do dataset gigante de lutas, e para cada linha, pega o nome do lutador 1 e do lutador 2, e depois pega as estatisticas de cada um dos lutadores, e coloca em um dicionario com o nome do lutador como chave e as estatisticas como valor.
for index, row in fights.iterrows():
    f1 = row['Fighter_1']
    f2 = row['Fighter_2']
    winner = row['Winner']
    method = row['Method']

    for f in [f1,f2]:
        if f not in ufc_stats:
            ufc_stats[f] = {'ufc_wins': 0, 'ufc_losses': 0, 'ufc_kos': 0, 'ufc_submissions': 0 }

    if winner == f1:
        ufc_stats[f1]['ufc_wins'] += 1
        ufc_stats[f2]['ufc_losses'] += 1
        if method in ['KO/TKO', "TKO - Doctor's stoppage"]:
            ufc_stats[f1]['ufc_kos'] += 1
        elif method == 'Submission':
            ufc_stats[f1]['ufc_submissions'] += 1
    elif winner == f2:
        ufc_stats[f2]['ufc_wins'] += 1
        ufc_stats[f1]['ufc_losses'] += 1
        if method in ['KO/TKO', "TKO - Doctor's stoppage"]:
            ufc_stats[f2]['ufc_kos'] += 1
        elif method == 'Submission':
            ufc_stats[f2]['ufc_submissions'] += 1

#criar dataframe a partir do dicionario do ufc)stats
ufc_df = pd.DataFrame.from_dict(ufc_stats, orient='index').reset_index().rename(columns={'index': 'Nome'})

df_merged = pd.merge(f_stats, ufc_df, on='Nome', how='inner')

def clean_pct(val):
    if isinstance(val, str) and val.endswith('%'):
        return float(val.strip('%')) / 100
    return val

df_merged['td_acc_float'] = df_merged['TD_Acc'].apply(clean_pct)
df_merged['td_def_float'] = df_merged['TD_Def'].apply(clean_pct)

df_merged["win_rate"] = df_merged["ufc_wins"] / (df_merged["ufc_wins"] + df_merged["ufc_losses"] + 1e-6)
df_merged["ko_rate"] = df_merged["ufc_kos"] / (df_merged["ufc_wins"] + 1e-6)
df_merged["sub_rate"] = df_merged["ufc_submissions"] / (df_merged["ufc_wins"] + 1e-6)

#eficiencia na trocacao:
df_merged["striking_eff"] = df_merged["SLpM"] / (df_merged["SApM"] + 0.1)

#grappling eficiencia
df_merged["grappling"] = df_merged["td_acc_float"] * (1 - df_merged["td_def_float"])

#renomenado nome para fighter name para casar perfeitamente com o frontend limit do roadmap
df_merged = df_merged.rename(columns={'Nome': 'fighter_name'})

df_merged.to_csv('fighters_features.csv', index=False)