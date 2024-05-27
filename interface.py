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
    st.write("""
    Nos últimos 15 anos, a exportação de vinhos do Brasil apresentou diversas variações. O gráfico a seguir ilustra a quantidade total de vinhos exportados em litros, ano após ano.
    Observar essas variações nos permite entender melhor as tendências e flutuações no mercado internacional de vinhos brasileiros.
    """)
    total_litros = df_litros.set_index('País').sum().reset_index()
    total_litros.columns = ['Ano', 'Total Litros']
    total_litros['Ano'] = total_litros['Ano'].astype(int)
    plot_bar_chart(total_litros['Ano'], total_litros['Total Litros'], 'Ano', 'Total de Litros', 'Total de Exportação por Ano (em Litros)')

    st.subheader('Total de Exportação por Ano (Dólares)')
    st.write("""
    Além da quantidade exportada, é crucial analisarmos o valor monetário das exportações. Este gráfico apresenta o total das exportações de vinhos em dólares,
    permitindo uma visão clara sobre a contribuição financeira das exportações de vinhos para a economia brasileira.
    """)
    total_dolares = df_dolares.set_index('País').sum().reset_index()
    total_dolares.columns = ['Ano', 'Total Dólares']
    total_dolares['Ano'] = total_dolares['Ano'].astype(int)
    plot_bar_chart(total_dolares['Ano'], total_dolares['Total Dólares'], 'Ano', 'Total em Dólares', 'Total de Exportação por Ano (em Dólares)')

    if not total_litros.empty:
        st.subheader('Previsão de Exportação de Litros para os Próximos 5 Anos')
        st.write("""
        Olhando para o futuro, podemos prever como as exportações de vinhos em litros podem se comportar nos próximos cinco anos.
        A previsão a seguir é baseada em modelos estatísticos e oferece uma visão sobre possíveis tendências futuras, ajudando a planejar estratégias de mercado.
        """)
        forecast_litros = forecast_data(total_litros['Total Litros'])
        plot_line_chart(total_litros['Ano'], total_litros['Total Litros'], 'Ano', 'Litros', 'Previsão de Exportação de Litros', forecast_litros)

    if not total_dolares.empty:
        st.subheader('Previsão de Exportação em Dólares para os Próximos 5 Anos')
        st.write("""
        Similarmente, prever o valor financeiro das exportações nos próximos cinco anos é essencial para entender o impacto econômico.
        A previsão a seguir fornece uma perspectiva sobre como o mercado pode se comportar financeiramente, ajudando na tomada de decisões estratégicas.
        """)
        forecast_dolares = forecast_data(total_dolares['Total Dólares'])
        plot_line_chart(total_dolares['Ano'], total_dolares['Total Dólares'], 'Ano', 'Dólares', 'Previsão de Exportação em Dólares', forecast_dolares)

    st.subheader('Top 10 Países por Exportação de Vinho (Litros)')
    st.write("""
    Vamos agora analisar os principais destinos dos vinhos brasileiros. Esta tabela apresenta os 10 principais países em termos de volume de exportação (em litros).
    Identificar esses mercados chave nos ajuda a focar nossos esforços em manter e expandir essas relações comerciais.
    """)
    exp_por_pais_litros = df_litros.groupby('País').sum().sum(axis=1).sort_values(ascending=False).head(10).reset_index()
    exp_por_pais_litros.columns = ['País', 'Total Litros']
    st.dataframe(exp_por_pais_litros.style.format({'Total Litros': '{:,.0f}'.format}))

    st.subheader('Top 10 Países por Exportação de Vinho (Dólares)')
    st.write("""
    Além do volume, é importante saber quais países estão gerando mais receita com a exportação de vinhos brasileiros.
    Esta tabela mostra os 10 principais países em termos de valor exportado (em dólares), destacando os mercados mais lucrativos.
    """)
    exp_por_pais_dolares = df_dolares.groupby('País').sum().sum(axis=1).sort_values(ascending=False).head(10).reset_index()
    exp_por_pais_dolares.columns = ['País', 'Total Dólares']
    st.dataframe(exp_por_pais_dolares.style.format({'Total Dólares': '${:,.0f}'.format}))


    st.header('Sugestões para Melhoria das Exportações de Vinho')
    st.write("""
    1. **Diversificação de Mercados**: Identificar e investir em mercados emergentes que possuem potencial de crescimento no consumo de vinhos.
    2. **Marketing e Branding**: Valorização das safras brasileiras através de divulgação do processo de fabricação e destacando o crescimento da exportação em países desenvolvidos e com cultura de vinhos próprios. Aumentar os esforços de marketing internacional para promover a marca dos vinhos brasileiros.
    3. **Qualidade e Inovação**: Investir na qualidade dos vinhos e na inovação dos processos de produção para atender às exigências dos mercados internacionais. Aprimorar os processos de fabricação para que os níveis de exportação para países desenvolvidos voltem ao que foram no início da produção em 2015, recuperando esse potencial.
    4. **Parcerias e Acordos Comerciais**: Estabelecer parcerias e acordos comerciais que facilitem o acesso a novos mercados e reduzam as barreiras tarifárias.
    5. **Sustentabilidade**: Implementar práticas sustentáveis na produção de vinhos, que são valorizadas pelos consumidores globais.
    """)

def analise_por_pais(df_litros, df_dolares):
    st.title('Análise de Exportação por País')

    st.write("""
    Explore as exportações de vinhos do Brasil por país. Selecione um país da lista abaixo para ver os dados detalhados de exportação em litros e dólares,
    além de previsões para os próximos anos.
    """)

    paises = df_litros['País'].unique()
    pais_selecionado = st.selectbox('Selecione o País', paises)
    
    df_litros_pais = df_litros[df_litros['País'] == pais_selecionado].drop(columns=['País'])
    df_dolares_pais = df_dolares[df_dolares['País'] == pais_selecionado].drop(columns=['País'])
    
    if not df_litros_pais.empty:
        st.subheader(f'Exportação de Vinhos para {pais_selecionado} (Litros)')
        st.write(f"""
        O gráfico abaixo apresenta a quantidade total de vinhos exportados para {pais_selecionado} em litros, ao longo dos últimos 15 anos.
        Essa visualização ajuda a identificar as tendências de consumo e a evolução das exportações para esse mercado específico.
        """)
        plot_bar_chart(df_litros_pais.columns.astype(int), df_litros_pais.iloc[0], 'Ano', 'Litros', f'Exportação de Vinhos para {pais_selecionado} (Litros)')
        
        st.subheader(f'Previsão de Exportação de Litros para {pais_selecionado}')
        st.write(f"""
        Baseado nos dados históricos, projetamos a quantidade de vinhos que será exportada para {pais_selecionado} nos próximos 5 anos.
        Essas previsões são cruciais para planejar estratégias de mercado e ajustar a produção conforme a demanda esperada.
        """)
        forecast_litros_pais = forecast_data(df_litros_pais.iloc[0])
        plot_line_chart(df_litros_pais.columns.astype(int), df_litros_pais.iloc[0], 'Ano', 'Litros', f'Previsão de Exportação de Litros para {pais_selecionado}', forecast_litros_pais)
    
    if not df_dolares_pais.empty:
        st.subheader(f'Exportação de Vinhos para {pais_selecionado} (Dólares)')
        st.write(f"""
        Este gráfico mostra o valor total das exportações de vinhos para {pais_selecionado} em dólares, ao longo dos últimos 15 anos.
        Analisar esses dados financeiros nos permite entender melhor a importância econômica desse mercado para o Brasil.
        """)
        plot_bar_chart(df_dolares_pais.columns.astype(int), df_dolares_pais.iloc[0], 'Ano', 'Dólares', f'Exportação de Vinhos para {pais_selecionado} (Dólares)')
        
        st.subheader(f'Previsão de Exportação em Dólares para {pais_selecionado}')
        st.write(f"""
        As previsões abaixo mostram a estimativa de valor em dólares das exportações de vinhos para {pais_selecionado} nos próximos 5 anos.
        Com essas informações, podemos planejar ações para maximizar a receita e fortalecer a presença do vinho brasileiro nesse mercado.
        """)
        forecast_dolares_pais = forecast_data(df_dolares_pais.iloc[0])
        plot_line_chart(df_dolares_pais.columns.astype(int), df_dolares_pais.iloc[0], 'Ano', 'Dólares', f'Previsão de Exportação em Dólares para {pais_selecionado}', forecast_dolares_pais)


def comparar_paises(df_litros, df_dolares):
    st.title('Comparar Exportação entre Países')

    st.write("""
    Compare as exportações de vinhos do Brasil entre diferentes países. Selecione dois ou mais países da lista abaixo para ver os dados detalhados de exportação em litros e dólares.
    Esta comparação ajuda a identificar quais mercados são mais fortes e quais têm potencial para crescimento.
    """)

    paises = df_litros['País'].unique()
    paises_selecionados = st.multiselect('Selecione os Países', paises)
    
    if len(paises_selecionados) >= 2:
        df_litros_selecionados = df_litros[df_litros['País'].isin(paises_selecionados)]
        df_dolares_selecionados = df_dolares[df_dolares['País'].isin(paises_selecionados)]
        
        if not df_litros_selecionados.empty:
            st.subheader('Comparação de Exportação de Litros')
            st.write("""
            O gráfico abaixo mostra a comparação da quantidade de vinhos exportados em litros para os países selecionados, ao longo dos últimos 15 anos.
            Essa visualização permite identificar quais mercados importam mais vinhos brasileiros e como essas exportações têm evoluído.
            """)
            for pais in paises_selecionados:
                df_pais = df_litros_selecionados[df_litros_selecionados['País'] == pais].drop(columns=['País'])
                plot_bar_chart(df_pais.columns.astype(int), df_pais.iloc[0], 'Ano', 'Litros', f'Exportação de Vinhos para {pais}')
        
        if not df_dolares_selecionados.empty:
            st.subheader('Comparação de Exportação em Dólares')
            st.write("""
            Este gráfico mostra a comparação do valor das exportações de vinhos em dólares para os países selecionados, ao longo dos últimos 15 anos.
            Analisar essas informações financeiras ajuda a entender melhor a contribuição econômica de cada mercado para o Brasil.
            """)
            for pais in paises_selecionados:
                df_pais = df_dolares_selecionados[df_dolares_selecionados['País'] == pais].drop(columns=['País'])
                plot_bar_chart(df_pais.columns.astype(int), df_pais.iloc[0], 'Ano', 'Dólares', f'Exportação de Vinhos para {pais}')
    else:
        st.write("Por favor, selecione pelo menos dois países para comparar as exportações.")

