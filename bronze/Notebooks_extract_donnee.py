# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "5"
# ///
# MAGIC %md
# MAGIC Notebook extract de données databricks 

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **import fichier csv** 
# MAGIC
# MAGIC DEPUIS UN VOLUME
# MAGIC
# MAGIC

# COMMAND ----------

path = "/Volumes/databricks_gaelle/default/donnees_api/ent_comm_detail.csv"
df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .option("delimiter", ";")
    .csv(path))
display(df)
df.printSchema()
print("Nombre de lignes :", df.count())




### "test de push"
