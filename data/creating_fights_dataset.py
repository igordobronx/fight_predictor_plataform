import pandas as pd

fights = pd.read_csv("data/raw_data/ufc_gold_dataset_final.csv")
features = pd.read_csv("data/fighters_features.csv")

#removendo nomes duplicados
features_unique = features.drop_duplicates(subset='fighter_name')

feat_cols = ['win_rate', 'ko_rate', 'sub_rate', 'striking_eff', 'grappling']
features_unique = features_unique.set_index("fighter_name")

features_dict = features_unique[feat_cols].to_dict(orient='index')

fight_records = []

#cruza cada luta com historico de performance de ambos lutadores e cria um dataset com as features de ambos os lutadores e o resultado da luta (vencedor)
for idx, row in fights.iterrows():
    f1, f2, winner = row['Fighter_1'], row['Fighter_2'], row['Winner']

    #ignora lutadores cujo nao tem features registradas
    if f1 not in features_dict or f2 not in features_dict or winner not in [f1, f2]:
        continue


    f1_feats = features_dict[f1]
    f2_feats = features_dict[f2]

    record = {
        "fighter_a": f1,
        "fighter_b": f2,

        "fighter_a_win_rate": f1_feats['win_rate'],
        "fighter_b_win_rate": f2_feats['win_rate'],

        "fighter_a_ko_rate": f1_feats['ko_rate'],
        "fighter_a_sub_rate": f1_feats['sub_rate'],
        "fighter_a_striking_eff": f1_feats['striking_eff'],
        "fighter_a_grappling": f1_feats['grappling'],

        "fighter_b_ko_rate": f2_feats['ko_rate'],
        "fighter_b_sub_rate": f2_feats['sub_rate'],
        "fighter_b_striking_eff": f2_feats['striking_eff'],
        "fighter_b_grappling": f2_feats['grappling'],

        "winner": 1 if winner == f1 else 0
    }
    fight_records.append(record)
    
    record_inv = {
        "fighter_a": f2,
        "fighter_b": f1,

        "fighter_a_win_rate": f2_feats['win_rate'],
        "fighter_b_win_rate": f1_feats['win_rate'],

        "fighter_a_ko_rate": f2_feats['ko_rate'],
        "fighter_a_sub_rate": f2_feats['sub_rate'],
        "fighter_a_striking_eff": f2_feats['striking_eff'],
        "fighter_a_grappling": f2_feats['grappling'],

        "fighter_b_ko_rate": f1_feats['ko_rate'],
        "fighter_b_sub_rate": f1_feats['sub_rate'],
        "fighter_b_striking_eff": f1_feats['striking_eff'],
        "fighter_b_grappling": f1_feats['grappling'],

        "winner": 1 if winner == f2 else 0
    }
    fight_records.append(record_inv)

    

fights_dataset = pd.DataFrame(fight_records)
fights_dataset.to_csv("fights_features.csv", index=False)

print("DAtaset de luta foi criado com sucesso.")