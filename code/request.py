# 1º passo, impotar todas as bibliotecas necessárias 
import psycopg2
import pandas as pd

# 2º passo, realizar a conecxão com o bando de dados do Neon
conn = psycopg2.connect(
    host="ep-empty-butterfly-a80jq6wq-pooler.eastus2.azure.neon.tech", #Código do host na neon
    database="neondb", # nome do banco de dados criado no Neon
    user="neondb_owner", # usuário do bando de dados 
    password="npg_tyFNIJXP9j7g", # senha do banco de dados
    port="5432", # porta padrão do banco de dados 
    sslmode="require" # modo de segurança para conexão com o bando de dados
)
print("Conexão realizada com sucesso!")


# 3º passo, criar um cursor para executar comandos SQL
cursor = conn.cursor()
# 4º passo, criar uma tabela no bancco de dados
cursor.execute("""
    CREATE TABLE IF NOT EXISTS carros (
        id SERIAL PRIMARY KEY,
        marca VARCHAR(50) NOT NULL,
        modelo VARCHAR(50) NOT NULL,
        ano INT NOT NULL,
        motor VARCHAR(50) NOT NULL
    )
""")
print("Tabela criada com sucesso!")

# 5º passo, inserir dados na tabela criada
cursor.execute("""
    INSERT INTO carros (marca, modelo, ano, motor)
    VALUES
        ('Golf', 'GTI', 2020, 'EA888'),
        ('Civic', 'SI', 2008, 'K20'),
        ('Subaru', 'STI', 2015, 'EJ25');
""")
print("Dados inseridos com sucesso!")

# 6º passo, commitar as alterações no banco de dados
conn.commit()
print("Alterações commitadas com sucesso!")
