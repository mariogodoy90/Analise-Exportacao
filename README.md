# Análise de Exportação de Vinhos do Brasil

Este projeto foi desenvolvido como parte da Fase 1 da Pós-Graduação em Data Analytics da FIAP. Ele utiliza dados de exportação de vinhos do Brasil para realizar uma análise detalhada e fornecer insights sobre as tendências de exportação nos últimos 15 anos. A aplicação foi desenvolvida utilizando Streamlit para visualização interativa.

## Funcionalidades

- **Análise Geral**: Visualização dos dados de exportação de vinhos em litros e dólares por ano.
- **Previsão de Exportação**: Projeções para os próximos 5 anos com base em modelos estatísticos.
- **Top 10 Países**: Identificação dos principais mercados em termos de volume e valor das exportações.
- **Análise por País**: Detalhamento dos dados de exportação por país, com visualizações e previsões específicas.
- **Comparação entre Países**: Comparação das exportações entre diferentes países selecionados.

## Estrutura do Projeto

- `data_processing.py`: Funções para carregar e processar os dados de exportação e climáticos.
- `forecasting.py`: Funções para previsão de dados futuros utilizando o modelo Holt-Winters.
- `visualization.py`: Funções para criação de gráficos e visualizações.
- `interface.py`: Script principal que define a interface do Streamlit e organiza as análises.

## Exemplo de Utilização

A aplicação possui várias abas, cada uma oferecendo uma análise diferente:

- **Análise Geral**: Visualização do total de exportações em litros e dólares, previsões e principais mercados.
- **Análise por País**: Detalhamento das exportações para um país selecionado.
- **Comparar Países**: Comparação das exportações entre países selecionados.
