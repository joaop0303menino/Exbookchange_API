from sqlalchemy import create_engine 
from urllib.parse import quote_plus
from dotenv import load_dotenv
import os

load_dotenv()

DB = os.getenv("Url_DB")
#Connection with database
engine = create_engine(DB)

try:
    with engine.connect() as conn:
        print("Conexão bem-sucedida!")
except Exception as e:
    print("Erro de conexão:", e)