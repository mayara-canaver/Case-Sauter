import pandas as pd
import numpy as np

from google_play_scraper import reviews_all
from google.oauth2 import service_account

pd.options.display.max_columns = None

endereco = str(input("Entre com o endereco do app:\n"))

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

positivo.to_gbq(project_id="folkloric-rite-336521",
                destination_table="alexa_data.positivo",
                if_exists="replace")
