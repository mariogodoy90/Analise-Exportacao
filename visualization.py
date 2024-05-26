import matplotlib.pyplot as plt
import streamlit as st

def formatar_valor(x, pos):
    return '{:,.0f}'.format(x).replace(',', '.')

def plot_bar_chart(x, y, x_label, y_label, title):
    fig, ax = plt.subplots(figsize=(8, 4))  # Tamanho ajustado para se adaptar melhor
    ax.bar(x, y, color='#6fa8dc', edgecolor='black')
    ax.set_xlabel(x_label, fontsize=10)
    ax.set_ylabel(y_label, fontsize=10)
    ax.set_title(title, fontsize=12, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(x, rotation=45, ha="right", fontsize=8)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(formatar_valor))
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    st.pyplot(fig)

def plot_line_chart(x, y, x_label, y_label, title, forecast=None):
    fig, ax = plt.subplots(figsize=(8, 4))  # Tamanho ajustado para se adaptar melhor
    ax.plot(x, y, marker='o', color='#f6b26b', label='Real')
    if forecast is not None:
        x_list = x.tolist()
        forecast_years = list(range(int(x_list[-1]) + 1, int(x_list[-1]) + 1 + len(forecast)))
        ax.plot(forecast_years, forecast, marker='o', color='#93c47d', label='Previsão')
    
    all_years = list(map(int, x)) + forecast_years if forecast is not None else list(map(int, x))
       
    ax.set_xlabel(x_label, fontsize=10)
    ax.set_ylabel(y_label, fontsize=10)
    ax.set_title(title, fontsize=12, fontweight='bold')
    ax.set_xticks(all_years)
    ax.set_xticklabels(all_years, rotation=45, ha="right", fontsize=8)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(formatar_valor))
    ax.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    st.pyplot(fig)
