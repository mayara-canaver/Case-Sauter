import pandas as pd
import numpy as np
import pandas_gbq

from google_play_scraper import reviews_all
from google.oauth2 import service_account
from google.cloud import bigquery
from pandas.io import gbq

pd.options.display.max_columns = None

alexa_resultado = reviews_all(
    "com.amazon.dee.app",
    lang="pt",
    country="br"
)

alexa_df = pd.DataFrame.from_dict(alexa_resultado)

alexa_df = alexa_df.drop(["reviewId", "userName", "userImage", "replyContent", "repliedAt"], axis=1)

alexa_df.columns = [x.upper() for x in alexa_df.columns]

alexa_df["CONTENT"] = alexa_df["CONTENT"].str.strip()
alexa_df["CONTENT"] = alexa_df["CONTENT"].str.upper()
alexa_df["CONTENT"] = alexa_df["CONTENT"].replace('"', '\"')

cols = alexa_df.select_dtypes(include=[np.object]).columns
alexa_df[cols] = alexa_df[cols].apply(lambda x: x.str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8'))

alexa_df = alexa_df.dropna()

positivo = alexa_df.loc[alexa_df["SCORE"] >= 4]
positivo = positivo[:-10]

neutro = alexa_df.loc[alexa_df["SCORE"] == 3]
neutro = neutro[:-10]

negativo = alexa_df.loc[alexa_df["SCORE"] < 3]
negativo = negativo[:-10]

positivo.to_csv(r"C:/Users/Mayara Lopes/Desktop/sauter/positivo.csv", index=False)
neutro.to_csv(r"C:/Users/Mayara Lopes/Desktop/sauter/neutro.csv", index=False)
negativo.to_csv(r"C:/Users/Mayara Lopes/Desktop/sauter/negativo.csv", index=False)

key_path = "GBQ.json"

credentials = service_account.Credentials.from_service_account_file(
    key_path, scopes=["https://www.googleapis.com/auth/cloud-plataform"]
)

positivo.to_gbq(project_id="folkloric-rite-336521",
                destination_table="alexa_data.positivo",
                if_exists="replace")
