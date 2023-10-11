#  Desafio beeMôn Felipe Antunes:

realizei as tasks utilizando python, postgre e docker. Extraio nome, ano, rating, diretores, escritores e atores dos filmes. Realizo o screenshot e salvo as png's na pasta raiz do diretório juntamente com os arquivos CSV e JSON. Realizo a inserção no banco e imprimo o data frame no output. O código principal está localizado no arquivo app.py, criei um arquivo de setup do banco e um outro arquivo a parte para rodar o script de forma agendada. O site escolhido foi o imdb: (https://www.imdb.com/chart/top/?ref_=nv_mv_250)
foi utilizado o python 3.9 na construção da aplicação.

Pontos sobre o código:
 - O usuário pode modificar a linha 135 de sintaxe( top_movie_links = extract_top_movie_links(2) ) para determinar o numero de filmes que deseja extrair do site. No exemplo fornecido estão sendo extraídos dois filmes.

Para rodar o código execute o comando : docker-compose up --build


bibliotecas usadas:
 - selenium
 - pandas
 - csv
 - json
 - logging
 - psycopg2
banco de dados relacional:
 - PostgreSQL (PgAdmin4)

Fluxo Principal
Se o script for executado como principal:

 - Inicia-se o WebDriver e registra-se o início desta atividade.
 - Extrai-se os links dos principais filmes do IMDB.
 - Para cada link extraído, coleta-se os detalhes do filme, adiciona-os a uma lista e tira-se um screenshot da página do filme.
 - Os detalhes coletados são salvos em arquivos JSON e CSV.
 - O WebDriver é encerrado.
 - Conecta-se ao banco de dados e insere-se os detalhes dos filmes.
 - Visualiza-se os dados inseridos usando o Pandas.
 - Finalmente, a conexão com o banco de dados é encerrada e registra-se o sucesso da operação.



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





