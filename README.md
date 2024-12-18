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
