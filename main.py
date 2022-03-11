import pandas as pd
import numpy as np
import os

from google_play_scraper import reviews_all
from google.oauth2 import service_account
from dotenv import load_dotenv

pd.options.display.max_columns = None

load_dotenv()

id = os.getenv("ID")

endereco = str(input("Entre com o endereco do app:\n"))

# REQUISIÇÃO DOS DADOS DO APP ESCOLHIDO PELO USUÁRIO
app = reviews_all(
    endereco,
    lang="pt",
    country="br"
)

app_df = pd.DataFrame.from_dict(app)

app_df = app_df.drop(["reviewId", "userName", "userImage", "replyContent", "repliedAt"], axis=1)

app_df.columns = [x.upper() for x in app_df.columns]

app_df["CONTENT"] = app_df["CONTENT"].str.strip()
app_df["CONTENT"] = app_df["CONTENT"].str.upper()
app_df["CONTENT"] = app_df["CONTENT"].replace('"', '\"')

cols = app_df.select_dtypes(include=[np.object]).columns
app_df[cols] = app_df[cols].apply(lambda x: x.str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8'))

app_df = app_df.dropna()

# SEPARAÇÃO DOS ARQUIVOS DE ACORDO COM O SCORE (POSITIVO, NEUTRO E NEGATIVO)
# RETIRA-SE OS 10 ULTIMOS REGISTROS DE CADA ARQUIVO, PARA EVITAR DADO FALTANTE
positivo = app_df.loc[app_df["SCORE"] >= 4]
positivo = positivo[:-10]

neutro = app_df.loc[app_df["SCORE"] == 3]
neutro = neutro[:-10]

negativo = app_df.loc[app_df["SCORE"] < 3]
negativo = negativo[:-10]

positivo.to_csv(r"/Desktop/positivo.csv", index=False)
neutro.to_csv(r"/Desktop/neutro.csv", index=False)
negativo.to_csv(r"/Desktop/negativo.csv", index=False)

key_path = "GBQ.json"

credentials = service_account.Credentials.from_service_account_file(
    key_path, scopes=["https://www.googleapis.com/auth/cloud-plataform"]
)

lista_nome_tabela, lista_dataset = ["positivo", "neutro", "negativo"], [positivo, neutro, negativo]

for dataset, nome_tabela in zip(lista_dataset, lista_nome_tabela):
    dataset.to_gbq(project_id=id,
                   destination_table="banco." + nome_tabela,
                   if_exists="replace")

    dataset.to_csv(r"/Desktop/" + nome_tabela + " .csv", index=False)
