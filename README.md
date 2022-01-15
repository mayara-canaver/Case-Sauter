# EN/en

## Introduction

The Alexa Brasil main page is scraped on the Play Store, where the objective is to download all the data found and after that perform a treatment and then do the analysis.

The analysis takes place through the Jupyter Notebook using the Pandas Profiling library, which already shows us several statistical observations of the variables.

The algorithm also allows for generalization, where you can enter the Play Store address and get the data from whichever app you want, since the fields are generalized.

A connection is also made to BigQuery where we can store the data and visualize it when necessary.

## Libraries

The following libraries/packages need to be installed before running the project:

```bash
pip install numpy
pip install google-auth-oauthlib
pip install pandas
pip install pandas_gbq
pip install pandas_profiling
```


# PT/br

## Introdução

É feito o scraping da página principal da Alexa Brasil na Play Store, onde o objetivo é baixar todos os dados encontrados e após isso realizar um tratamento e então fazer a análise.

A análise ocorre através do Jupyter Notebook utilizando a biblioteca Pandas Profiling, a qual já nos mostra várias observações estatísticas das variáveis.

O algoritmo também permite a generalização, onde você pode inserir o endereço da Play Store e assim obter o dado de qual app quiser, já que os campos são generalizados.

Também é feita uma conexão com o BigQuery onde podemos armazenar os dados e fazer a visualização deles quando necessário.

## Bibliotecas

As seguintes bibliotecas /pacotes precisam ser instalados antes de rodar o projeto:

```bash
pip install numpy
pip install google-auth-oauthlib
pip install pandas
pip install pandas_gbq
pip install pandas_profiling
```
