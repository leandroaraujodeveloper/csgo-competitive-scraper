# Web scraping de dados do cenário competitivo do jogo Counter Strike Global Ofensive
Neste repositório estão os dados de times e partidas do jogo csgo. Se você contribuir com a atualização alguns dos proximos passos estarão elencados aqui.

## Instalação
Baixe o repositorio localmente.

    git clone https://github.com/leandroaraujodeveloper/csgo-competitive-scraper.git
    cd csgo-competitive-scraper

Instale as dependencias.

    pip install -r requirements.txt

## Atualizando dados

Exemplo de geração de arquivo de dados da hltv

    scrapy crawl hltv_spider -o data/hltv_teams.json

## Objetivos

  - [x] Iniciar projeto com [Scrapy](https://www.scrapy.org)
  - [ ] Pegar dados do site [HLTV](https://www.hltv.org/)
    - [ ] Dados de times
    - [ ] Dados de partidas
    - [ ] Dados do ranking
    - [ ] Dados de jogadores
  - [ ] Pegar dados do site [Liquidpedia](https://liquipedia.net/counterstrike/Main_Page)
    - [ ] Dados de times
    - [ ] Dados de partidas
    - [ ] Dados do ranking
    - [ ] Dados de jogadores
