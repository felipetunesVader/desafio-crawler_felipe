#  Desafio beeMôn Felipe Antunes:

realizei as tasks utilizando python, postgre e docker. Extraio nome, ano, rating, diretores, escritores e atores dos filmes. Realizo o screenshot e salvo as png's na pasta raiz do diretório juntamente com os arquivos CSV e JSON. Realizo a inserção no banco e imprimo o data frame no output. O código principal está localizado no arquivo app.py, criei um arquivo de setup do banco e um outro arquivo a parte para rodar o script de forma agendada. O site escolhido foi o imdb: (https://www.imdb.com/chart/top/?ref_=nv_mv_250)
foi utilizado o python 3.9 na construção da aplicação.

bibliotecas usadas:
 - selenium
 - pandas
 - csv
 - json
 - logging
 - psycopg2

## Desafio:
Escolher uma dos sites abaixo para fazer o desafio

- [imdb.com](https://www.imdb.com/chart/top/?ref_=nv_mv_250)

### Minimo Entregável:

- Buscar dados de forma automatizada(script de linha de comando ou interface clicavel)   -- FEITO
- Padronizar os retornos de forma estruturada (json/csv) --  FEITO
- Sistema de logs de para acompanhamento da execução  -- FEITO
- Ter um prova da consulta (Screenshot) -- FEITO

### Pontos Extra para:

- Armazenamento dos resultados em um banco relacional ou não relacional -- FEITO
- fazer um dataframe que possibilite visualizar os resultados via pandas -- FEITO
- Trazer resultados de forma dinamica sem fixar caminhos no `xpath` -- FEITO
- Dockerizar a aplicação -- FEITO
- Conseguir agendar uma execução para um dia e horario. -- FEITO





