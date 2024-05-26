import streamlit as st
from data_processing import load_data, preprocess_data, filter_top_countries
from visualization import plot_bar_chart, plot_line_chart
from forecasting import forecast_data
from interface import analise_geral, analise_por_pais, comparar_paises

# Configurações iniciais
#st.set_page_config(page_title="Análise de Exportação de Vinhos", page_icon="🍷", layout="wide")

st.sidebar.title("Configurações")

ultimo_ano = st.sidebar.slider("Selecione o último ano", min_value=2000, max_value=2023, value=2023)
intervalo_anos = st.sidebar.slider("Selecione o intervalo de anos", min_value=1, max_value=15, value=15)
primeiro_ano = ultimo_ano - intervalo_anos + 1

# Barra de progresso
progress_bar = st.sidebar.progress(0)

# Carregando e processando os dados
progress_bar.progress(10)
df = load_data("exportacao/ExpVinho.csv", delimiter=';')

progress_bar.progress(40)
df_litros, df_dolares = preprocess_data(df, primeiro_ano, ultimo_ano)

progress_bar.progress(70)
df_litros, df_dolares = filter_top_countries(df_litros, df_dolares, top_n=20)

progress_bar.progress(100)

# Configuração das abas
tabs = st.tabs(["Análise Geral", "Análise por País", "Comparar Países"])

with tabs[0]:
    analise_geral(df_litros, df_dolares)

with tabs[1]:
    analise_por_pais(df_litros, df_dolares)

with tabs[2]:
    comparar_paises(df_litros, df_dolares)
