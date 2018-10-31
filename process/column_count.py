
# coding: utf-8

# In[1]:


import findspark
findspark.init()
import pyspark
from pyspark.sql.types import StructType
from pyspark.sql.types import StructField
from pyspark.sql.types import StringType
from pyspark.sql import SQLContext
import pandas as pd
sc =pyspark.SparkContext(appName="Pi")
sqlc = SQLContext(sc)


# In[2]:

basic_folder ="/home/project/project_lastest/output/"
basic_folder_spark ="hdfs://master:9000/project_lastest/"
input_name=basic_folder+"result_all_nocontent.csv"
output_name_company = basic_folder_spark+"company_result"
output_name_city = basic_folder_spark+"city_result"
output_name_state =basic_folder_spark+"state_result"

# rdd_city = rdd.map(lambda x=>(x[2],x[0])).groupByKey()
# rdd_state = rdd.map(lambda x=>(x[3],x[0])).groupByKey()
column_company = ["company","job","frequency"]
column_city = ["city","job","frequency"]
column_state = ["state","job","frequency"]

rdd = sc.textFile(input_name).map(lambda line:line.replace('\"','')).map(lambda line:line.split(","))

# In[3]:


rdd_company =rdd.map(lambda x:(x[2].strip(),x[1]))
wordcount_company = rdd_company.map(lambda x: (x,1)).reduceByKey(lambda x,y:x+y).map(lambda x:[x[0][0],x[0][1],x[1]])
df_company = sqlc.createDataFrame(wordcount_company)

rdd_city =rdd.map(lambda x:(x[3].strip(),x[1]))
wordcount_city = rdd_city.map(lambda x: (x,1)).reduceByKey(lambda x,y:x+y).map(lambda x:[x[0][0],x[0][1],x[1]])
df_city = sqlc.createDataFrame(wordcount_city)

rdd_state =rdd.map(lambda x:(x[4].strip(),x[1]))
wordcount_state = rdd_state.map(lambda x: (x,1)).reduceByKey(lambda x,y:x+y).map(lambda x:[x[0][0],x[0][1],x[1]])
df_state = sqlc.createDataFrame(wordcount_state)


df_company.write.format("com.databricks.spark.csv").save(output_name_company)
df_city.write.format("com.databricks.spark.csv").save(output_name_city)
df_state.write.format("com.databricks.spark.csv").save(output_name_state)

# In[5]:


pd_company= df_company.toPandas()
pd_company.columns = column_company
pd_company.to_csv(output_name_company,index=False, encoding='utf-8')

pd_city= df_city.toPandas()
pd_city.columns = column_city
pd_city.to_csv(output_name_city,index=False, encoding='utf-8')

pd_state= df_state.toPandas()
pd_state.columns = column_state
pd_state.to_csv(output_name_state,index=False, encoding='utf-8')

