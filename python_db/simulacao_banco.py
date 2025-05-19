import sqlite3
import time
import random

# Nome do banco de dados
DATABASE_FILE = 'dados_irrigacao.db'

def criar_tabela():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS leitura_sensores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            umidade REAL,
            temperatura REAL,
            ph_analogico INTEGER,
            fosforo_presente BOOLEAN,
            potassio_presente BOOLEAN,
            irrigacao_ativa BOOLEAN
        )
    ''')
    conn.commit()
    conn.close()
    print("Tabela criada (se necessário).")

def inserir_dados(umidade, temperatura, ph, fosforo, potassio, irrigacao):
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO leitura_sensores (umidade, temperatura, ph_analogico, fosforo_presente, potassio_presente, irrigacao_ativa)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (umidade, temperatura, ph, fosforo, potassio, irrigacao))
    conn.commit()
    conn.close()
    print("Dados inseridos com sucesso.")

def consultar_dados():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM leitura_sensores ORDER BY timestamp DESC")
    dados = cursor.fetchall()
    conn.close()
    print("\n--- Leitura dos dados ---")
    for row in dados:
        print(row)

def atualizar_umidade(id_registro, nova_umidade):
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE leitura_sensores
        SET umidade = ?
        WHERE id = ?
    ''', (nova_umidade, id_registro))
    conn.commit()
    conn.close()
    print(f"Umidade atualizada para o registro {id_registro}.")

def remover_dado(id_registro):
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM leitura_sensores WHERE id = ?", (id_registro,))
    conn.commit()
    conn.close()
    print(f"Registro {id_registro} removido.")

if __name__ == "__main__":
    criar_tabela()

    print("\nInserindo dados simulados...")
    for _ in range(5):
        umidade = round(random.uniform(30, 80), 2)
        temperatura = round(random.uniform(20, 30), 2)
        ph = random.randint(200, 800)
        fosforo = random.choice([True, False])
        potassio = random.choice([True, False])
        irrigacao = random.choice([True, False])
        inserir_dados(umidade, temperatura, ph, fosforo, potassio, irrigacao)
        time.sleep(0.5)

    consultar_dados()
