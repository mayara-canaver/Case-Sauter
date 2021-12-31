# Case Sauter

## Tarefa 01:

Nessa tarefa foi pedido para acessar as informações do Aplicativo da Alexa na Play Store e assim obter seus dados criando um novo dataset com separação dos valores de Score.

Foram criados então três arquivos com as avaliações negativas, neutras e positivas e visualizadas e analisadas no pandas_profiling como foi solicitado.

## Tarefa 02:

Nessa tarefa é solicitado a criação do banco de dados com as informações dos datasets que foi informado acima.

Foram criadas três tabelas então com as avaliações e contendo cinco colunas cada uma.

A biblioteca pandas_gbq da Google Cloud BigQuery foi utilizada para inserção desses dados.

## Tarefa 03:

Foi feita uma pipeline de todos os processos feitos do projeto, desde a parte de credenciamento de dados até a inserção dos dados no banco.

Também foi feita a automação do código onded o usuário possa inserir o link do app da Play Store.


## Bibliotecas

As seguintes bibliotecas /pacotes precisam ser instalados antes de rodar o projeto:

```bash
pip install numpy
pip install google-auth-oauthlib
pip install pandas
pip install pandas_gbq
pip install pandas_profiling
```
