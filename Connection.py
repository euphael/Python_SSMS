# CONEXAO 1:


# import pyodbc

# conn_str = (
#     r'DRIVER={SQL Server};'
#     r'SERVER=RAPHAEL;' 
#     r'DATABASE=master;'
#     r'Trusted_Connection=yes;'
# )

# # Conectando ao banco de dados
# conn = pyodbc.connect(conn_str)

# # Exemplo de execução de consulta
# cursor = conn.cursor()
# cursor.execute('SELECT @@VERSION')
# row = cursor.fetchone()
# print(f'Versão do SQL Server: {row[0]}')


# queryTeste = "SELECT * FROM dbo.Cliente"
# cursor.execute(queryTeste)
# row = cursor.fetchall()
# print(row)

# # Fechar conexão
# conn.close()

# CONEXAO 2:


import json
import pandas as pd
from sqlalchemy import create_engine

#Conexão no banco principal
conexao = (
    "mssql+pyodbc:///?odbc_connect=" + 
    "DRIVER={ODBC Driver 17 for SQL Server};" +
    "SERVER=RAPHAEL;" +
    "DATABASE=master;" +
    "Trusted_Connection=yes"
)

engine = create_engine(conexao, pool_pre_ping=True)

def receberDados(query):
    response = pd.read_sql_query(query, engine)
    resultadosJson = response.to_json(orient='records')
    dadosDesserializados = json.loads(resultadosJson)
    return dadosDesserializados

def selectCliente():
    query = "SELECT * FROM dbo.Cliente"
    dados_cliente = receberDados(query)
    return dados_cliente


dados_cliente = selectCliente()
for cliente in dados_cliente:
    print(cliente)

