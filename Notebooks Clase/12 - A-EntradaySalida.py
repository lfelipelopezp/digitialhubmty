# Databricks notebook source
# MAGIC %md
# MAGIC Archivos

# COMMAND ----------

#1.- athlete_events.csv
#2.- PopularCreativeTypes.csv

# COMMAND ----------

!pip install pandas

# COMMAND ----------

import pandas as pd
import numpy as np

# COMMAND ----------

datos1=pd.read_csv("C:\Users\isaac.cedeno\Downloads\athlete_events.csv")

# COMMAND ----------

#\U está apartado por el sistema para una operación

# COMMAND ----------

datos1=pd.read_csv("C:\\Users\\isaac.cedeno\\Downloads\\athlete_events.csv")

# COMMAND ----------

datos2=pd.read_csv("PopularCreativeTypes.csv")

# COMMAND ----------

datos1

# COMMAND ----------

#datos2

# COMMAND ----------

datos1["Games"].unique().tolist()

# COMMAND ----------

datos1["Sport"] == "Judo"

# COMMAND ----------

datosJudo=datos1[datos1["Sport"]=="Judo"]

# COMMAND ----------

datosJudo

# COMMAND ----------

datosFut=datos1[datos1["Sport"]=="Football"]
datosFut

# COMMAND ----------

datosFut["Sex"].count()

# COMMAND ----------

datosFut["Sex"].value_counts()

# COMMAND ----------

datosFut["Age"].max()

# COMMAND ----------

datosFut["Age"].min()

# COMMAND ----------

datosFut[datosFut["Age"]==15]

# COMMAND ----------

datosFut[datosFut["Age"]==40]

# COMMAND ----------

OrdWeight=datosFut.sort_values(by=["Weight"])
OrdWeight

# COMMAND ----------

OrdAge=datosFut.sort_values(by=["Age"])

# COMMAND ----------

OrdAge

# COMMAND ----------

OrdAge[OrdAge["Age"].notna()]

# COMMAND ----------



# COMMAND ----------



# COMMAND ----------


