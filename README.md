# 📘 Web Scraper de Livros (Data Science Category)

Este projeto é um **Web Scraper automatizado** que coleta dados de livros da categoria **Data Science** do site [Books To Scrape](https://books.toscrape.com). Ele realiza:

- Coleta dos títulos e preços dos livros.
- Geração de arquivo CSV com os dados.
- Criação de gráfico com a distribuição de preços.
- Dashboard automático com análise exploratória dos dados.
- Agendamento diário do scraping às 09:00 da manhã.

---

## 🚀 Tecnologias Utilizadas

- Python 3
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/)
- [Requests](https://docs.python-requests.org/)
- [Pandas](https://pandas.pydata.org/)
- [Seaborn + Matplotlib](https://seaborn.pydata.org/)
- [YData Profiling](https://docs.ydata.ai/docs/profiling)
- [Schedule](https://schedule.readthedocs.io/en/stable/)
- Replit (ambiente de desenvolvimento online)

---

## ⚙️ Como Usar o Projeto

```bash
git clone https://github.com/GustaSantos-Dev/web-scraper-livros.git
cd web-scraper-livros

2. Instalar as Dependências

pip install -r requirements.txt

3. Executar o Script

python scraping.py


⏰ Agendamento Automático
O script utiliza a biblioteca schedule para rodar automaticamente todos os dias às 09:00.

O loop fica ativo continuamente até que você pressione Ctrl + C.

📁 Estrutura de Saída
Ao executar o script, ele irá gerar:

livros_YYYY-MM-DD_HH-MM-SS.csv: Arquivo com todos os livros coletados.

grafico_precos.png: Gráfico com a distribuição dos preços.

dashboard_livros.html: Dashboard interativo com estatísticas automáticas dos dados.


📂 Organização do Projeto
bash
Copiar
Editar
web-scraper-livros/
├── scraping.py             # Código principal
├── README.md               # Este arquivo
├── .gitignore              # Ignora arquivos temporários
├── requirements.txt        # Dependências do projeto
├── dados/                  # (opcional) CSVs salvos
├── imagens/                # (opcional) gráficos gerados
└── dashboard/              # (opcional) dashboards gerados



🧪 Exemplo de Uso
yaml
Copiar
Editar
📄 Coletando: https://books.toscrape.com/catalogue/category/books/data-science_22/index.html
📁 CSV salvo como: livros_2025-04-05_09-00-00.csv
📈 Gráfico salvo como: grafico_precos.png
📊 Dashboard salvo como: dashboard_livros.html
✅ Processo completo com sucesso!



🧑‍💻 Autor
Gustavo Reis
Desenvolvedor em formação e entusiasta em automações Python para dados.

GitHub: @GustaSantos-Dev
