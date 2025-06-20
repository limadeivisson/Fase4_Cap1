import sqlite3
import pandas as pd
import os

# Criação da pasta db se não existir
os.makedirs("db", exist_ok=True)

# Dados simulados
dados = {
    "umidade": [40, 30, 20, 70, 60, 55, 25, 45, 65, 15],
    "nutrientes": [70, 65, 60, 80, 75, 78, 50, 68, 82, 40],
    "hora": [6, 7, 8, 12, 13, 14, 9, 10, 11, 15],
    "precisa_irrigar": [1, 1, 1, 0, 0, 0, 1, 1, 0, 1]
}
df = pd.DataFrame(dados)

# Conexão e gravação
con = sqlite3.connect("db/sensores.db")
df.to_sql("leituras", con, if_exists="replace", index=False)
con.close()

print("Base SQLite criada com sucesso.")
