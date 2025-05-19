# 🌿 Projeto FIAP – Fase 3: Simulação de Sistema de Irrigação Inteligente

[![GitHub](https://img.shields.io/badge/Grupo-FarmTech%20Solutions-green)](https://github.com/seu-grupo/exemplo)
[![Turma](https://img.shields.io/badge/Turma-1TIAOB%2F2025-blue)]()
[![Status](https://img.shields.io/badge/Status-Concluído-success)]()

---

## 💡 Descrição

Este projeto foi desenvolvido como parte da atividade avaliativa da FIAP para a Fase 3, com foco em sensores, automação com ESP32, lógica de controle embarcado e simulação de banco de dados com Python. A proposta simula uma máquina agrícola inteligente que coleta dados de sensores e aciona uma bomba de irrigação com base em regras lógicas.

---

## 🎯 Objetivos

* Coletar dados de sensores simulados de umidade, pH, fósforo e potássio
* Simular um circuito funcional no Wokwi com ESP32
* Aplicar a lógica de decisão para ligar/desligar a bomba via relé
* Armazenar dados em banco SQLite com Python e realizar CRUD
* (Opcional) Exibir dados em dashboard e integrar com API de clima

---

## 🔧 Componentes Simulados no Wokwi

* ESP32 DevKit v1
* Sensor de Umidade/Temperatura DHT22
* LDR (simula sensor de pH)
* Botões para simular presença de Fósforo (P) e Potássio (K)
* Relé com LED para indicar ativação da bomba de irrigação

---

## 🧠 Lógica de Controle

* Se a **umidade < 50%** E **P ou K estiverem presentes** → **bomba ligada**
* Caso contrário, a bomba permanece desligada
* O valor analógico do LDR é usado como referência para pH (0–14)

---

## 📦 Estrutura do Projeto

```
projeto-irrigacao/
├── src/
│   └── main.ino                   # Código C++ para ESP32
├── diagram.json                  # Circuito Wokwi
├── platformio.ini                # Configuração PlatformIO
├── .gitignore                    # Exclusões de build
├── docs/
│   └── README_detalhado.txt
├── python_db/
│   ├── simulacao_banco.py        # Banco SQLite e CRUD
│   ├── dashboard.py              # Visualização com Streamlit
│   ├── api_clima.py              # Integração com OpenWeatherMap
│   └── requirements.txt
└── README.md                     # Documentação geral do projeto
```

---

## 🧪 Banco de Dados (Python + SQLite)

* Tabela: `leitura_sensores`

* Campos:

  * umidade (REAL), temperatura (REAL), ph\_analogico (INTEGER)
  * fosforo\_presente (BOOLEAN), potassio\_presente (BOOLEAN)
  * irrigacao\_ativa (BOOLEAN), timestamp (DATETIME)

* Operações implementadas:

  * Inserção de dados
  * Atualização de registros
  * Consulta e remoção

---

## 📊 Dashboard Interativo ("Ir Além")

* Visualiza os dados armazenados no banco
* Gráficos de umidade, pH e estado do relé
* Desenvolvido com **Streamlit**

## 🌦 Integração com API Climática ("Ir Além")

* Busca previsão do tempo em tempo real (OpenWeatherMap)
* Lógica condicional: **se houver previsão de chuva, bomba é desativada**

---

## 📥 Instalação e Execução

### Wokwi

1. Acesse [https://wokwi.com](https://wokwi.com)
2. Crie novo projeto com ESP32
3. Substitua `main.ino` e `diagram.json`
4. Rode a simulação e acompanhe pelo Serial Monitor

### Python (Windows/Linux/Mac)

```bash
pip install -r python_db/requirements.txt
python python_db/simulacao_banco.py  # CRUD
streamlit run python_db/dashboard.py  # Dashboard
```

---

## 👥 Integrantes do Grupo

* Deivisson Gonçalves Lima – RM565095 – [deivisson.engtele@gmail.com](mailto:deivisson.engtele@gmail.com)
* Lucian Paiva Binner – RM563350 – [lucian.binner@hotmail.com](mailto:lucian.binner@hotmail.com)
* Omar Calil Abrão Mustafá Assem – RM561375 – [ocama12@gmail.com](mailto:ocama12@gmail.com)
* Paulo Henrique de Sousa – RM564262 – [pauloo.sousa16@outlook.com](mailto:pauloo.sousa16@outlook.com)
* Renan Danilo dos Santos Pereira – RM566175 – [renansantos4978@gmail.com](mailto:renansantos4978@gmail.com)

---

## ✅ Status

Entrega finalizada com sucesso e repositório documentado. Pronto para apresentação e/ou publicação.
