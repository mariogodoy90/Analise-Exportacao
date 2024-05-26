import streamlit as st
from visualization import plot_bar_chart, plot_line_chart
from forecasting import forecast_data

# Configurando a página
#st.set_page_config(page_title="Análise de Exportação de Vinhos do Brasil", layout="wide")

# Adicionando estilo CSS para melhorar a aparência da interface
st.markdown("""
    <style>
    .main {
        background-color: #ffffff;
        padding: 10px;
    }
    h1, h2, h3 {
        color: #000000;
    }
    .stButton button {
        background-color: #007BFF;
        color: white;
        padding: 10px 24px;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        font-size: 14px;
    }
    .stButton button:hover {
        background-color: #0056b3;
    }
    .stDataFrame {
        border: 1px solid #ddd;
        border-radius: 4px;
        overflow: hidden;
    }
    .stDataFrame table {
        width: 100%;
        font-size: 12px;
        text-align: left;
        color: #000000;
    }
    .stDataFrame th, .stDataFrame td {
        padding: 8px;
    }
    .css-1v3fvcr .stTabs [data-baseweb="tab"] {
        color: #007BFF;
        background-color: #f0f0f0;
        font-size: 14px;
        border-radius: 4px 4px 0 0;
    }
    .css-1v3fvcr .stTabs [data-baseweb="tab"]:hover {
        color: #0056b3;
        background-color: #e0e0e0;
    }
    .css-1v3fvcr .stTabs [data-baseweb="tab"][aria-selected="true"] {
        color: white;
        background-color: #007BFF;
    }
    </style>
    """, unsafe_allow_html=True)

def analise_geral(df_litros, df_dolares):
    st.title('Análise de Exportação de Vinhos do Brasil')

    st.subheader('Total de Exportação por Ano (Litros)')
    st.write("Este gráfico mostra o total de exportação de vinhos em litros para cada ano nos últimos 15 anos.")
    total_litros = df_litros.set_index('País').sum().reset_index()
    total_litros.columns = ['Ano', 'Total Litros']
    total_litros['Ano'] = total_litros['Ano'].astype(int)
    plot_bar_chart(total_litros['Ano'], total_litros['Total Litros'], 'Ano', 'Total de Litros', 'Total de Exportação por Ano (em Litros)')

    st.subheader('Total de Exportação por Ano (Dólares)')
    st.write("Este gráfico mostra o total de exportação de vinhos em dólares para cada ano nos últimos 15 anos.")
    total_dolares = df_dolares.set_index('País').sum().reset_index()
    total_dolares.columns = ['Ano', 'Total Dólares']
    total_dolares['Ano'] = total_dolares['Ano'].astype(int)
    plot_bar_chart(total_dolares['Ano'], total_dolares['Total Dólares'], 'Ano', 'Total em Dólares', 'Total de Exportação por Ano (em Dólares)')

    if not total_litros.empty:
        st.subheader('Previsão de Exportação de Litros para os Próximos 5 Anos')
        st.write("Esta previsão mostra a estimativa de exportação de vinhos em litros para os próximos 5 anos.")
        forecast_litros = forecast_data(total_litros['Total Litros'])
        plot_line_chart(total_litros['Ano'], total_litros['Total Litros'], 'Ano', 'Litros', 'Previsão de Exportação de Litros', forecast_litros)

    if not total_dolares.empty:
        st.subheader('Previsão de Exportação em Dólares para os Próximos 5 Anos')
        st.write("Esta previsão mostra a estimativa de exportação de vinhos em dólares para os próximos 5 anos.")
        forecast_dolares = forecast_data(total_dolares['Total Dólares'])
        plot_line_chart(total_dolares['Ano'], total_dolares['Total Dólares'], 'Ano', 'Dólares', 'Previsão de Exportação em Dólares', forecast_dolares)

    st.subheader('Top 10 Países por Exportação de Vinho (Litros)')
    st.write("Esta tabela mostra os 10 principais países em termos de exportação de vinhos em litros nos últimos 15 anos.")
    exp_por_pais_litros = df_litros.groupby('País').sum().sum(axis=1).sort_values(ascending=False).head(10).reset_index()
    exp_por_pais_litros.columns = ['País', 'Total Litros']
    st.dataframe(exp_por_pais_litros.style.format({'Total Litros': '{:,.0f}'.format}))

    st.subheader('Top 10 Países por Exportação de Vinho (Dólares)')
    st.write("Esta tabela mostra os 10 principais países em termos de exportação de vinhos em dólares nos últimos 15 anos.")
    exp_por_pais_dolares = df_dolares.groupby('País').sum().sum(axis=1).sort_values(ascending=False).head(10).reset_index()
    exp_por_pais_dolares.columns = ['País', 'Total Dólares']
    st.dataframe(exp_por_pais_dolares.style.format({'Total Dólares': '${:,.0f}'.format}))

def analise_por_pais(df_litros, df_dolares):
    st.title('Análise de Exportação por País')

    paises = df_litros['País'].unique()
    pais_selecionado = st.selectbox('Selecione o País', paises)
    
    df_litros_pais = df_litros[df_litros['País'] == pais_selecionado].drop(columns=['País'])
    df_dolares_pais = df_dolares[df_dolares['País'] == pais_selecionado].drop(columns=['País'])
    
    if not df_litros_pais.empty:
        st.subheader(f'Exportação de Vinhos para {pais_selecionado} (Litros)')
        st.write(f"Este gráfico mostra o total de exportação de vinhos em litros para {pais_selecionado} nos últimos 15 anos.")
        plot_bar_chart(df_litros_pais.columns.astype(int), df_litros_pais.iloc[0], 'Ano', 'Litros', f'Exportação de Vinhos para {pais_selecionado} (Litros)')
        
        forecast_litros_pais = forecast_data(df_litros_pais.iloc[0])
        st.subheader(f'Previsão de Exportação de Litros para {pais_selecionado}')
        st.write(f"Esta previsão mostra a estimativa de exportação de vinhos em litros para {pais_selecionado} nos próximos 5 anos.")
        plot_line_chart(df_litros_pais.columns.astype(int), df_litros_pais.iloc[0], 'Ano', 'Litros', f'Previsão de Exportação de Litros para {pais_selecionado}', forecast_litros_pais)
    
    if not df_dolares_pais.empty:
        st.subheader(f'Exportação de Vinhos para {pais_selecionado} (Dólares)')
        st.write(f"Este gráfico mostra o total de exportação de vinhos em dólares para {pais_selecionado} nos últimos 15 anos.")
        plot_bar_chart(df_dolares_pais.columns.astype(int), df_dolares_pais.iloc[0], 'Ano', 'Dólares', f'Exportação de Vinhos para {pais_selecionado} (Dólares)')
        
        forecast_dolares_pais = forecast_data(df_dolares_pais.iloc[0])
        st.subheader(f'Previsão de Exportação em Dólares para {pais_selecionado}')
        st.write(f"Esta previsão mostra a estimativa de exportação de vinhos em dólares para {pais_selecionado} nos próximos 5 anos.")
        plot_line_chart(df_dolares_pais.columns.astype(int), df_dolares_pais.iloc[0], 'Ano', 'Dólares', f'Previsão de Exportação em Dólares para {pais_selecionado}', forecast_dolares_pais)

def comparar_paises(df_litros, df_dolares):
    st.title('Comparar Exportação entre Países')

    paises = df_litros['País'].unique()
    paises_selecionados = st.multiselect('Selecione os Países', paises)
    
    if len(paises_selecionados) >= 2:
        df_litros_selecionados = df_litros[df_litros['País'].isin(paises_selecionados)]
        df_dolares_selecionados = df_dolares[df_dolares['País'].isin(paises_selecionados)]
        
        if not df_litros_selecionados.empty:
            st.subheader('Comparação de Exportação de Litros')
            for pais in paises_selecionados:
                df_pais = df_litros_selecionados[df_litros_selecionados['País'] == pais].drop(columns=['País'])
                plot_bar_chart(df_pais.columns.astype(int), df_pais.iloc[0], 'Ano', 'Litros', f'Exportação de Vinhos para {pais}')
        
        if not df_dolares_selecionados.empty:
            st.subheader('Comparação de Exportação em Dólares')
            for pais in paises_selecionados:
                df_pais = df_dolares_selecionados[df_dolares_selecionados['País'] == pais].drop(columns=['País'])
                plot_bar_chart(df_pais.columns.astype(int), df_pais.iloc[0], 'Ano', 'Dólares', f'Exportação de Vinhos para {pais}')
