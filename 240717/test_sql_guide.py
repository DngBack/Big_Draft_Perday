import os
import openai
from dotenv import load_dotenv
from llama_index.core import SQLDatabase
from llama_index.llms.openai import OpenAI
from llama_index.core import SQLDatabase

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

engine = create_engine("sqlite:///:memory:")
metadata_obj = MetaData()

# create city SQL table
table_name = "city_stats"
city_stats_table = Table(
    table_name,
    metadata_obj,
    Column("city_name", String(16), primary_key=True),
    Column("population", Integer),
    Column("country", String(16), nullable=False),
)
metadata_obj.create_all(engine)

from llama_index.core import SQLDatabase
from llama_index.llms.openai import OpenAI

llm = OpenAI(temperature=0.1, model="gpt-3.5-turbo")

sql_database = SQLDatabase(engine, include_tables=["city_stats"])

sql_database = SQLDatabase(engine, include_tables=["city_stats"])
from sqlalchemy import insert

rows = [
    {"city_name": "Toronto", "population": 2930000, "country": "Canada"},
    {"city_name": "Tokyo", "population": 13960000, "country": "Japan"},
    {
        "city_name": "Chicago",
        "population": 2679000,
        "country": "United States",
    },
    {"city_name": "Seoul", "population": 9776000, "country": "South Korea"},
]
for row in rows:
    stmt = insert(city_stats_table).values(**row)
    with engine.begin() as connection:
        cursor = connection.execute(stmt)
        

from llama_index.core.query_engine import NLSQLTableQueryEngine

query_engine = NLSQLTableQueryEngine(
    sql_database=sql_database, tables=["city_stats"], llm=llm
)
query_str = "Which city has the highest population?"
response = query_engine.query(query_str)
print(response)
