#%%
import pandas as pd
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
import findspark

# %%
findspark.init()

# %%
conf = SparkConf().setAppName('appName').setMaster('spark://localhost:7077')
sc = SparkContext(conf=conf)
spark = SparkSession(sc)

# %%
pandas_df = pd.DataFrame({'make':['Jaguar', 'MG', 'MINI', 'Rover', 'Lotus'],
                          'registration':['AB98ABCD','BC99BCDF','CD00CDE','DE01DEF','EF02EFG'],
                          'year':[1998,1999,2000,2001,2002]})

# %%
spark_df = spark.createDataFrame(pandas_df)

# %%
spark_df.show()
# %%
