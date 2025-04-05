import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from ydata_profiling import ProfileReport  # Atualização da importação
from datetime import datetime
import schedule
import time

# 📥 Coleta o conteúdo HTML de uma URL
def pegar_html(url):
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            return resposta.text
        else:
            print(f"Erro ao acessar o site: {resposta.status_code}")
            return None
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return None

# 🔍 Extrai livros do HTML
def coletar_livros(html):
    soup = BeautifulSoup(html, "html.parser")
    livros = []
    itens = soup.find_all("article", class_="product_pod")

    for item in itens:
        titulo = item.h3.a["title"]
        preco = item.find("p", class_="price_color").text
        livros.append({"Título": titulo, "Preço": preco})

    return livros

# ➡️ Verifica se há próxima página
def encontrar_proxima_pagina(soup):
    next_button = soup.find("li", class_="next")
    if next_button:
        return next_button.a["href"]
    return None

# 🔁 Faz scraping de várias páginas
def scraping_varias_paginas():
    base_url = "https://books.toscrape.com/catalogue/category/books/data-science_22/"
    url = base_url + "index.html"
    livros_coletados = []

    while url:
        print(f"📄 Coletando: {url}")
        html = pegar_html(url)
        if html:
            soup = BeautifulSoup(html, "html.parser")
            livros = coletar_livros(html)
            livros_coletados.extend(livros)
            proxima = encontrar_proxima_pagina(soup)
            url = base_url + proxima if proxima else None
        else:
            break

    return livros_coletados

# 💾 Salva em CSV
def salvar_em_csv(lista):
    agora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nome = f"livros_{agora}.csv"
    df = pd.DataFrame(lista)
    df.to_csv(nome, index=False)
    print(f"📁 CSV salvo como: {nome}")
    return nome

# 📊 Gera gráfico com Seaborn
def gerar_grafico(lista):
    df = pd.DataFrame(lista)
    df["Preço"] = df["Preço"].str.replace("£", "").astype(float)

    plt.figure(figsize=(10, 5))
    sns.histplot(df["Preço"], bins=10, kde=True, color="skyblue")
    plt.title("Distribuição de Preços dos Livros")
    plt.xlabel("Preço (£)")
    plt.ylabel("Frequência")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("grafico_precos.png")
    print("📈 Gráfico salvo como: grafico_precos.png")

# 📋 Gera dashboard automático
def gerar_dashboard(nome_arquivo_csv):
    df = pd.read_csv(nome_arquivo_csv)
    df["Preço"] = df["Preço"].str.replace("£", "").astype(float)

    profile = ProfileReport(df, title="Análise de Livros", explorative=True)
    profile.to_file("dashboard_livros.html")
    print("📊 Dashboard salvo como: dashboard_livros.html")

# 🚀 Função principal
def main():
    print("🔍 Iniciando scraping...")
    livros = scraping_varias_paginas()
    if livros:
        arquivo_csv = salvar_em_csv(livros)
        gerar_grafico(livros)
        gerar_dashboard(arquivo_csv)
        print("✅ Processo completo com sucesso!")
    else:
        print("⚠️ Nenhum dado encontrado.")

# ⏱️ Agendamento diário
schedule.every().day.at("09:00").do(main)

# 🔁 Loop contínuo
print("⏳ Sistema de scraping agendado. Pressione Ctrl+C para parar.")
while True:
    schedule.run_pending()
    time.sleep(60)

