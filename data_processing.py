import pandas as pd
import re

def load_data(file_path, delimiter):
    return pd.read_csv(file_path, delimiter=delimiter)

def preprocess_data(df, primeiro_ano, ultimo_ano):
    anos_interesse = [str(ano) for ano in range(primeiro_ano, ultimo_ano + 1)]
    
    litros_cols = ['País'] + [col for col in anos_interesse if col in df.columns]
    dolares_cols = ['País'] + [f"{ano}.1" for ano in anos_interesse if f"{ano}.1" in df.columns]
    
    df_litros = df[litros_cols]
    df_dolares = df[dolares_cols]

    # Removendo sufixo .1 das colunas do df_dolares
    df_dolares.columns = [re.sub(r'\.1$', '', col) for col in df_dolares.columns]

    # Filtrando países sem dados
    df_litros = df_litros[(df_litros.drop(columns=['País']) != 0).any(axis=1)]
    df_dolares = df_dolares[(df_dolares.drop(columns=['País']) != 0).any(axis=1)]

    df_litros, df_dolares = filter_top_countries(df_litros, df_dolares)
    
    return df_litros, df_dolares

def filter_top_countries(df_litros, df_dolares, top_n=20):
    # Selecionar os top N países por litros exportados
    top_countries = df_litros.set_index('País').sum(axis=1).nlargest(top_n).index
    df_litros_top = df_litros[df_litros['País'].isin(top_countries)]
    df_dolares_top = df_dolares[df_dolares['País'].isin(top_countries)]
    
    return df_litros_top, df_dolares_top
