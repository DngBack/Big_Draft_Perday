import os
import openai
from dotenv import load_dotenv
from llama_index.core import SQLDatabase, VectorStoreIndex
from llama_index.llms.openai import OpenAI
from llama_index.core import SQLDatabase
from llama_index.core.objects import SQLTableSchema, SQLTableNodeMapping, ObjectIndex

from llama_index.core.retrievers import NLSQLRetriever

from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    String,
    Integer,
    select,
)

load_dotenv(".env")
openai_config = os.getenv("OPENAI_API_KEY")

os.environ["OPENAI_API_KEY"] = openai_config
openai.api_key = os.environ["OPENAI_API_KEY"]
llm = OpenAI(temperature=0.1, model="gpt-3.5-turbo")
# db = SQLDatabase.from_uri("sqlite:///bike_store.db")

sql_url = "sqlite:///bike_store.db"
engine = create_engine(sql_url)

# load all table definitions
metadata_obj = MetaData()
metadata_obj.reflect(engine)

sql_database = SQLDatabase(engine)

table_node_mapping = SQLTableNodeMapping(sql_database)

table_schema_objs = []
for table_name in metadata_obj.tables.keys():
    table_schema_objs.append(SQLTableSchema(table_name=table_name))

# sql_database = SQLDatabase(engine, include_tables=["brands", "stores", "staffs", "orders", "customers", \
#         "products",  "order_items", "stocks", "categories"])
# We dump the table schema information into a vector index. The vector index is stored within the context builder for future use.
obj_index = ObjectIndex.from_objects(
    table_schema_objs,
    table_node_mapping,
    VectorStoreIndex,
)

from llama_index.core.query_engine import NLSQLTableQueryEngine

llm = OpenAI(temperature=0.1, model="gpt-3.5-turbo")

# query_engine = NLSQLTableQueryEngine(
#     sql_database=sql_database,
#     llm=llm
# )
# query_str = "How many brands of this bike store?"
# response = query_engine.query(query_str)

# print(str(response))
# default retrieval (return_raw=True)
nl_sql_retriever = NLSQLRetriever(
    sql_database=sql_database, return_raw=True
)

results = nl_sql_retriever.retrieve(
    "Return the top 5 staff with the highest manager_id."
)
print(results)
